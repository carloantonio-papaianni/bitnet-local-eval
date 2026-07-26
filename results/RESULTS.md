# Results

## Setup

| | |
|---|---|
| Model | microsoft/BitNet-b1.58-2B-4T, GGUF, `i2_s` |
| Runtime | bitnet.cpp (llama.cpp fork), CPU only, `-ngl 0`, batch 1 |
| Machine | MacBook Pro, Intel x86_64, 16 GB RAM, AVX2, no AVX-512 |
| OS | macOS 13.7.8 |
| Threads | 4 |
| Context | 2048 |
| Date | 26 July 2026 |

This is an Intel laptop, not Apple Silicon. Numbers on an M-series part will be considerably better and are not comparable.

## Throughput

Median of 3 runs, 128 generated tokens each, from `llama-cli`'s own `llama_perf_context_print` output.

| Metric | Value |
|---|---|
| Generation | **15.0 tok/s** (runs: 16.42, 14.91, 15.00) |
| Prompt evaluation | 16.09 tok/s |
| Model load | 915 ms |

`llama-bench` would be the conventional tool here, but it segfaults on this build after printing the table header, so these are measured on real generations instead — which at least has the merit of being the path you would actually run.

**Reading of it.** Comfortable for one person typing at it and waiting: 15 tokens per second is faster than most people read. Nowhere near enough for anything concurrent, and the model reloads in under a second, which means the cost is all in inference and not in startup. Running a 2B model at conversational speed on a six-year-old Intel laptop with no GPU is the part worth noticing. The distance between that and serving real traffic is not something a better kernel closes.

## The mistake worth reporting

The first pass used greedy decoding (`--temp 0`) with no repetition penalty, chosen so that runs would be reproducible. Every language collapsed into loops — `"A) 420 units"` repeated through the alphabet, `"1 point:"` twenty times, the same Spanish sentence numbered one to seven. Read on its own it looked like a broken model.

It was mostly a broken harness. Repeating the same 36 prompts under three decoding settings:

| Run | EN | IT | ES |
|---|---|---|---|
| greedy, no repetition penalty | 0.60 | 0.44 | 0.58 |
| greedy, repetition penalty 1.1 | 0.24 | 0.32 | 0.29 |
| temp 0.8, repetition penalty 1.1 | **0.04** | **0.17** | **0.05** |

Repetition score is the fraction of word trigrams in an output that are not unique — 0 means nothing repeats, 1 means a single phrase looping. Reproduce with `scripts/compare_runs.py`.

Fixing the decoding removes almost all of it. English goes from 0.60 to 0.04. Anyone publishing "this model degenerates" off the first run would have been describing their own sampler.

## Language quality

With decoding controlled, the language difference survives — and it is the one number in the table above that does not collapse. Italian sits at 0.17 against 0.04 and 0.05, three to four times more repetitive than English and Spanish under identical settings.

Reading the outputs rather than the scores, the failures are different in kind:

| Language | Usable for a real task? | What breaks |
|---|---|---|
| English | For simple instructions, yes | Stays grammatical and on topic; drifts into invented follow-up questions nobody asked |
| Spanish | Borderline | Grammatical and structurally sound; reasoning often correct in shape, wrong in arithmetic |
| Italian | No | Grammar breaks down, code-switches into English mid-sentence, and loses the subject entirely |

Two examples, both from the best configuration.

Asked in three languages to compute output for a line running 6.5 hours at 420 units per hour with a 40-minute stoppage, English opens with a correct method — work out actual operating time, then multiply. Spanish does the same and reasons explicitly about how the stoppage affects total time. Italian writes *"420 pezzi / 40 minuti = 10.5 pezzi per minute"* — wrong operation, wrong unit, English word inside an Italian sentence — and lands on 420, which is the input rate rather than an answer.

Asked what most often causes bearing failure, English answers sensibly (lubrication, contamination, water ingress) and then invents an unrelated question about car batteries and answers that too. Spanish produces a degenerate list and a fabricated video link. Italian produces *"Piove a leggermente, ma non c'era un vario nel tempo. It's not worth the effort"* — meteorologically confused, ungrammatical, and half in English.

**Reading of it.** Benchmarks for small models are overwhelmingly English, and the drop-off outside English is steeper than the headline scores imply — but it is not uniform, and it is not simply "worse the further from English you get". Spanish, with roughly 500 million native speakers and presumably a large share of the training data, holds up close to English. Italian does not. For anything customer-facing outside the anglosphere, which language you are in is a first-order product constraint rather than a localisation detail, and it has to be measured per language rather than assumed from an aggregate score.

## What holds in every configuration

**It hallucinates instead of declining.** Asked for a serial number it could not possibly know, it produced a fluent, specific, invented answer in all three languages and under all three decoding settings. Nothing about sampling fixes this. For any grounded or retrieval-backed use, the model will not signal when it is outside what it knows, so the surrounding system has to.

**Instruction-following degrades faster than fluency.** Told to answer in exactly five words, no language complied under any setting. Told to reply in one language while the prompt switched to another, it followed the switch. Output that reads well and output that did what it was told are different properties, and only the first improves when you fix the sampler.

## What I would do differently

Score the language comparison properly rather than reading it, so the finding is defensible to someone who does not speak the language — the repetition metric is a start but it measures degeneration, not correctness. Test a second ternary checkpoint so the conclusions are about the approach rather than this model. Measure with batch size above one, since that is the number that decides whether any of this is deployable. And repeat on Apple Silicon: the CPU here is the oldest part of the setup and probably flatters the argument for dedicated hardware.
