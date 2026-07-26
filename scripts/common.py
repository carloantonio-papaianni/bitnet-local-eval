"""Shared helpers: locate the bitnet.cpp build and call llama-cli."""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


class EmptyOutput(RuntimeError):
    """llama-cli returned success but generated nothing."""


def resolve_paths(args):
    """Binary and model come from --bin/--model, else $BITNET_DIR.

    Nothing is hardcoded: the checkout lives outside this repo and its path
    is never written to a committed file.
    """
    if args.bin and args.model:
        return Path(args.bin), Path(args.model)

    root = os.environ.get("BITNET_DIR")
    if not root:
        sys.exit(
            "Set BITNET_DIR to your bitnet.cpp checkout, or pass --bin and --model.\n"
            '  export BITNET_DIR="/path/to/BitNet"'
        )
    root = Path(root).expanduser()
    binary = Path(args.bin) if args.bin else root / "build" / "bin" / "llama-cli"
    model = (
        Path(args.model)
        if args.model
        else root / "models" / "BitNet-b1.58-2B-4T" / "ggml-model-i2_s.gguf"
    )

    if not binary.exists():
        sys.exit(f"llama-cli not found at {binary}")
    if not model.exists():
        sys.exit(f"model not found at {model}")
    return binary, model


def add_common_args(p):
    p.add_argument("--bin", help="path to llama-cli (default: $BITNET_DIR/build/bin/llama-cli)")
    p.add_argument("--model", help="path to the .gguf (default: under $BITNET_DIR/models)")
    p.add_argument("--threads", type=int, default=4)
    p.add_argument("--ctx", type=int, default=2048)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--temp", type=float, default=0.0,
                   help="0 = greedy. Reproducible, but degenerates without a repeat penalty.")
    p.add_argument("--repeat-penalty", type=float, default=1.1,
                   help="1.0 = off. Greedy + 1.0 sends this model into repetition loops.")


def generate(binary, model, prompt, n_predict, threads, ctx, seed,
             temp=0.0, repeat_penalty=1.1):
    """One-shot completion. Returns (text, stderr).

    Prompts are sent verbatim, with no chat template. This GGUF ships without
    one, and hand-applying the Llama-3 special tokens makes the model emit
    end-of-text immediately and produce nothing. Sending the instruction as a
    plain completion works, and keeps the prompt in one language rather than
    wrapping non-English prompts in English scaffolding.

    repeat_penalty defaults to 1.1 rather than off. Greedy decoding with no
    penalty makes this model loop on a single phrase for the whole budget, in
    every language — which looks like a language failure and is not one.
    """
    with tempfile.NamedTemporaryFile(
        "w", suffix=".txt", delete=False, encoding="utf-8"
    ) as f:
        f.write(prompt)
        prompt_file = f.name

    cmd = [
        str(binary),
        "-m", str(model),
        "-f", prompt_file,
        "-n", str(n_predict),
        "-t", str(threads),
        "-c", str(ctx),
        "--temp", str(temp),
        "--seed", str(seed),
        "--repeat-penalty", str(repeat_penalty),
        "-ngl", "0",
        "-b", "1",
        "--no-display-prompt",
        "--simple-io",
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    finally:
        os.unlink(prompt_file)

    if proc.returncode != 0:
        raise RuntimeError(
            f"llama-cli exited {proc.returncode}\n"
            f"command: {' '.join(cmd)}\n\n{proc.stderr[-2000:]}"
        )

    text = proc.stdout.replace("[end of text]", "").strip()
    if not text:
        raise EmptyOutput(
            "llama-cli produced no text.\n"
            f"command: {' '.join(cmd)}\n"
            f"prompt was:\n{prompt[:300]}\n\n"
            f"stderr tail:\n{proc.stderr[-1200:]}"
        )
    return text, proc.stderr


PERF_PROMPT = re.compile(
    r"prompt eval time\s*=.*?([0-9.]+)\s*tokens per second", re.S
)
PERF_EVAL = re.compile(
    r"llama_perf_context_print:\s+eval time\s*=.*?([0-9.]+)\s*tokens per second", re.S
)
PERF_LOAD = re.compile(r"load time\s*=\s*([0-9.]+)\s*ms")


def parse_perf(stderr):
    """llama-cli prints its own timings; llama-bench segfaults on this build."""
    out = {}
    for key, rx in (
        ("prompt_eval_tokens_per_s", PERF_PROMPT),
        ("generation_tokens_per_s", PERF_EVAL),
    ):
        m = rx.search(stderr)
        if m:
            out[key] = float(m.group(1))
    m = PERF_LOAD.search(stderr)
    if m:
        out["model_load_ms"] = float(m.group(1))
    return out
