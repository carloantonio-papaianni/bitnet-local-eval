"""Compare runs produced under different decoding settings.

The repetition score is a crude but objective measure of degeneration: the
fraction of word trigrams in an output that are not unique. 0 means nothing
repeats, 1 means the output is a single phrase looping. It exists because the
first run of this harness looked like a language failure and was mostly a
decoding failure, and eyeballing could not tell the two apart.
"""

import argparse
import json
from pathlib import Path


def repetition_score(text):
    words = text.split()
    if len(words) < 6:
        return 0.0
    trigrams = [tuple(words[i:i + 3]) for i in range(len(words) - 2)]
    return 1 - len(set(trigrams)) / len(trigrams)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", default="results/raw")
    p.add_argument("--show", nargs="*", default=["p05", "p11"],
                   help="prompt ids to print side by side")
    p.add_argument("--chars", type=int, default=220)
    return p.parse_args()


def main():
    args = parse_args()
    raw = Path(args.dir)

    runs = {}
    for path in sorted(raw.glob("multilingual_*.json")):
        label = path.stem.replace("multilingual_", "")
        runs[label] = json.loads(path.read_text(encoding="utf-8"))

    if not runs:
        raise SystemExit(f"no multilingual_*.json files in {raw}")

    langs = ("en", "it", "es")
    width = max(len(k) for k in runs) + 2

    print("Repetition score — 0 is clean, 1 is a single phrase looping\n")
    print("run".ljust(width) + "".join(l.upper().rjust(8) for l in langs))
    print("-" * (width + 8 * len(langs)))
    for label, rows in runs.items():
        line = label.ljust(width)
        for lang in langs:
            scores = [repetition_score(r["output"]) for r in rows if r["lang"] == lang]
            line += f"{sum(scores) / len(scores):8.2f}"
        print(line)

    for pid in args.show:
        print(f"\n\n{'=' * 70}\n{pid}\n{'=' * 70}")
        for label, rows in runs.items():
            print(f"\n--- {label} ---")
            for r in rows:
                if r["id"] == pid:
                    snippet = r["output"][:args.chars].replace("\n", " ")
                    print(f"  [{r['lang'].upper()}] {snippet}")


if __name__ == "__main__":
    main()
