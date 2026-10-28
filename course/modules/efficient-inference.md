# M9 — Efficient and distributed inference: measure before you optimize

Required milestone: **Analyze efficient and distributed inference** — kernels, batching, KV allocation, vLLM source, quantization, speculative decoding, parallelism and interconnect costs. Use controlled benchmarks and distinguish simulated multi-device reasoning from hardware measurements ([roadmap](../../ROADMAP.md#stages-and-milestones)). This page elaborates that row and Track C modules C5–C11 of the [advanced study plan](../../materials/advanced-study.md#ordered-modules-and-lab-checkpoints); it adds no required outcome, depth or scope.

## Useful result

The second half of the [project route](../../ROADMAP.md#project-route) row **"A measured model endpoint"**: compare bounded serving and optimization experiments, and label simulated parallelism. The learner extends the M6 timing harness into a controlled benchmark workload, traces one request through a serving engine, then changes one variable at a time.

**Observable acceptance:** for each optimization studied, a benchmark record shows the baseline and one changed condition under an unchanged workload. The record covers revisions, hardware, dtype, prompt/output lengths, concurrency, cache state and warmup, along with errors, memory, TTFT, inter-token latency and throughput, and a quality check where output can change. The learner traces one vLLM request from API server to streamed token at a pinned revision. Every multi-device result is labeled *measured* or *simulated/analyzed*.

## Placement and prerequisites

- Entry: M6 inference accounting (C3 cache equivalence, C4 measurement) and M5 service operation. Hardware-specific labs need a suitable authorized host.
- C5–C7 and C10/C11 reasoning can start on a laptop. Serving labs (C8) and kernel, quantized-kernel and multi-device measurements wait for host suitability.
- C12 reliable serving is shared with M6 and M10. M9's controlled benchmarks feed it, and the C12 load and failure/recovery exercise is defended with the M10 capstone. C13 backend comparisons stay optional specialization.

## Checkpoints

| ID | Mechanism | Observable evidence | Hours |
|---|---|---|---:|
| C5 | GPU memory hierarchy, tiling, fusion, attention kernels, FlashAttention, compilation, CUDA graphs | Baseline versus optimized attention, correctness checked first; synchronized timing; warmup/compile separated from steady state | 6–10 |
| C6 | Request queues; static, dynamic and continuous batching; token budgets; chunked prefill; fairness; backpressure; cancellation | Learner's scheduling simulation shows a short request waiting behind a long prompt; a policy change explained | 5–8 |
| C7 | Block allocation, PagedAttention, fragmentation, prefix reuse, eviction, offload | Learner's block-table simulation reclaims finished requests; per-sequence KV reuse, shared-prefix caching and application response caching distinguished | 5–8 |
| C8 | vLLM request path: API server → processing → engine/scheduler → KV allocation → model runner → sampled token → streaming | Single-request trace at a pinned revision; a small model served on a verified supported host; state ownership at each stage explained | 8–12 |
| C9 | Weight-only versus activation/KV quantization; scales, outliers, calibration, supported kernels, quality | One supported quantized configuration against a baseline on the same prompts; memory, latency and quality reported together | 5–8 |
| C10 | Draft proposals, target verification, acceptance/rejection, overhead | Toy verification trace, then one supported implementation measured; explains when a draft fails to speed things up | 4–7 |
| C11 | Data/tensor/pipeline/expert parallelism, collectives and interconnects, MoE routing, long context, prefill/decode separation | Communication and memory-ownership diagram; a justified partition; simulator or design analysis, labeled, if multiple devices are unavailable | 7–12 |

Planning split of the 40–65h [workload](../WORKLOAD.md) row; overlapping benchmark setup counts once.

## Lab sequence

Each increment follows the [session workflow](../../teaching/README.md#prepare-and-teach). Simulations and analyses are learner-authored. Teachers supply questions, source passages and hints, not implementations. A practical slice is at most 6–9 project hours.

| Increment | Deliverable | Acceptance check | Learner's first action | Timebox |
|---|---|---|---|---|
| 1. Benchmark record | M6 harness extended with the Track C condition fields | Two repeated runs agree within the stated variance; warmup reported separately | List what could change between two "identical" runs | 1–2 sessions |
| 2. Attention comparison | Naive versus optimized attention on the same inputs | Outputs agree within tolerance before any timing; timings synchronized | Predict which is faster at short and long sequence lengths | 2 sessions |
| 3. Scheduler simulation | Queue simulation with one switchable batching policy | Head-of-line wait reproduced and reduced by the policy change | Draw the request timeline for one long and one short prompt | 2–3 sessions |
| 4. Block-table simulation | Block allocator with free, reclaim and prefix sharing | Reclaimed blocks are reused; a shared prefix is counted once; exhaustion triggers the predicted behavior | Compute blocks needed for three requests at a given block size | 2–3 sessions |
| 5. Engine trace | Annotated request path in nano-vllm, then vLLM at a pinned revision | Each stage names the code location and the state it owns; differences between the two engines noted | Predict where a request waits before its first token | 2–3 sessions |
| 6. One optimization measured | Quantization **or** speculative decoding against a baseline | Same workload; speed, memory and quality reported together; result explained, even if slower | State the expected effect and what would falsify it | 2–3 sessions |
| 7. Partition analysis | Parallelism plan for a named model and device count | Per-device memory and per-step communication derived; labeled as analysis unless measured | Estimate whether the weights fit on one device | 2 sessions |

## Failure experiments

- Time GPU work without synchronization, or include compile and graph capture; show the misleading number.
- Change two variables at once, such as batch size and cache state; show why the result cannot be attributed.
- Critique nano-vllm's [`bench.py`](../../materials/sources/inference/nano-vllm/bench.py): random prompt tokens, `ignore_eos=True`, and throughput computed from requested `max_tokens` over wall time with no TTFT, tail latency or quality. State what it does and does not establish.
- Exhaust KV blocks in the simulation and in nano-vllm's scheduler logic (`Scheduler.schedule`/`preempt`). Explain preemption and the recomputation it causes.
- Report a quantized speedup with degraded output; a low-acceptance draft model that slows decoding; a simulated tensor-parallel speedup presented as measured. Identify each as an invalid claim.

## Hardware notes

A laptop is enough for the simulations, the attention correctness checks, source traces, the toy speculative trace and partition analysis. llama.cpp or MLX LM can run quantized local models, but Mac results do not establish GPU-kernel, CUDA or vLLM behavior. nano-vllm imports Triton and `flash_attn` and initializes NCCL in `ModelRunner.__init__` (line 26), so it executes only on a supported CUDA host; its scheduler and block manager are plain Python and can be read anywhere. FlashAttention kernels, CUDA graphs, vLLM serving, quantized GPU kernels and any multi-device measurement need a suitable authorized host, checked against the pinned release's installation requirements. No host, rental or budget is chosen here.

## Materials

| Source | Role | Checkpoint |
|---|---|---|
| [Stanford CS336](https://cs336.stanford.edu/): GPUs, kernels/Triton, parallelism and inference lectures | Deeper instruction, selected by topic | C5, C11 |
| [FlashAttention paper](https://arxiv.org/abs/2205.14135); implementation pinned at `materials/sources/inference/flash-attention` (`98c1cee0ed59`, not checked out) | Attention IO and kernels; algorithm versus hardware-specific code | C5 |
| [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) | Optional kernel depth; validate correctness before timing | C5 |
| [PagedAttention paper](https://arxiv.org/abs/2309.06180) | Memory-management model; current details come from vLLM source | C7 |
| nano-vllm (pinned `bb823b3e0698`): [`scheduler.py`](../../materials/sources/inference/nano-vllm/nanovllm/engine/scheduler.py) `schedule` 25–73, `preempt` 75–79, `postprocess` 81–92; [`block_manager.py`](../../materials/sources/inference/nano-vllm/nanovllm/engine/block_manager.py) `can_allocate` 58–73, `allocate` 75–92, `deallocate` 94–101, `hash_blocks` 110–120 | Readable continuous batching, chunked prefill, preemption and hashed prefix reuse | C6, C7 |
| nano-vllm [`model_runner.py`](../../materials/sources/inference/nano-vllm/nanovllm/engine/model_runner.py) `allocate_kv_cache` 103–121, `run_model` 196–212, `capture_cudagraph` 222–257; [`llm_engine.py`](../../materials/sources/inference/nano-vllm/nanovllm/engine/llm_engine.py) `step` 49–55; [`layers/attention.py`](../../materials/sources/inference/nano-vllm/nanovllm/layers/attention.py); [`layers/linear.py`](../../materials/sources/inference/nano-vllm/nanovllm/layers/linear.py) `RowParallelLinear` 131–156 | KV sizing from free memory, CUDA-graph replay, engine step and tensor-parallel all-reduce | C5, C7, C8, C11 |
| vLLM pinned at `materials/sources/inference/vllm` (`06e172b5cf88`, not checked out) with matching [documentation](https://docs.vllm.ai/en/latest/): [benchmarking](https://docs.vllm.ai/en/latest/benchmarking/), [prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/), [quantization](https://docs.vllm.ai/en/latest/features/quantization/), [parallelism](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) | Main production trace and operation guide; pair the checkout with matching docs | C6–C11 |
| llama.cpp (`8ca4060b7e30`) or MLX LM (`f39c4aa2af5d`), not checked out | The one local lane for quantized formats; choose one | C9 |
| SGLang (`610a74d64855`, not checked out) | Later comparison once the vLLM path and method are understood | C13 (optional) |
| M6 artifacts: [nanochat `engine.py`](../../materials/sources/inference/nanochat/nanochat/engine.py) and [`scripts/chat_web.py`](../../materials/sources/inference/nanochat/scripts/chat_web.py) | Baseline of one request per worker without continuous batching | C6, C8 |

Fetch a pinned checkout only when its lesson is active, for example `git submodule update --init --checkout materials/sources/inference/vllm`. Use the same form for `flash-attention`, `llama.cpp`, `mlx-lm` and `sglang`. Recheck nano-vllm line ranges if its pin changes.

## Assessment

Use the [shared rubric](../ASSESSMENT.md), including its advanced-work requirement for a bounded research comparison or reproduction. Require learner-authored simulations, a pinned source trace, controlled benchmark records with limits, and correct labeling of simulation versus measurement. In an unseen variation, such as a new block size, arrival pattern, acceptance rate or device count, the learner predicts and then checks the result. A failed reproduction with a sound method is acceptable. A speedup without conditions or a quality check is not.

**Estimated hours:** 40–65 directed hours ([workload forecast](../WORKLOAD.md)).
