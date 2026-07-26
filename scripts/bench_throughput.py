"""Throughput for a ternary GGUF model, read from llama-cli's own timings.

llama-bench would be the obvious tool, but it segfaults on the bitnet.cpp build
I have (it prints the table header and dies). llama-cli reports prompt-eval and
generation rates itself on stderr, and has the advantage of measuring the path
you would actually run.
"""

import argparse
import json
import platform
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

from common import EmptyOutput, add_common_args, generate, parse_perf, resolve_paths

# Fixed, reasonably long prompt so prompt-eval is measured over something real.
PROMPT = (
    "You are assisting a maintenance engineer on a factory floor. A conveyor "
    "motor on line 3 is drawing about 15 percent more current than its recorded "
    "baseline and is running roughly 8 degrees hotter than normal. The line has "
    "been in continuous operation for eleven days since the last scheduled stop. "
    "Vibration on the drive end was measured last week and was within tolerance. "
    "The ambient temperature in the building has not changed. Explain the three "
    "most likely causes of this behaviour, say which one you would check first "
    "and why, and describe what measurement would confirm or rule it out."
)


def parse_args():
    p = argparse.ArgumentParser()
    add_common_args(p)
    p.add_argument("--gen-tokens", type=int, default=128)
    p.add_argument("--repeats", type=int, default=3)
    p.add_argument("--out", default="results/raw/throughput.json")
    return p.parse_args()


def main():
    args = parse_args()
    binary, model = resolve_paths(args)

    print(f"model:   {model.name}")
    print(f"threads: {args.threads}   ctx: {args.ctx}   n_predict: {args.gen_tokens}")
    print(f"repeats: {args.repeats}\n")

    runs = []
    for i in range(args.repeats):
        try:
            _, stderr = generate(
                binary, model, PROMPT,
                n_predict=args.gen_tokens, threads=args.threads,
                ctx=args.ctx, seed=args.seed, temp=0.0,
            )
        except EmptyOutput as e:
            sys.exit(f"Run {i + 1} generated nothing — stopping.\n\n{e}")

        perf = parse_perf(stderr)
        if "generation_tokens_per_s" not in perf:
            sys.exit(
                "Could not find timing lines in llama-cli output. "
                "Expected 'llama_perf_context_print: eval time'.\n\n"
                + stderr[-1500:]
            )
        runs.append(perf)
        print(
            f"  run {i + 1}/{args.repeats}: "
            f"generation {perf['generation_tokens_per_s']:.2f} tok/s, "
            f"prompt eval {perf.get('prompt_eval_tokens_per_s', float('nan')):.2f} tok/s"
        )

    def median_of(key):
        vals = [r[key] for r in runs if key in r]
        return round(statistics.median(vals), 2) if vals else None

    result = {
        "recorded_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model_file": model.name,
        "machine": f"{platform.system()} {platform.release()} / {platform.machine()}",
        "threads": args.threads,
        "context": args.ctx,
        "n_predict": args.gen_tokens,
        "gpu_layers": 0,
        "batch": 1,
        "repeats": args.repeats,
        "generation_tokens_per_s_median": median_of("generation_tokens_per_s"),
        "prompt_eval_tokens_per_s_median": median_of("prompt_eval_tokens_per_s"),
        "model_load_ms_median": median_of("model_load_ms"),
        "runs": runs,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2))

    print("\n--- medians ---")
    print(f"generation:  {result['generation_tokens_per_s_median']} tok/s")
    print(f"prompt eval: {result['prompt_eval_tokens_per_s_median']} tok/s")
    print(f"model load:  {result['model_load_ms_median']} ms")
    print(f"\nwritten to {out_path}")


if __name__ == "__main__":
    main()
