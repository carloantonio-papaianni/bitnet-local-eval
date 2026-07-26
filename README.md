# bitnet-local-eval

Notes and scripts from running [BitNet b1.58 2B](https://huggingface.co/microsoft/BitNet-b1.58-2B-4T-gguf) locally on an ordinary laptop CPU, through [bitnet.cpp](https://github.com/microsoft/BitNet).

I'm interested in ternary-weight models for edge inference, so before forming an opinion I wanted to answer two questions myself rather than read someone else's benchmark:

1. What throughput does a 2B ternary model actually get on a CPU that is not a datacentre part?
2. How much worse does it get outside English? Published evals for small models are overwhelmingly English-only, and the use cases I care about are not.

This is the harness I used and what I found. It is deliberately small — two scripts and a prompt file. It is not a framework.

## What's here

```
scripts/common.py              the llama-cli call and the timing parser
scripts/bench_throughput.py    throughput, read from llama-cli's own timings
scripts/multilingual_check.py  same 12 prompts in English / Italian / Spanish
scripts/compare_runs.py        repetition scores across decoding settings
prompts/multilingual.jsonl     the prompt set
results/RESULTS.md             my numbers and my reading of them
```

## Prerequisites

You need a working [bitnet.cpp](https://github.com/microsoft/BitNet) build and the GGUF weights — this repo vendors neither. Follow their README, then confirm you have `build/bin/llama-cli` and a `ggml-model-i2_s.gguf`. Python 3.9+, standard library only. No pip install, no torch.

## Running it

```bash
export BITNET_DIR="/path/to/your/BitNet"

python scripts/bench_throughput.py --threads 4 --repeats 3
python scripts/multilingual_check.py --threads 4 --temp 0.8 --repeat-penalty 1.1 --tag temp08
python scripts/compare_runs.py
```

`--tag` keeps runs apart so you can compare decoding settings instead of overwriting them. That turned out to matter more than anything else here.

Both accept `--bin` and `--model` if your layout differs. Nothing about your local paths is written to any committed file.

Defaults are `--temp 0` and `--repeat-penalty 1.1`, with a fixed seed. Greedy decoding makes runs reproducible, but greedy with the penalty off sends this model into repetition loops — see the results — so if you only run one configuration, use `--temp 0.8 --repeat-penalty 1.1`.

Three things I had to work around, all worth knowing if you try this yourself:

`llama-bench` segfaults on my bitnet.cpp build — it prints the table header and dies. Throughput therefore comes from `llama-cli`'s own `llama_perf_context_print` lines instead, which has the side benefit of measuring the path you would actually run rather than a synthetic one.

Prompts are sent verbatim, with no chat template. This GGUF ships without one, and hand-applying the Llama-3 special tokens made the model emit end-of-text immediately and return nothing at all. Sending each instruction as a plain completion works, and it avoids wrapping the Italian and Spanish prompts in English scaffolding, which would bias which language the model answers in — the exact thing this repo is trying to measure.

## What I found

Full detail, with the numbers, in [results/RESULTS.md](results/RESULTS.md).

**15 tokens per second on generation**, on a six-year-old Intel laptop with no GPU, and the model loads in under a second. Faster than most people read, and nowhere near enough for two people at once. That gap is the whole reason the hardware question is worth asking.

**My first conclusion was wrong, and the way it was wrong is the interesting part.** I ran everything greedy with no repetition penalty, for reproducibility. Every language collapsed into loops and it looked like a broken model. It was a broken harness: fixing the decoding took the repetition score in English from 0.60 to 0.04. Anyone publishing off that first run would have been describing their own sampler and calling it a model evaluation.

**The language gap survived the correction, and is not uniform.** Under identical, properly-configured decoding, Italian scores 0.17 on repetition against 0.04 for English and 0.05 for Spanish. Reading the outputs, Spanish holds up close to English — grammatical, structurally sound — while Italian breaks grammar, code-switches into English mid-sentence, and loses the subject. "Worse the further you get from English" is not what is happening; it is per-language and has to be measured that way.

**It hallucinates instead of declining, under every setting.** Asked for a fact it could not hold, it produced a fluent, specific, invented answer in all three languages and all three decoding configurations. Sampling does not touch this. For anything grounded in retrieved context, the model will not tell you when it is outside what it knows, so the system around it has to.

**Instruction-following degrades faster than fluency.** Told to answer in exactly five words, nothing complied, in any language, under any setting. Fixing the sampler makes output read better; it does not make it obey.

## Caveats

One machine, one model, one person's prompt set. The language comparison is my own reading of the outputs, not a scored benchmark — I speak Italian natively and Spanish daily, which is why I judged those two and did not attempt others. Everything is reproducible from what is here; if you get different numbers I'd like to know.

## Licence

MIT.
