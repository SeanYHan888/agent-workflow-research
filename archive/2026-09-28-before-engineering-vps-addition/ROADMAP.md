# Distributed AI Agent Systems — roadmap

Curriculum v1 adopted September 28, 2026. This map is adaptable under the [course charter](course/CHARTER.md); stable milestone IDs preserve links and learning credit across revisions. The [decision record](teaching/DECISIONS.md) explains changes. The earlier 160-hour foundation forecast is [archived](archive/2026-09-28-before-program-structure/ROADMAP.md), not the enlarged program's duration.

## Start and schedule

Use the [live Obsidian course overview](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Notes/Coding Agent Course/00 Start Here.md>) for project status and dates. September 28 inspection found the original tool-cycle section complete and JS/Node active. Verify the current owning note before assigning work; calendar dates do not establish learning.

Next core session: inspect the student's latest JS/Node evidence, choose the next unmet language/process checkpoint, and prepare a short attempt-first lesson. Do not restart completed Variables or the tool cycle by default. The [VPS idea](course/ideas/I001-vps.md) is a candidate for the normal exploration allowance, not a replacement primary module.

Budget and active-work limits are owned by the charter: 15 hours/week, normally 10 core/labs, 3 project and 2 exploration. New project options have no dates until activated. The existing Obsidian forecasts remain unchanged pending a concrete reforecast; JS/Node's recorded end overlaps the TS start and added scope needs estimation. No revised overall finish date has been promised.

## Stages and milestones

Each row is a learning destination, not one execution project. Larger milestones contain several independently finishable projects. Use [project mappings](course/PROJECTS.md), [materials](materials/README.md) and the [assessment rubric](course/ASSESSMENT.md).

| Stage | Milestone | Boundary and demonstration |
|---|---|---|
| I. Foundations | M1. Explain and implement an agent tool cycle | Model output versus harness execution; messages, validation, stop conditions and failures. Preserve the existing Section 1 evidence rather than assigning it again. |
| I. Foundations | M2. Write and control a program | JS/TS, Node, async, errors, files, subprocesses and basic Bash/process/network literacy. Build and explain a bounded task runner. |
| I. Foundations | M3. Build a small typed agent | Provider/tool contracts, runtime validation, context, persistence, cancellation and tests. Extend the runner rather than starting several independent agents. |
| II. Reliable single-host systems | M4. Explain real harnesses and integration boundaries | Selected mini-swe-agent/Pi source, Pi extension and real-worker adapter; terminal and GUI session ownership. Retain required Codex source study with a scoped Rust reading bridge, sequenced after the smaller source traces. |
| II. Reliable single-host systems | M5. Operate an isolated service on Linux | OS processes/threads, virtual memory, files/I/O, permissions and scheduling; Linux services/logs, SSH, DNS/TCP/HTTP/TLS, routing/firewalls, VPS recovery, Docker images/volumes/networks and resource isolation. Diagnose failures before adding orchestration. |
| II. Reliable single-host systems | M6. Explain and measure model inference | Tensor/attention prerequisites, one-token generation, sampling, KV cache, prefill/decode, memory/latency accounting and single-host serving. Keep model execution distinct from the harness tool loop. |
| III. Distributed systems | M7. Coordinate durable distributed work | State ownership, queues, concurrency, idempotency, retry/backoff, leases, uncertain outcomes, consistency and recovery under partial failure. Reuse worker adapters and demonstrate worker loss and duplicate delivery. |
| III. Distributed systems | M8. Operate services with Kubernetes | Workload lifecycle, scheduling/resources, service discovery, networking, configuration/secrets, persistent state, rollout and recovery. Compare behavior with the understood single-host deployment. |
| III. Distributed systems | M9. Analyze efficient and distributed inference | Kernels, batching, KV allocation, vLLM source, quantization, speculative decoding, parallelism and interconnect costs. Use controlled benchmarks and distinguish simulated multi-device reasoning from hardware measurements. |
| IV. Integrated capstone | M10. Build and defend a distributed agent system | Join durable job coordination, isolated workers and a model-serving boundary. Demonstrate evaluation, observability, cancellation, overload and failure recovery; defend architecture and report correctness, latency, resource use and human intervention. |

M1's historical evidence remains credited for the demonstrated capability. New criteria introduced by future revisions become explicit gaps rather than erasing old completion.

## Dependencies and flexibility

| Milestone | Entry requirements |
|---|---|
| M1 | Small-script orientation as needed |
| M2 | Tool-cycle orientation; language/process diagnostics determine the next lesson |
| M3 | Relevant M2 language, async, file and process checkpoints |
| M4 | M3; deeper Codex tracing also needs its scoped Rust reading bridge |
| M5 | M2 shell/process foundations; deploying the learned agent uses M3/M4 contracts |
| M6 | Python/tensor/attention readiness; introduce missing mathematics before optimizations |
| M7 | M4 worker boundary and M5 single-host operation/recovery |
| M8 | M5 containers/networks/services and M7 coordination/failure reasoning |
| M9 | M6 inference accounting and M5 service operation; hardware-specific labs need a suitable authorized host |
| M10 | M7 durable work, M8 deployment and M9 serving/evaluation evidence |

Stage II modules need dedicated time, but an unrelated source-reading requirement does not block an otherwise ready Linux lesson. Preparatory exploration can precede a full milestone without granting its completion. Keep one primary module; reorder eligible lessons under the charter instead of running every subject simultaneously.

## Subject boundaries

| Subject | Core scope | Optional depth |
|---|---|---|
| Programming and agents | JS/TS/Node, targeted Python/Rust, tools/context/state, concurrency, source tracing, evaluation and bounded extensions | Full UI-framework study, rebuilding a complete commercial harness |
| OS and Linux | Processes/threads, scheduling, virtual memory, files/I/O, users/permissions, signals, services, resource isolation and diagnosis | Writing a kernel or device driver |
| Networks and VPS | DNS, TCP/IP, HTTP/TLS, SSH, addressing/routing, ports/firewalls, service reachability, remote state and recovery | Implementing an entire protocol stack |
| Containers and Kubernetes | Images, volumes, namespaces/cgroups, container networking, declarative workloads, scheduling/discovery, configuration/secrets and recovery | Custom operators and cluster internals without a relevant project question |
| Inference and serving | C1–C12 coverage from [advanced materials](materials/advanced-study.md): generation/cache, memory, kernels, batching, vLLM, quantization/speculation, parallelism and reliable serving | C13 backend/architecture specializations and model pretraining |
| Distributed agent systems | State ownership, queues, retries/idempotency, consistency/leases, backpressure, partial failure, observability, security and measured orchestration | Building a general-purpose orchestration framework before evaluating existing tools |

Terminal collaboration, GUI/client ownership and a team with final human review remain required outcomes. A specific product is a candidate implementation, not a permanent curriculum boundary. Official Claude courses are assigned materials for agent mechanisms; the source route retains mini-swe-agent → Pi → Codex, with supporting comparisons.

## Assessment and capstone

Every milestone uses the shared artifact/experiment, explanation and unfamiliar-change standard. Advanced work includes bounded research comparison or reproduction. The capstone joins durable coordination, isolated workers and model serving, with real multi-host execution and measured failure/recovery. Multi-device inference simulation must be labeled; it does not count as a measured hardware speedup.

## Changes

New ideas enter [IDEAS.md](course/IDEAS.md). Equivalent exercises can change routinely while preserving outcomes. Required milestone/core/deadline changes use the charter's impact review and student agreement, then update this map, project/material links and approved schedule together. Existing evidence is mapped forward, and retired IDs remain discoverable.
