# M6 — Model inference: explain and measure one generation

Required milestone: **Explain and measure model inference** — tensor/attention prerequisites, one-token generation, sampling, KV cache, prefill/decode, memory/latency accounting and single-host serving, keeping model execution distinct from the harness tool loop ([roadmap](../../ROADMAP.md#stages-and-milestones)). This page elaborates that row and Track C modules C1–C4 of the [advanced study plan](../../materials/advanced-study.md#ordered-modules-and-lab-checkpoints); it adds no required outcome, depth or scope.

## Useful result

The first half of the [project route](../../ROADMAP.md#project-route) row **"A measured model endpoint"**: trace one-token generation and KV growth, then measure prefill and decode. The learner builds a small, instrumented generation experiment around a compact model implementation, then serves it from one host and measures it through that endpoint. M9 later reuses the same harness for kernel, batching and serving experiments.

**Observable acceptance:** for a fixed prompt, the learner's cached generation produces the same tokens (greedy) or next-token logits within a stated tolerance as an uncached loop. They predict the KV-cache size from the model configuration before measuring it. They report TTFT, inter-token latency, output tokens/second and peak memory with recorded conditions, and explain which loop is the model's token loop and which belongs to the harness.

## Placement and prerequisites

- Entry: Python/tensor/attention readiness. Use the Track C [prerequisite check](../../materials/advanced-study.md#prerequisite-check) — dimensions, broadcasting, matrix multiplication, softmax, parameters versus runtime state, a basic HTTP request. Introduce missing mathematics before any optimization.
- M1 tool-cycle evidence supplies the harness side of the comparison; it is not re-taught here.
- M6 does not wait for M5. The single-host endpoint only needs M2 process/HTTP literacy; deploying it as a supervised service reuses M5 later.
- M9 needs M6 accounting (C3/C4) and M5 service operation. Full C12 load, overload and failure work is in M9/M10; M6 covers only the single-host serving introduction the [materials shelf](../../materials/README.md) assigns to M6.

## Checkpoints

| ID | Mechanism | Observable evidence | Hours |
|---|---|---|---:|
| Bridge | Tensors, shapes, softmax, attention as weighted lookup | Learner predicts and checks shapes through one attention call; explains a broadcasting error they caused | 6–12 |
| C1 | One token end to end: tokenization/template → embeddings → causal attention/MLP/residual/norm → logits → sampling → detokenization; positions/RoPE | Shape trace through a tiny decoder; names the value that chooses the next token | 5–8 |
| C2 | Generation loop: greedy, temperature/top-k/top-p, stop tokens, max output, streaming, inference mode, reproducibility | Learner-written loop with predicted termination; written contrast of this token loop with the harness tool loop | 4–6 |
| C3 | Prefill versus decode; stored keys/values; masks and cache positions; MHA/GQA/MQA | Cached versus uncached logits within tolerance; derived cache size; a deliberate position/mask bug found and explained | 7–10 |
| C4 | Weights, KV, activations/workspace, allocator overhead; dtype; FLOPs, bandwidth, arithmetic intensity | Fit estimate before running; measured TTFT, inter-token latency, tokens/s and peak memory; dominant bottleneck explained | 7–10 |
| Serve | Single-host serving introduction: one streaming endpoint over the same engine | One endpoint run with C4 metrics measured through it, separating cold start, prefill, decode and client/network overhead | 6–9 |

Planning split of the 35–55h [workload](../WORKLOAD.md) row; shared work counts once. Derive the cache formula `2 × layers × batch × tokens × KV_heads × head_dimension × bytes_per_element` and every assumption, as Track C requires.

## Lab sequence

Each increment follows the [session workflow](../../teaching/README.md#prepare-and-teach): the learner predicts or attempts first, and the teacher gives the smallest useful hint. No increment is written for the learner.

| Increment | Deliverable | Acceptance check | Learner's first action | Timebox |
|---|---|---|---|---|
| 1. Shape trace | Annotated trace of one forward pass through a tiny randomly initialized decoder | Every tensor shape matches the learner's prediction, or the mismatch is explained | Write predicted shapes for `CausalSelfAttention.forward` before running | 1–2 sessions |
| 2. Token loop | Own generation loop with greedy and one sampling mode | Greedy output repeats exactly under a fixed seed; termination matches prediction | Predict when the loop stops for a given stop token and max length | 1–2 sessions |
| 3. Cache equivalence | Cached and uncached paths over the same weights | Greedy tokens identical; logits within a stated tolerance | Derive expected cache tensor size from the config | 2–3 sessions |
| 4. Accounting sheet | Memory/latency estimate plus measurement | Measured peak memory and timings are compared with the estimate, and the gap is explained | Estimate weight and KV bytes for two prompt lengths | 2 sessions |
| 5. One endpoint | Streaming endpoint over the engine, with a timing record | TTFT measured at the client versus inside the engine; the difference is attributed | Sketch where request parsing ends and the token loop begins | 2–3 sessions; at most 6–9 project hours as one slice |

## Failure experiments

- Offset the cache position by one, as with the rotary offset `T0` in nanochat `GPT.forward` (lines 251–252), or break the chunk mask; observe divergence from the uncached reference and locate it.
- Reuse a cache across two prompts without reset; explain the output.
- Remove the stop token or set temperature above zero without a seed; predict, then observe termination and reproducibility.
- Time without device synchronization or include first-call warmup; show how the reported latency changes.
- Engine-level tool: nanochat's `Engine.generate` runs a calculator inside the token loop by forcing tokens (engine.py lines 281–297). Explain why this differs from M1, where the harness executes a tool between model requests.

## Hardware notes

A laptop CPU or Metal backend is enough for increments 1–4 with a tiny randomly initialized configuration: shapes, cache equivalence and timing structure need no trained weights. Meaningful text and representative timings need trained weights and one modest local backend that fits memory. Choose llama.cpp **or** MLX LM, not both. nanochat's inline engine test (engine.py lines 330–384) loads a trained checkpoint and calls `torch.cuda.synchronize()`, so it does not run unchanged without CUDA; the learner writes their own fixture. Record backend, dtype and device with every measurement. Local results do not establish GPU or vLLM behavior. No host, model download, rental or budget is chosen here.

## Materials

| Source | Role | Checkpoint |
|---|---|---|
| [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html), selected [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) | Tensor and model vocabulary for gaps found at entry | Bridge, C1 |
| [nanochat `gpt.py`](../../materials/sources/inference/nanochat/nanochat/gpt.py): `CausalSelfAttention.forward` (66–109), `Block.forward` (131–134), `GPT.forward` (243–274), uncached `GPT.generate` (276–305), `estimate_flops` (204–210) | Compact decoder to trace, plus an uncached reference loop | C1, C2, C3, C4 |
| [nanochat `engine.py`](../../materials/sources/inference/nanochat/nanochat/engine.py): `KVCache` (83–160, `insert_kv` 135–160), `sample_next_token` (164–181), `Engine.generate` (199–303: prefill 216–228, decode loop 243–303) | Cache growth, prefill/decode split, sampling and the in-engine tool | C2, C3 |
| [nanochat `tests/test_engine.py`](../../materials/sources/inference/nanochat/tests/test_engine.py) | Example of testing cache resizing without a trained model | C3 |
| [nanochat `scripts/chat_web.py`](../../materials/sources/inference/nanochat/scripts/chat_web.py): `WorkerPool` (98–147), `generate_stream` (262–311), `/chat/completions` (313–382), `/health` (384–393) | Single-host streaming server with one request per worker; M9 contrasts it with continuous batching | Serve |
| [Hugging Face cache explanation](https://huggingface.co/docs/transformers/en/cache_explanation) | First C3 reading after shapes make sense | C3 |
| [Stanford CS336](https://cs336.stanford.edu/) resource-accounting and inference lectures | Deeper instruction, selected by topic | C4 |
| llama.cpp or MLX LM (pinned, not checked out: `materials/sources/inference/llama.cpp` at `8ca4060b7e30`, `materials/sources/inference/mlx-lm` at `f39c4aa2af5d`; fetch with `git submodule update --init --checkout materials/sources/inference/llama.cpp`) | The one local backend for real weights | C4, Serve |

nanochat is pinned at `d5759400f967`. Select inference paths only; the training scripts are out of scope. Recheck line ranges if the pin changes.

## Assessment

Use the [shared rubric](../ASSESSMENT.md). The learner demonstrates cache equivalence and the accounting sheet, explains one generation end to end, and handles an unseen variation, such as a GQA head ratio, a new stop condition or a changed dtype, with a prediction before execution. Copied formulas without stated assumptions, or timings without conditions, are revision triggers. Reuse M1 evidence for the harness side of the comparison.

**Estimated hours:** 35–55 directed hours ([workload forecast](../WORKLOAD.md)), including reading, attempts, feedback and assessment.
