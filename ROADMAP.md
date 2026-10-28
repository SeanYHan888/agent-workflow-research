# Distributed AI Agent Systems — roadmap

Current curriculum: **v1.10, October 17, 2026** — nineteen milestones (M1–M19) in four stages, taught through one evolving project. Each milestone has a [module guide](course/modules/README.md). Milestone IDs are stable across revisions so links and learning credit carry forward; the [decision record](course/CHANGELOG.md) explains every change, and [HISTORY.md](HISTORY.md) locates earlier versions. This map is adaptable under the [course charter](course/CHARTER.md).

## How the course is taught

Start each session with a useful build, bug or experiment, introduce theory at the point of need, and finish with observed behavior and a learner explanation. The [charter](course/CHARTER.md#project-first-teaching--adopted-october-6-2026) owns the teaching agreement and the [session workflow](teaching/README.md#prepare-and-teach) shows how one session runs. The [October 4 build-first options](course/projects/agentic-linux-distribution/BUILD-FIRST-OPTIONS.md) (an early VPS route and reduced graduation requirements) remain unselected alternatives.

## Start and schedule

A new learner starts at M1 and M2: read the [M1 tool-cycle guide](course/modules/agent-tool-cycle.md), then begin the controllable local runner in the [project route](#project-route) with one observable check. Teach the next missing language/process concept inside that attempt and introduce [M11](course/modules/engineering-practice.md) E1/E2 Git inspection and recovery before substantial edits. A local runner needs no VPS or provider decision. A returning learner starts from their recorded evidence, not from the first chapter; calendar dates do not establish learning.

Budget and active-work limits are owned by the charter: 15 hours/week, normally 10 core/labs, 3 project and 2 exploration, with one primary module and one active course project. New project options have no dates until activated. The [workload forecast](course/WORKLOAD.md) estimates remaining scope and counts overlap once. No overall finish date is promised.

Progress, dates and learning evidence live with the learner, not in the course plan. Keep them in your own planning system or a gitignored `private/` folder.

## One project connects the course

The [final-project folder](course/projects/agentic-linux-distribution/README.md) owns the six design goals and a mapping for M1–M19: **Rust, easy remote SSH, distributed system, agentic first, safety and lightweight operation across remote VPS nodes**. Build toward this goal through the course: runner → typed agent → worker adapter → Linux service → remote nodes → distribution release. Reuse working components and assessment evidence; M10 integrates them.

Keep the final architecture open. A VPS node must work headlessly with bounded resources; a desktop or local model is not required on each node. Choose numerical limits, a VPS profile and the image delivery method through experiments. Foundations, Kubernetes and inference remain assessed subjects even when their teaching artifacts or services do not ship on the node.

## Project route

Use this route for lesson selection; the milestone tables below define assessed depth and dependencies. Rows are project families, not single 21-day assignments or new calendar commitments. Select one small increment at a time, reuse the same artifact where useful, and split work at the capacity checks in the [catalog](course/PROJECTS.md). Cross-cutting foundations enter when the next mechanism needs them.

| Build or investigate | Useful increments and observable checks | Concepts taught through the work |
|---|---|---|
| A controllable local runner | Task-file CLI → fixed harmless child process → framed output and cancellation. Diagnose malformed input, failed startup and a process that must stop. | M2 files, functions, errors, async, streams and shell; M11 inspect/recover changes. M1 credit is reused. |
| A typed agent using that runner | Validate one task/tool contract, add a bounded tool loop and persist/reload one session. Reject invalid input and recover an interrupted run. | M3 types, runtime validation, context/state; M16 pure logic, effects and object boundaries; M11 tests/review. |
| An MCP surface for the runner | Trace one discovery and tool call, build a narrow stdio server over job status/logs, connect it from Pi and another host, then refuse an out-of-scope request. Later reach a node over `ssh` stdio. | M19 MC1–MC4; reuses M1 tool cycle, M3 validation, M4 Pi trace, M18 CLI/skill comparison and M5 access boundaries. |
| A reusable, evaluated skill | Write one skill for inspecting a failed runner job; compare it with a no-skill baseline, test irrelevant requests and missing tools, then revise and disable it. | M18 AS1–AS4; reuse M3/M4 harness and M11 review evidence. No marketplace build required. |
| A real harness connection | Trace one request, implement one narrow extension/adapter and compare terminal/GUI interruption and reconnect behavior. | M4 process/provider/client ownership and required source study; M12 R1 before deeper Rust traces. |
| A supervised Linux worker | Start/stop a fixture service, inspect logs after reconnect, bound resource use and demonstrate a denied operation and recovery. | M5 processes, files, memory, SSH, networks and isolation; M13 relevant machine checkpoints. Reuse M2 process experiments. |
| A useful Rust component and compiler labs | Build a small CLI component; separately grow parser → checker/evaluator → bytecode VM → bounded optimization. Test malformed input and explain an unseen language change. | M12 R1/K1–K5, with M13 machine traces, M14 parsing/structure costs, M15 proofs and M16 Rust transfer at their entry gates. Each compiler increment is separately scoped. |
| Durable work across nodes | Add local job state/recovery, then bounded dispatch and reconciliation. Inject duplicate delivery, disconnect and worker loss; use separate RabbitMQ and Kafka labs. | M7 storage, transactions, queues, partial failure and required distributed theory; M14 indexes/queues and M15 protocol invariants. |
| A measured model endpoint | Trace one-token generation and KV growth, measure prefill/decode, then compare bounded serving/optimization experiments. Label simulated parallelism. | M6 inference accounting → M9 kernels, batching, vLLM, quantization and parallelism. Use an authorized suitable host when hardware is required. |
| Deployment and interface comparisons | Deploy the understood service with Kubernetes and test recovery; separately trace T3/Quattro behavior, make a reversible extension and defend a design choice. | M8 orchestration and M17 T3/Quattro criteria, retaining each module's full evidence requirements. |
| A reproducible distribution release | Integrate proven components; verify fresh install, SSH, two remote nodes, measured limits, failed-update recovery and release artifacts. | M10 release brief and all graduation gates; M11 acceptance. Packaging begins incrementally before final assessment. |

Foundation work produces concrete evidence alongside this route: machine traces and memory experiments (M13), implemented structures and complexity comparisons (M14), proofs/counterexamples and protocol histories (M15), and two designs exercised against a shared contract (M16). The full criterion lists still apply; these examples are entry points, not substitutes for all required depth. An isolated lab can be the best project when it makes a mechanism visible.

## Stages and milestones

Each row is a learning destination, not one execution project. Larger milestones contain several independently finishable projects. Use [project mappings](course/PROJECTS.md), [materials](materials/README.md) and the [assessment rubric](course/ASSESSMENT.md).

| Stage | Milestone | Boundary and demonstration |
|---|---|---|
| I. Foundations | M1. Explain and implement an agent tool cycle | Model output versus harness execution; messages, validation, stop conditions and failures. Preserve the existing Section 1 evidence rather than assigning it again. |
| I. Foundations | M2. Write and control a program | JS/TS, Node, async, errors, files, subprocesses and basic Bash/process/network literacy. Build and explain a bounded task runner. |
| I. Foundations; reinforced throughout | M11. Deliver and recover an engineering change | Git/GitHub, issues/specs, focused commits, PRs/CI, review, ADRs, TDD, recovery and deliverable acceptance. [E1/E2](course/modules/engineering-practice.md) begin with M2; the [agent review/CI delivery experiment](course/projects/agent-review-ci-lab.md) follows through M3/M4, measuring missed defects and human review effort. |
| I. Foundations | M3. Build a small typed agent | Provider/tool contracts, runtime validation, context, persistence, cancellation and tests. Extend the runner rather than starting several independent agents. Use selected CS329Z component/baseline lessons from the [university integration map](materials/university-course-integration.md). |
| I–II. Programming and design | M16. Compare and defend programming paradigms | [P1–P4](course/modules/programming-paradigms.md): pure functions/effects, encapsulation/polymorphism/composition, type-based modeling and a shared FP/OOP comparison with a small Rust transfer. |
| I–II. Foundations | M13. Explain the machine executing a program | [A1–A4](course/modules/core-foundations.md): representation/logic, ISA/datapath/calls, caches/pipeline and linking/loading, with simulation and actual-target evidence distinguished. |
| I–II. Foundations | M14. Analyze and implement algorithms/data structures | [ALG1–ALG4](course/modules/core-foundations.md): complexity/correctness, sequences/maps/trees/heaps, graphs and algorithm design including dynamic programming. |
| I–III. Foundations | M15. Reason about programs and protocols | [DM1–DM4](course/modules/core-foundations.md): logic/proofs, induction/recurrences, graphs/state invariants, counting and discrete probability; learner derivations and unfamiliar variations. |
| II. Reliable single-host systems | M4. Explain real harnesses and integration boundaries | Selected mini-swe-agent/Pi source, Pi extension and real-worker adapter; terminal and GUI session ownership. Retain required Codex source study after smaller traces and M12 R1 Rust readiness; compiler completion is not a prerequisite to initial harness reading. CS329Z design material supports harness/memory/framework comparisons without replacing source traces. |
| I–II. Language and systems foundations | M12. Build and explain a small compiler | [R1/K1–K5](course/modules/systems-foundations.md): Rust ownership/types, lexing/parsing, scope/type checking, AST evaluator, bytecode compiler/VM, bounded optimization/native pipeline and a rustc mechanism trace. Learner-authored artifacts plus unfamiliar-change defense. |
| II. Reliable single-host systems | M5. Operate an isolated service on Linux | OS processes/threads, virtual memory, files/I/O, permissions and scheduling; Linux services/logs, SSH, DNS/TCP/HTTP/TLS, routing/firewalls, VPS recovery, Docker images/volumes/networks and resource isolation. Use M13 A1–A4 for F0 machine prerequisites; require the [O1–O3/N1–N3/S1](course/modules/systems-foundations.md) OS, socket/framing, packet/failure and access-boundary evidence before orchestration. |
| II. Reliable single-host systems | M6. Explain and measure model inference | Tensor/attention prerequisites, one-token generation, sampling, KV cache, prefill/decode, memory/latency accounting and single-host serving. Keep model execution distinct from the harness tool loop. |
| III. Distributed systems | M7. Coordinate durable distributed work | [D1–D3 storage foundations](course/modules/systems-foundations.md): indexes, durable logs, crash recovery and transaction/concurrency reasoning; then state ownership, queues, concurrency, idempotency, retry/backoff, leases, uncertain outcomes, consistency and recovery under partial failure. Required [message-broker study](course/modules/message-brokers.md): RabbitMQ job queues and Kafka retained event streams, with acknowledgements/offsets, replay, ordering and failure experiments. Use the selected MIT 6.5840 replication/consistency/ownership route and CS329Z single/multi-agent comparison. Reuse worker adapters and demonstrate worker loss and duplicate delivery. |
| III. Distributed systems | M8. Operate services with Kubernetes | Workload lifecycle, scheduling/resources, service discovery, networking, configuration/secrets, persistent state, rollout and recovery. Compare behavior with the understood single-host deployment. |
| III. Distributed systems | M9. Analyze efficient and distributed inference | Kernels, batching, KV allocation, vLLM source, quantization, speculative decoding, parallelism and interconnect costs. Use controlled benchmarks and distinguish simulated multi-device reasoning from hardware measurements. |
| II–IV. Agentic Linux | M17. Explain and integrate an agent desktop | Dedicated [T3 Code and Omarchy Quattro course](course/modules/agentic-linux.md): reuse the M4 GUI trace, then study Linux service operation, shell/IPC, a reversible extension and a design comparison. |
| I–II. Agent workflows | M18. Design and evaluate reusable agent skills | [AS1–AS4](course/modules/agent-skills.md): select and dissect, author one bounded skill, compare held-out behavior, maintain and adapt host assumptions. Required evidence includes non-activation/failure cases and learner explanation. |
| I–II. Agent workflows | M19. Connect, expose and secure tools with MCP | [MC1–MC4](course/modules/mcp.md): protocol trace, learner-authored server, two-host comparison with tool-loading and CLI/skill alternatives, and server/host-enforced boundaries. Optional Tasks/Apps/sampling depth only when the runner needs it. |
| IV. Integrated capstone | M10. Publish and defend an agent-first Linux distribution | Use the [distribution release brief](course/projects/agentic-linux-distribution.md): deployable VPS image, Rust systems component, SSH workflow, measured resource limits, safety, updates, recovery and public release evidence. Join durable job coordination, isolated workers and a model-serving boundary. Demonstrate evaluation, observability, cancellation, overload and failure recovery; defend architecture and report correctness, latency, resource use and human intervention. Use CS329Z-inspired baseline, data/scorer and failure-analysis criteria; reuse MIT-style reasoning about guarantees. |

M1's historical evidence remains credited for the demonstrated capability. New criteria introduced by future revisions become explicit gaps rather than erasing old completion.

## Dependencies and flexibility

| Milestone | Entry requirements |
|---|---|
| M1 | Small-script orientation as needed |
| M2 | Tool-cycle orientation; language/process diagnostics determine the next lesson |
| M3 | Relevant M2 language, async, file and process checkpoints; M11 E1/E2 before substantial agent edits |
| M4 | M3; deeper Codex tracing also needs M12 R1 Rust readiness; K1–K5 completion is not required for initial source traces |
| M12 | Relevant M2 programming readiness, then R1; relevant M14 ALG1/ALG2 and M15 DM1/DM2 support parsing/checking, and M13 A1/A2/A4 precede K4/K5 as needed. Credit demonstrated prerequisites without waiting for full M13–M15 completion. |
| M16 | Relevant M2 functions/classes/interfaces/errors; use a small M3 artifact. Rust transfer follows M12 R1; full M16 is not a gate to starting M3/M4. |
| M13 | M2 programming readiness for compiled examples; A1 before A2, A2 before A4; R1 only when choosing Rust implementations |
| M14 | Basic programming, with DM1/DM2 introduced as needed; use Python before R1 if helpful |
| M15 | Diagnostic mathematical/programming readiness; DM1 before proof-heavy work; use DM2 with algorithms and DM3 with protocols |
| M5 | M2 shell/process foundations; Rust is not a gate to early OS/network lessons; deploying the learned agent uses M3/M4 contracts |
| M6 | Python/tensor/attention readiness; introduce missing mathematics before optimizations |
| M7 | M4 worker boundary and M5 single-host operation/recovery; D1–D3 local storage before durable distributed-state claims |
| M8 | M5 containers/networks/services and M7 coordination/failure reasoning |
| M9 | M6 inference accounting and M5 service operation; hardware-specific labs need a suitable authorized host |
| M17 | T1 reuses M4 GUI evidence; T2/Q1 need relevant M5 service, network and permission checkpoints; Q2 follows Q1 and C1 compares both paths. |
| M18 | AS1 after M1 orientation; AS2 after relevant M2 and M11 E1/E2; AS3 after AS2 and fixture reasoning; AS4 with relevant M4 boundaries. Does not block M3/M4 or early Linux work. |
| M19 | MC1 after M1 orientation and M2 stdio/JSON; MC2 after M3 validation; MC3 with M4 harness study; remote transport/auth in MC4 after M5 N1–N3/S1. Does not block M3/M4 or early Linux work. |
| M10 | M19 MCP boundary decision and evidence, M18 skill evaluation/maintenance evidence, M17 design/comparison evidence, M7 durable work, M8 deployment, M9 serving/evaluation, M11 review/acceptance/recovery, M12 compiler evidence, M13–M15 foundation evidence and M16 comparative-design evidence; the teaching compiler need not be embedded in the agent |
| M11 | E1/E2 with M2; E3 with a small testable program; E4–E6 during M3/M4 delivery. Full M11 is not a prerequisite to starting those lessons. |

Stage II modules need dedicated time, but an unrelated source-reading requirement does not block an otherwise ready Linux lesson. Preparatory exploration can precede a full milestone without granting its completion. Keep one primary module; reorder eligible lessons under the charter instead of running every subject simultaneously.

## Subject boundaries

| Subject | Core scope | Optional depth |
|---|---|---|
| Programming and agents | JS/TS/Node, targeted Python and required Rust foundations, tools/context/state, concurrency, source tracing, evaluation and bounded extensions | Full UI-framework study, rebuilding a complete commercial harness |
| Agent skills | M18 metadata and triggers, progressive loading, scoped workflows, evaluation, provenance, host assumptions and rollback | General skill marketplace, exhaustive repository completion or mandatory UI skill usage |
| Model Context Protocol | M19 JSON-RPC messages, stateless requests and versioning, tools/resources, schema validation, errors/cancellation, stdio and HTTP transports, host tool-loading strategies, authorization and untrusted-content boundaries | General gateway/registry, every extension (Tasks, Apps, Skills over MCP) or publishing public servers |
| Engineering practice | Git/GitHub collaboration, explicit specs, small reviewable changes, behavioral tests/TDD, proportionate ADRs, CI, mistake recovery and deliverable acceptance | Complex release automation, organization-wide process administration or extra ceremony without a project need |
| Compilers | M12 small typed language, AST/bytecode execution, optimization correctness, native pipeline and rustc trace | Production compiler/JIT/backend |
| Computer organization | M13 representation/logic, instructions/datapath/calls, caches/pipeline and linking/loading; absorbs former F0 | Complete CPU/HDL design and advanced microarchitecture |
| Algorithms and discrete mathematics | M14 complexity/structures/graphs/DP and M15 logic/proofs/induction/invariants/counting/probability | Full university course sequences, advanced complexity theory and large interview banks |
| Programming paradigms and system design | Required [M16 P1–P4](course/modules/programming-paradigms.md): FP, OOD, type-based modeling and design comparison; practical system design continues through M3/M4/M7/M10/M11 | Full Haskell/OCaml courses, category theory, Effect adoption, design-pattern and interview catalogs |
| OS and Linux | Processes/threads, scheduling, virtual memory, files/I/O, users/permissions, signals, services, resource isolation and diagnosis | Writing a kernel or device driver |
| Networks and VPS | DNS, TCP/IP, HTTP/TLS, SSH, addressing/routing, ports/firewalls, service reachability, remote state and recovery | Implementing an entire protocol stack |
| Containers and Kubernetes | Images, volumes, namespaces/cgroups, container networking, declarative workloads, scheduling/discovery, configuration/secrets and recovery | Custom operators and cluster internals without a relevant project question |
| Inference and serving | C1–C12 coverage from [advanced materials](materials/advanced-study.md): generation/cache, memory, kernels, batching, vLLM, quantization/speculation, parallelism and reliable serving | C13 backend/architecture specializations and model pretraining |
| Storage and security | Required M7 local indexes/logs/transactions/recovery; M5 least privilege, path boundaries, sandbox and enforced access experiments | Full database engine/SQL optimizer, advanced cryptography, Python native extensions and embedded/no_std projects |
| Message brokers and event streams | Required RabbitMQ/Kafka foundations and bounded labs inside M7: routing, acknowledgements, offsets, retention/replay, consumer groups, ordering, retries/dead letters, overload and application effects | Large production-cluster administration, full CDC/stream-processing platforms |
| Distributed agent systems | State ownership, queues, retries/idempotency, consistency/leases, backpressure, partial failure, observability, security and measured orchestration | Building a general-purpose orchestration framework before evaluating existing tools |

Terminal collaboration, GUI/client ownership and a team with final human review remain required outcomes. T3 Code and Omarchy Quattro are required M17 case studies; the distribution implementation is selected from comparison evidence. Official Claude courses are assigned materials for agent mechanisms (the MCP selections now serve M19); the source route retains mini-swe-agent → Pi → Codex, with supporting comparisons.

## Assessment and capstone

Every milestone uses the shared artifact/experiment, explanation and unfamiliar-change standard. [M11](course/modules/engineering-practice.md) adds a required engineering-delivery milestone, estimated initially at 12–18 hours spread through existing core/project allocations; its acceptance practice then continues across later work. This is added scope, not a claim that the existing dates still fit. M7 broker study is initially estimated at 16–18 hours, including overlapping queue/retry outcomes once; two six-hour labs can be separate project slices. Existing evidence is credited only for the criteria it demonstrates. Advanced work includes bounded research comparison or reproduction. The final product is a published agent-first Linux distribution, scoped by the [release brief](course/projects/agentic-linux-distribution.md). Publication readiness and learner mastery need separate evidence. The capstone joins durable coordination, isolated workers and model serving, with real multi-host execution and measured failure/recovery. Multi-device inference simulation must be labeled; it does not count as a measured hardware speedup.

## University course selections

[MIT 6.5840 and Stanford CS329Z](materials/university-course-integration.md) are selected required sources inside existing milestones. MIT supplies M7 theory and failure reasoning (20–27h initial selection); Stanford supplies M3/M4/M7/M10 agent design and evaluation (20–28h). These selections are included inside the milestone estimates in the [workload forecast](course/WORKLOAD.md), with shared work counted once. Original MIT Go labs and full Stanford coursework remain optional larger commitments. Preserve M1 credit, all OS/network/broker/Kubernetes/inference outcomes and the 15h weekly cap. Public-material release and learner-readiness checks precede assignments; university calendars do not change personal deadlines.

## Changes

New ideas enter [IDEAS.md](course/IDEAS.md). Equivalent exercises can change routinely while preserving outcomes. Required milestone/core/deadline changes use the charter's impact review and student agreement, then update this map, project/material links and approved schedule together. Existing evidence is mapped forward, and retired IDs remain discoverable.
