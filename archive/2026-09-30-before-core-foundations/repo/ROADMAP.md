# Distributed AI Agent Systems — roadmap

Curriculum v1.4 updated September 30, 2026: required M12 adds Rust/compiler construction; M5 deepens OS, networks and security; M7 adds local storage foundations. See the [systems module](course/modules/systems-foundations.md) for assessed mechanisms and bounded labs. Python extensions and embedded systems are electives. The September 28 v1.3 selections remain: selected MIT 6.5840 and Stanford CS329Z materials now strengthen the existing distributed-systems and agent-engineering milestones. RabbitMQ/Kafka remain required in M7; engineering practice remains M11. All milestone IDs stay stable. This map is adaptable under the [course charter](course/CHARTER.md); stable milestone IDs preserve links and learning credit across revisions. The [decision record](teaching/DECISIONS.md) explains changes. The earlier 160-hour foundation forecast is [archived](archive/2026-09-28-before-program-structure/ROADMAP.md), not the enlarged program's duration.

## Start and schedule

Use the [live Obsidian course overview](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Notes/Coding Agent Course/00 Start Here.md>) for project status and dates. September 28 inspection found the original tool-cycle section complete and JS/Node active. Verify the current owning note before assigning work; calendar dates do not establish learning.

Next core session: inspect the student's latest JS/Node evidence, choose the next unmet language/process checkpoint, and prepare a short attempt-first lesson. Do not restart completed Variables or the tool cycle by default. Introduce M11 E1/E2 Git inspection and recovery as a short foundation lesson within the current core allocation before substantial agent edits; it displaces equal core-study time. The old [VPS idea](course/ideas/I001-vps.md) is stopped pending the student's replacement-host direction; retained [VPS material](course/projects/vps-lab-roadmap.md) is reference, not an active assignment.

Budget and active-work limits are owned by the charter: 15 hours/week, normally 10 core/labs, 3 project and 2 exploration. New project options have no dates until activated. The [workload forecast](course/WORKLOAD.md) estimates remaining scope and counts overlap once. The student confirmed a conference break October 5–11 and return October 12. The [restart calendar proposal](teaching/2026-09-28-SCHEDULE-REVIEW.md) repairs the old JS/Node–TS overlap; its broader date changes await agreement. No overall finish date has been promised.

## Stages and milestones

Each row is a learning destination, not one execution project. Larger milestones contain several independently finishable projects. Use [project mappings](course/PROJECTS.md), [materials](materials/README.md) and the [assessment rubric](course/ASSESSMENT.md).

