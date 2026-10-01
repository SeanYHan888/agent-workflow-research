# Computer organization, algorithms and discrete mathematics

Required M13–M15, accepted September 30, 2026 by the student's “这三个都加上吧”. These are assessed foundations with selected depth, not promises to complete three entire university courses. They extend the [roadmap](../../ROADMAP.md); the [workload](../WORKLOAD.md) counts overlap once. Progress, dates and learner evidence remain in the owning Obsidian project.

## Teaching order and prior credit

Start with short diagnostics, using Python where language overhead would hide understanding. Demonstrated criteria receive credit; a diagnostic changes remaining instruction, not whether a required subject exists. Teach Rust implementations after M12 R1. Read narrow C/assembly examples as needed; no full additional C course is assigned.

Use the next mechanism to select one primary block: DM1 supports reasoning about contracts; DM2 and ALG1/ALG2 support recursive parsers; A1/A2 support VM and OS explanations; A3/A4 support compiler backends and inference costs; ALG3/DM3 support control-flow and protocol analysis. Later storage work uses ALG2/DM3 and probability uses DM4. All M13–M15 criteria join program completion, but their entire completion does not block early M2–M5 lessons. M6/M9 retain their separate linear-algebra/probability prerequisites.

Hours below include selected reading, instruction, learner attempts, experiments and assessment. These are provisional teacher estimates; reforecast from actual pace. A block can contain multiple bounded projects. A project-slot implementation is at most 6–9 hours over two or three weeks; theory uses its explicit core/lab allocation. No project is activated or assigned dates here.

## M13 — Explain the machine executing a program (24–36h)

| ID | Mechanisms and hours | Required evidence |
|---|---|---|
| A1 | Representation and digital logic, 6–8h: signed/unsigned integers, overflow, floating-point limits, byte order, Boolean gates, combinational versus sequential state, ALU/register/memory roles | Explain and test one representation failure; construct a small ALU/register simulation and trace a state transition. Distinguish the simulation from real hardware measurements. |
| A2 | Instruction execution and calls, 8–12h: ISA, registers, fetch/decode/execute, datapath/control, addressing, stack frames and calling convention | Trace a small function from source to the lab target's assembly and call/return state. Add an instruction to a bounded teaching CPU or instruction simulator and defend its behavior. No complete CPU/HDL course required. |
| A3 | Memory hierarchy and CPU performance, 6–10h: cache lines/locality, hierarchy, pipeline hazards and branch prediction concepts; latency versus throughput | Predict then measure one locality experiment with controlled inputs; explain a pipeline/branch example and why an algorithmic improvement need not improve runtime. Label simulator results and noisy timings. |
| A4 | Translation, linking and loading, 4–6h: object files, symbols/relocation, ABI, static/dynamic linking, executable loading | Inspect one object/executable and diagnose an unresolved symbol or ABI mismatch in a safe fixture. Trace source → object → executable → running process; separate linking from OS address mapping. |

Former M5 **F0 is a compatibility reference to A1–A4 evidence**, not a repeated assignment. Transfer its estimated 6–10h into this M13 envelope. CPU caches belong here; virtual memory/page tables/TLB behavior remains M5 O2. Reuse compiler K4 output for A4 while separately assessing the machine explanation.

## M14 — Choose, analyze and implement data structures/algorithms (30–45h)

| ID | Mechanisms and hours | Required evidence |
|---|---|---|
| ALG1 | Analysis and sequences, 8–12h: asymptotic time/space, worst/average/amortized distinctions, arrays/lists/stacks/queues, searching/sorting and recurrences | Compare two solutions to the same bounded workload, derive their costs and explain correctness. Implement a selected search/sort and show where an input invalidates a naive complexity claim. Timing alone is not a complexity proof. |
| ALG2 | Associative and ordered structures, 8–12h: hashing/collisions/load factor, trees/balancing concepts and heaps | Implement a bounded hash table or heap; explain the other structure and a tree operation. Defend an index/priority-queue choice with cost and adversarial-input reasoning. Reuse parser symbol tables and storage indexes rather than building duplicate applications. |
| ALG3 | Graphs, 8–12h: representations, BFS/DFS, topological order, cycles and shortest paths | Build a small dependency-graph analyzer; demonstrate traversal/order or cycle detection, then explain and test a shortest-path algorithm's assumptions, including a counterexample outside them. Connect graph reasoning to compiler blocks or job dependencies. |
| ALG4 | Algorithm design, 6–9h: divide-and-conquer, greedy choice versus dynamic programming, recurrence/state design and reconstruction | Solve one bounded DP problem and explain a greedy counterexample; defend an unfamiliar change, including state definition, recurrence, base cases and time/space costs. Large interview problem banks and advanced complexity theory are optional. |

