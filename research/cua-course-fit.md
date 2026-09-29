# Cua: course fit and a bounded exploration

Research date: September 28, 2026. Disposition: **good optional applied-lab candidate**, especially for M4, M5 and later M7/M10. It does not add a required milestone or change the schedule. This is a source review and proposed experiment, not an installation, benchmark result or completed learner assessment.

## Recommendation

Cua makes the boundary between an agent's decision and a computer's actual behavior unusually tangible. It can teach observation/action contracts, process and session ownership, isolated environments, uncertain outcomes, and independent acceptance checks. Those are already course outcomes. Begin with a two-hour source exploration; consider a pilot of at most six hours only after readiness and environment checks. Keep the [charter](../course/CHARTER.md)'s 15-hour budget and one active project.

It is **computer-use infrastructure**: software that lets an agent inspect and operate another application's interface. That differs from a **GUI client for working with coding agents**, whose interface lets the human manage conversations, review changes and supervise sessions. Cua may supply tools to such a client or run inside its workers; it does not by itself establish the course's human review, durable work coordination or team ownership design. This distinction follows the Driver's published integration contracts. [Driver architecture](https://github.com/trycua/cua/blob/main/libs/cua-driver/README.md)

## Components and boundaries

| Component | Responsibility and learning use |
|---|---|
| Cua Driver | Native desktop/browser observation and actions through CLI/MCP or typed application SDKs. Its Rust runtime underlies generated Python/TypeScript bindings; an application can embed it without a separate daemon. MCP remains an executable-level agent boundary. Study tool contracts and authority in M4. |
| Lume | Apple Silicon VM lifecycle for local macOS/Linux guests. A useful M5 virtualization comparison, subject to actual host capacity. |
| Sandbox SDK and Fleets | Sandbox interfaces address one computer; managed pools provide capacity and claims reserve it. Guest services, credentials, readiness and lifecycle remain distinct. Useful later for M7 ownership/recovery. |
| Cua-Bench | Task setup, variations, agent adapters, runners and final-state evaluators. Useful for acceptance and reproducible experiments in M11/M10. |
| `cua-agent` | A separately packaged agent/model integration layer; API-only and local-model extras have different dependencies. Optional comparison material, not the student's required harness implementation. |

