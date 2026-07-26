"""Run the same prompt set in English, Italian and Spanish; save outputs to read.

No automatic scoring, on purpose. Small-model failures in a language you speak
are obvious to a person and hard to catch with a metric, so this produces a
side-by-side file and leaves the judgement to whoever reads it.

Prompts go in verbatim, with no chat template and no English scaffolding around
the non-English ones — otherwise the harness itself biases the answer language.
"""

import argparse
import json
import sys
import time
from pathlib import Path

from common import EmptyOutput, add_common_args, generate, resolve_paths

LANGS = ("en", "it", "es")


def parse_args():
    p = argparse.ArgumentParser()
    add_common_args(p)
    p.add_argument("--prompts", default="prompts/multilingual.jsonl")
    p.add_argument("--gen-tokens", type=int, default=160)
    p.add_argument("--out", default="results/raw")
    p.add_argument("--tag", default="", help="suffix for the output files, to keep runs apart")
    return p.parse_args()


def load_prompts(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    args = parse_args()
    binary, model = resolve_paths(args)
    prompts = load_prompts(args.prompts)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    total = len(prompts) * len(LANGS)
    done = 0
    started = time.time()

    for item in prompts:
        for lang in LANGS:
            user = item[lang]
            try:
                text, _ = generate(
                    binary, model, user,
                    n_predict=args.gen_tokens, threads=args.threads,
                    ctx=args.ctx, seed=args.seed,
                    temp=args.temp, repeat_penalty=args.repeat_penalty,
                )
            except EmptyOutput as e:
                # Fail on the first empty result rather than producing a file
                # full of nothing and looking like it worked.
                sys.exit(
                    f"\nStopped at {item['id']}/{lang}: no output generated.\n"
                    f"Nothing was written. Fix this before re-running.\n\n{e}"
                )

            rows.append({
                "id": item["id"], "category": item["category"], "lang": lang,
                "prompt": user, "output": text,
            })
            done += 1
            elapsed = time.time() - started
            eta = (elapsed / done) * (total - done)
            print(f"[{done}/{total}] {item['id']} {lang} "
                  f"({len(text)} chars, ~{eta / 60:.0f} min left)")

    suffix = f"_{args.tag}" if args.tag else ""
    (out_dir / f"multilingual{suffix}.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    lines = [
        "# Multilingual outputs", "",
        f"Same 12 prompts in English, Italian and Spanish. temp {args.temp}, "
        f"repeat penalty {args.repeat_penalty}, seed {args.seed}, "
        "no chat template, prompts sent verbatim.", "",
        "Read these. Don't trust a score.", "",
    ]
    for item in prompts:
        lines += [f"## {item['id']} — {item['category']}", ""]
        for lang in LANGS:
            row = next(r for r in rows if r["id"] == item["id"] and r["lang"] == lang)
            lines += [
                f"**{lang.upper()} prompt**", "",
                f"> {row['prompt']}", "",
                f"**{lang.upper()} output**", "",
                "```", row["output"], "```", "",
            ]
    (out_dir / f"multilingual{suffix}.md").write_text("\n".join(lines), encoding="utf-8")

    mins = (time.time() - started) / 60
    print(f"\nDone in {mins:.0f} min. Written to {out_dir}/multilingual{suffix}.json and .md")
    print("Read multilingual.md, then fill in the language table in results/RESULTS.md.")


if __name__ == "__main__":
    main()