Python is acceptable for initial reasoning and assessment. Use Rust for selected structures once R1 is ready. The outcome is transferable algorithm design, not language repetition or a problem-count quota.

## M15 — Reason precisely about programs and protocols (24–36h)

| ID | Mechanisms and hours | Required evidence |
|---|---|---|
| DM1 | Logic and mathematical language, 6–9h: predicates/quantifiers, sets/functions/relations, implication and proof/counterexample | Formalize a program contract, distinguish necessary/sufficient conditions, and give a direct proof or counterexample. Explain a quantifier-order bug in a stated claim. |
| DM2 | Induction and recurrence, 6–9h: ordinary/strong/structural induction, recursive definitions and recurrence bounds | Prove a recursive algorithm or syntax-tree property using stated base/inductive cases; derive a simple recurrence bound and diagnose a flawed induction argument. Reuse ALG1 or compiler evidence where it demonstrates these criteria. |
| DM3 | Discrete structures and correctness, 6–9h: graphs/relations, state machines, invariants, safety versus liveness | Model a bounded worker/protocol state machine, prove preservation of one invariant, and find a counterexample to a false liveness claim. State fairness/failure assumptions; a few passing tests are not a proof for all executions. |
| DM4 | Counting and discrete probability, 6–9h: counting rules, conditional probability/independence, random variables, expectation and bounds | Derive a collision or retry probability under explicit assumptions, compare with a small simulation, and explain why correlated failures invalidate a naive independent-retry model. Continuous probability and inference mathematics remain separately scoped. |

For mathematics, the artifact can be a worked derivation/proof plus counterexample or simulation. Require explanation and an unfamiliar variation under the shared [rubric](../ASSESSMENT.md), not a software project for every proof.

## Selected primary sources

The linked official course/lab pages were inspected September 30, 2026. Our checkpoint groupings, experiments and hour estimates are original adaptations; they are not university completion or exam claims. Assign precise chapters/lectures at activation and check tool/architecture compatibility then.

| Source | Selection and role | Boundary |
|---|---|---|
| [Nand2Tetris course](https://www.nand2tetris.org/course) | A1/A2: selected Boolean logic/arithmetic, sequential memory and computer architecture explanations | Use simulation and bounded pieces. Full hardware project sequence, VM/compiler and OS projects are not additional requirements. |
| [CS:APP author labs](https://csapp.cs.cmu.edu/3e/labs.html) | A1–A4: machine representation, assembly/architecture and cache experiments; select accompanying machine-level explanations | Self-study availability and architecture checked before assignment. An x86 teaching trace on an ARM Mac is not native execution evidence. Do not assume instructor-only solutions are available. |
| [MIT 6.006, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | ALG1–ALG4: selected analysis, data structures, graph algorithms and dynamic programming; [official topic calendar](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/calendar/) | Select exercises for the criteria; full university problem sets/exams are optional. |
| [MIT 6.042J, Spring 2015](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | DM1–DM4: definitions/proofs, discrete structures and discrete probability using official text/readings | Selected foundational depth; no claim to cover every number-theory/combinatorics topic or complete the entire course. |

## Programming paradigms and system-design coverage audit

This records existing scope in response to the student's question; it does not silently add another required milestone.

| Topic | Current course coverage | Remaining distinction |
|---|---|---|
| Functional programming | M2 closures/callbacks; related Rust expressions/pattern matching in R1. [Effect is optional](../../materials/resource-catalog.md). | No coherent required pure-functions/immutability/higher-order composition/effect-management module or assessment yet. Language features alone do not establish FP depth. |
| OOP / object-oriented design | Required JS/TS classes/prototypes/interfaces in the [language catalog](../../materials/resource-catalog.md); responsibility/state boundaries in M3/M4. | [Grokking OOD](../../materials/ood-assessment.md) remains a targeted optional bridge. Deep polymorphism, composition-versus-inheritance design and pattern tradeoffs are not a complete required OOD course. |
| System design | Required M3 contracts/state, M4 ownership/integration, M7 storage/queues/backpressure/idempotency/consistency/failure, M10 measured design defense and M11 design/review discipline. | Practical system design is a core thread. A complete interview template/problem bank or every large-scale product architecture is optional. |

A future explicit FP/OOP expansion should define a small shared paradigm-comparison exercise and its workload impact through idea intake. This audit does not change their required depth today.