| Stage | Milestone | Boundary and demonstration |
|---|---|---|
| I. Foundations | M1. Explain and implement an agent tool cycle | Model output versus harness execution; messages, validation, stop conditions and failures. Preserve the existing Section 1 evidence rather than assigning it again. |
| I. Foundations | M2. Write and control a program | JS/TS, Node, async, errors, files, subprocesses and basic Bash/process/network literacy. Build and explain a bounded task runner. |
| I. Foundations; reinforced throughout | M11. Deliver and recover an engineering change | Git/GitHub, issues/specs, focused commits, PRs/CI, review, ADRs, TDD, recovery and deliverable acceptance. [E1/E2](course/modules/engineering-practice.md) begin with M2; the full delivery exercise follows through M3/M4. |
| I. Foundations | M3. Build a small typed agent | Provider/tool contracts, runtime validation, context, persistence, cancellation and tests. Extend the runner rather than starting several independent agents. Use selected CS329Z component/baseline lessons from the [university integration map](materials/university-course-integration.md). |
| II. Reliable single-host systems | M4. Explain real harnesses and integration boundaries | Selected mini-swe-agent/Pi source, Pi extension and real-worker adapter; terminal and GUI session ownership. Retain required Codex source study after smaller traces and M12 R1 Rust readiness; compiler completion is not a prerequisite to initial harness reading. CS329Z design material supports harness/memory/framework comparisons without replacing source traces. |
| I–II. Language and systems foundations | M12. Build and explain a small compiler | [R1/K1–K5](course/modules/systems-foundations.md): Rust ownership/types, lexing/parsing, scope/type checking, AST evaluator, bytecode compiler/VM, bounded optimization/native pipeline and a rustc mechanism trace. Learner-authored artifacts plus unfamiliar-change defense. |
| II. Reliable single-host systems | M5. Operate an isolated service on Linux | OS processes/threads, virtual memory, files/I/O, permissions and scheduling; Linux services/logs, SSH, DNS/TCP/HTTP/TLS, routing/firewalls, VPS recovery, Docker images/volumes/networks and resource isolation. Require the [F0/O1–O3/N1–N3/S1](course/modules/systems-foundations.md) machine, OS, socket/framing, packet/failure and access-boundary evidence before orchestration. |
| II. Reliable single-host systems | M6. Explain and measure model inference | Tensor/attention prerequisites, one-token generation, sampling, KV cache, prefill/decode, memory/latency accounting and single-host serving. Keep model execution distinct from the harness tool loop. |
| III. Distributed systems | M7. Coordinate durable distributed work | [D1–D3 storage foundations](course/modules/systems-foundations.md): indexes, durable logs, crash recovery and transaction/concurrency reasoning; then state ownership, queues, concurrency, idempotency, retry/backoff, leases, uncertain outcomes, consistency and recovery under partial failure. Required [message-broker study](course/modules/message-brokers.md): RabbitMQ job queues and Kafka retained event streams, with acknowledgements/offsets, replay, ordering and failure experiments. Use the selected MIT 6.5840 replication/consistency/ownership route and CS329Z single/multi-agent comparison. Reuse worker adapters and demonstrate worker loss and duplicate delivery. |
| III. Distributed systems | M8. Operate services with Kubernetes | Workload lifecycle, scheduling/resources, service discovery, networking, configuration/secrets, persistent state, rollout and recovery. Compare behavior with the understood single-host deployment. |
| III. Distributed systems | M9. Analyze efficient and distributed inference | Kernels, batching, KV allocation, vLLM source, quantization, speculative decoding, parallelism and interconnect costs. Use controlled benchmarks and distinguish simulated multi-device reasoning from hardware measurements. |
| IV. Integrated capstone | M10. Build and defend a distributed agent system | Join durable job coordination, isolated workers and a model-serving boundary. Demonstrate evaluation, observability, cancellation, overload and failure recovery; defend architecture and report correctness, latency, resource use and human intervention. Use CS329Z-inspired baseline, data/scorer and failure-analysis criteria; reuse MIT-style reasoning about guarantees. |

M1's historical evidence remains credited for the demonstrated capability. New criteria introduced by future revisions become explicit gaps rather than erasing old completion.

## Dependencies and flexibility

| Milestone | Entry requirements |
|---|---|
| M1 | Small-script orientation as needed |
| M2 | Tool-cycle orientation; language/process diagnostics determine the next lesson |
| M3 | Relevant M2 language, async, file and process checkpoints; M11 E1/E2 before substantial agent edits |
| M4 | M3; deeper Codex tracing also needs M12 R1 Rust readiness; K1–K5 completion is not required for initial source traces |
| M12 | Relevant M2 programming readiness; diagnose trees/recursion/complexity, then R1. F0 machine concepts precede K4/K5 as needed. |
| M5 | M2 shell/process foundations; Rust is not a gate to early OS/network lessons; deploying the learned agent uses M3/M4 contracts |
| M6 | Python/tensor/attention readiness; introduce missing mathematics before optimizations |
| M7 | M4 worker boundary and M5 single-host operation/recovery; D1–D3 local storage before durable distributed-state claims |
| M8 | M5 containers/networks/services and M7 coordination/failure reasoning |
| M9 | M6 inference accounting and M5 service operation; hardware-specific labs need a suitable authorized host |
| M10 | M7 durable work, M8 deployment, M9 serving/evaluation, M11 review/acceptance/recovery and M12 compiler evidence; the teaching compiler need not be embedded in the agent |
| M11 | E1/E2 with M2; E3 with a small testable program; E4–E6 during M3/M4 delivery. Full M11 is not a prerequisite to starting those lessons. |

Stage II modules need dedicated time, but an unrelated source-reading requirement does not block an otherwise ready Linux lesson. Preparatory exploration can precede a full milestone without granting its completion. Keep one primary module; reorder eligible lessons under the charter instead of running every subject simultaneously.

## Subject boundaries