Sources: [Driver source architecture](https://github.com/trycua/cua/blob/main/libs/cua-driver/README.md), [Lume requirements](https://cua.ai/docs/how-to-guides/lume/install-lume), [Fleet tutorial](https://cua.ai/docs/tutorials/your-first-cloud-fleet), [Cua-Bench concepts](https://cua.ai/docs/concepts/what-is-cua-bench), [agent package manifest](https://github.com/trycua/cua/blob/1cb7b6fb2415b6d12978d2dfa3ecda0b07075c72/libs/python/agent/pyproject.toml).

The repository also advertises CUA-S1 research models. That is optional model specialization material; including Cua in a lab does not make training those models or studying every component required. [Repository overview](https://github.com/trycua/cua)

## Runtime feasibility: choose a path, not a product label

- **Lowest-infrastructure experiment:** the official simulated Cua-Bench tutorial needs Python 3.12/3.13, `uv`, and Playwright Chromium, but no Docker daemon, VM or model API key for its reference-solution run. This is a browser-rendered simulation, not proof of native macOS automation. [Tutorial](https://cua.ai/docs/tutorials/your-first-cua-bench-task)
- **Existing desktop Driver:** requires a supported interactive desktop and platform permissions. macOS needs Accessibility and Screen Recording; Linux behavior differs across X11, Wayland compositors and toolkits. A successful tool return is not necessarily successful application behavior. A generic headless VPS shell is not an interactive desktop. [Platform support](https://cua.ai/docs/reference/cua-driver/platform-support)
- **Local Lume:** documented requirements are Apple Silicon, macOS 13+, at least 8 GB RAM (16 GB recommended) and 50 GB free disk. These are product prerequisites, not confirmation that the student's Mac currently has enough spare capacity. [Installation requirements](https://cua.ai/docs/how-to-guides/lume/install-lume)
- **Linux Sandbox:** the documented default Linux VM uses `qemu-system-x86_64`; the container path selects Docker. The local/Fleet image matrix differs, and accepting an image does not prove it boots. Local and pool-backed Fleet snapshots are documented as unimplemented, so plan fixture recreation rather than assuming universal snapshot rollback. [Runtime support](https://cua.ai/docs/reference/sandbox-sdk/runtime-support)
- **A Linux VPS:** suitability remains unverified. Check host/guest architecture, guest image availability, RAM/disk, desktop dependencies, nested virtualization and accessible acceleration before selecting it. In particular, do not infer that an Oracle ARM host can efficiently run the default x86 VM because both have “Linux” labels. Cua's compatibility helper uses a coarse `/dev/kvm` existence probe; its x86 helper's Linux branch is not a complete architecture qualification. The QEMU implementation also explicitly falls back to software emulation for x86 guests on Apple Silicon. Inspect the actual selected path and prove a boot. [Compatibility code](https://github.com/trycua/cua/blob/1cb7b6fb2415b6d12978d2dfa3ecda0b07075c72/libs/python/cua-sandbox/cua_sandbox/runtime/compat.py), [QEMU implementation](https://github.com/trycua/cua/blob/1cb7b6fb2415b6d12978d2dfa3ecda0b07075c72/libs/python/cua-sandbox/cua_sandbox/runtime/qemu.py)

This review does not establish a self-hosted replacement for Cua's managed Fleet control plane on a small VPS. Treat local runtime support and managed Fleet availability as separate questions.

## Dependencies, costs and license boundaries

The inspected `cua-sandbox` 0.8.0 manifest requires Python `>=3.11,<3.14`, pins `cua-fleet==0.1.17`, uses a Cua wheel index, and includes HTTP/WebSocket, SSH, VNC and schema dependencies. Its optional Driver extra pins `cua-driver==0.27.0`. Resolve a coherent version set for a pilot; do not combine latest snippets indiscriminately. [Pinned manifest](https://github.com/trycua/cua/blob/1cb7b6fb2415b6d12978d2dfa3ecda0b07075c72/libs/python/cua-sandbox/pyproject.toml)

The published Driver Python manifest inspected through the web describes a native wheel with no declared Python runtime dependencies, but that does not remove native/platform requirements. Cua-Bench's manifest has substantially more dependencies, including Cua agent/computer packages, Docker's Python client and Playwright; “no Docker required for the simulated tutorial” is not “no Docker-related package installed.” [Driver manifest](https://github.com/trycua/cua/blob/main/libs/cua-driver/python/pyproject.toml), [Bench manifest](https://github.com/trycua/cua/blob/main/libs/cua-bench/pyproject.toml)

The inspected `cua-agent` manifest uses LiteLLM and has optional provider/local-model extras; local Hugging Face/MLX variants bring additional model-serving dependencies. Open-source tooling does not provide free hosted inference. Budget model-provider use separately from local compute or hosted capacity; no provider pricing or account entitlement was verified here. [Agent manifest](https://github.com/trycua/cua/blob/1cb7b6fb2415b6d12978d2dfa3ecda0b07075c72/libs/python/agent/pyproject.toml)

Fleet requires its own credentials. A one-replica pool may remain chargeable after releasing a claim; deletion must be confirmed. Exact rates were not established, and this note does not authorize spending or provisioning. [Fleet lifecycle and billing warning](https://cua.ai/docs/tutorials/your-first-cloud-fleet)

The repository's main license is MIT, but optional `cua-som`, perception extensions and model artifacts have separate terms. The current overview identifies AGPL components and explicitly distinguishes model/dataset licenses. Choose the minimal pilot components and inspect their exact resolved licenses before distributing or hosting them. [License boundaries](https://github.com/trycua/cua#license)

## Source-level evidence and assessment implications

The pinned Cua-Bench starter task has separate setup, solve and evaluate functions. Its reference solution clicks a CSS selector; its evaluator checks `window.__clicked`. That is a useful demonstration of independent final-state inspection, but passing that fixture only proves that small objective. It does not establish visual reasoning, general desktop competence or resistance to an agent modifying the evaluator's state directly. In an assessment, constrain action access and keep evaluator authority outside the tested agent. [Starter implementation](https://github.com/trycua/cua/blob/1cb7b6fb2415b6d12978d2dfa3ecda0b07075c72/libs/cua-bench/cua_bench/templates/starter_env/main.py)

Cua-Bench separates tasks, environments, agents and runners, and supports variations and traces. This supplies experiment machinery, not an automatically meaningful score: task difficulty, reset quality, agent access and success conditions still determine what was measured. No benchmark rankings or success rates were reproduced during this review. [Benchmark design](https://cua.ai/docs/concepts/what-is-cua-bench)

## Placement and prerequisites

| Course location | Proposed use | Boundary |
|---|---|---|
| M4 | Trace one observation → action → verification path; distinguish model, harness, Driver and environment. | Adds a comparison/example, not another complete codebase-reading obligation. |
| M5 | Operate one isolated desktop fixture and explain resources, permissions, processes and cleanup. | Start only after shell/process/network and environment readiness checks. |
| M7 | Later reuse the worker boundary to study lost connections, leases, duplicate actions and retries. | A pool claim is not proof of exactly-once execution or durable business outcomes. |
| M8 | Optional deployment comparison if runtime constraints fit an understood cluster. | Do not add Kubernetes simply because Cua exists. |
| M10 / M11 | Evaluate an unfamiliar task variation and submit a reviewable result with evidence. | One successful GUI demo does not satisfy the distributed capstone. |

Practical entry requirements: async Python/TypeScript literacy, tool-cycle understanding, basic process/network diagnosis, a clearly isolated fixture, and the ability to state acceptance before running an agent. Check the owning Obsidian note before assigning or scheduling; this research does not claim learner readiness.

## Proposed exploration and pilot

**Two-hour exploration, from the existing exploration allowance:** draw the component boundary; read the starter task and runtime selection; explain why a tool return, screenshot, evaluator result and real-world success are different evidence. End with a one-page choice between simulation, an authorized isolated desktop, or deferral. No installation is needed for this source exercise.

**Optional pilot, at most six hours over two project weeks:** activate only when prerequisites and the environment are ready, using the existing three-hour project allocation. Include setup in the limit; stop and report the blocker if setup consumes the budget. This is a proposed learner task, not work for the teacher to complete on the student's behalf.

Use one harmless fixture, such as entering a fixed value in a local demo form and saving it to a temporary file. Require:

1. A written success condition, exact versions/environment and a known clean starting state.
2. A screenshot/action trace with timestamps, plus an independent check of the saved value or fixture state; an agent's final message is insufficient.
3. A clean reset and repeat run. Recreate fixture data/environment where snapshots are unavailable.
4. Cancellation during the attempt, followed by evidence that no further actions continue and the fixture remains inspectable.
5. One injected transient failure and bounded retry after checking the current state; avoid blindly repeating an action that may already have completed.
6. A small unfamiliar variation, short explanation of the failure boundary, and review of differences between predicted and observed behavior.

Record latency, action count, retries, observed success/failure and any model cost. Make no broad reliability claim from this small sample. Native desktop execution can be a later substitution for the simulated fixture if it earns the setup time.

## Evidence scope and refresh

The public repository API returned commit `1cb7b6fb2415b6d12978d2dfa3ecda0b07075c72` (commit timestamp September 28, 2026). Runtime implementation, Sandbox/Agent manifests, Bench starter and a small Bench test file were read at that pin. Other links above are live official docs or `main` documents accessed on the research date; they are not an immutable release snapshot. Some official examples still pin Sandbox 0.7.0 while the source manifest is 0.8.0, reinforcing the need to select and record exact pilot versions.

No packages were installed, model requests made, resources provisioned, native GUI tests run or student work completed. Source inspection establishes a plausible educational fit. Actual portability, performance, cost and operational reliability remain experiment questions.