| Subject | Core scope | Optional depth |
|---|---|---|
| Programming and agents | JS/TS/Node, targeted Python and required Rust foundations, tools/context/state, concurrency, source tracing, evaluation and bounded extensions | Full UI-framework study, rebuilding a complete commercial harness |
| Engineering practice | Git/GitHub collaboration, explicit specs, small reviewable changes, behavioral tests/TDD, proportionate ADRs, CI, mistake recovery and deliverable acceptance | Complex release automation, organization-wide process administration or extra ceremony without a project need |
| Compilers and supporting machine concepts | M12 small typed language, AST/bytecode execution, optimization correctness, native pipeline and rustc trace; F0 instructions/call stack/cache/linking within M5 | Production compiler/JIT/backend, full CPU design or full architecture course |
| OS and Linux | Processes/threads, scheduling, virtual memory, files/I/O, users/permissions, signals, services, resource isolation and diagnosis | Writing a kernel or device driver |
| Networks and VPS | DNS, TCP/IP, HTTP/TLS, SSH, addressing/routing, ports/firewalls, service reachability, remote state and recovery | Implementing an entire protocol stack |
| Containers and Kubernetes | Images, volumes, namespaces/cgroups, container networking, declarative workloads, scheduling/discovery, configuration/secrets and recovery | Custom operators and cluster internals without a relevant project question |
| Inference and serving | C1–C12 coverage from [advanced materials](materials/advanced-study.md): generation/cache, memory, kernels, batching, vLLM, quantization/speculation, parallelism and reliable serving | C13 backend/architecture specializations and model pretraining |
| Storage and security | Required M7 local indexes/logs/transactions/recovery; M5 least privilege, path boundaries, sandbox and enforced access experiments | Full database engine/SQL optimizer, advanced cryptography, Python native extensions and embedded/no_std projects |
| Message brokers and event streams | Required RabbitMQ/Kafka foundations and bounded labs inside M7: routing, acknowledgements, offsets, retention/replay, consumer groups, ordering, retries/dead letters, overload and application effects | Large production-cluster administration, full CDC/stream-processing platforms |
| Distributed agent systems | State ownership, queues, retries/idempotency, consistency/leases, backpressure, partial failure, observability, security and measured orchestration | Building a general-purpose orchestration framework before evaluating existing tools |

Terminal collaboration, GUI/client ownership and a team with final human review remain required outcomes. A specific product is a candidate implementation, not a permanent curriculum boundary. Official Claude courses are assigned materials for agent mechanisms; the source route retains mini-swe-agent → Pi → Codex, with supporting comparisons.

## Assessment and capstone

Every milestone uses the shared artifact/experiment, explanation and unfamiliar-change standard. [M11](course/modules/engineering-practice.md) adds a required engineering-delivery milestone, estimated initially at 12–18 hours spread through existing core/project allocations; its acceptance practice then continues across later work. This is added scope, not a claim that the existing dates still fit. M7 broker study is initially estimated at 16–18 hours, including overlapping queue/retry outcomes once; two six-hour labs can be separate project slices. Existing evidence is credited only for the criteria it demonstrates. Advanced work includes bounded research comparison or reproduction. The capstone joins durable coordination, isolated workers and model serving, with real multi-host execution and measured failure/recovery. Multi-device inference simulation must be labeled; it does not count as a measured hardware speedup.

## University course selections

[MIT 6.5840 and Stanford CS329Z](materials/university-course-integration.md) are selected required sources inside existing milestones. MIT supplies M7 theory and failure reasoning (20–27h initial selection); Stanford supplies M3/M4/M7/M10 agent design and evaluation (20–28h). These selections are included inside the milestone estimates in the [workload forecast](course/WORKLOAD.md), with shared work counted once. Original MIT Go labs and full Stanford coursework remain optional larger commitments. Preserve M1 credit, all OS/network/broker/Kubernetes/inference outcomes and the 15h weekly cap. Public-material release and learner-readiness checks precede assignments; university calendars do not change personal deadlines.

## Changes

New ideas enter [IDEAS.md](course/IDEAS.md). Equivalent exercises can change routinely while preserving outcomes. Required milestone/core/deadline changes use the charter's impact review and student agreement, then update this map, project/material links and approved schedule together. Existing evidence is mapped forward, and retired IDs remain discoverable.
