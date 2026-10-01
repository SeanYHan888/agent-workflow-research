# Operating systems, networks and distributed operations

September 30 update: the required [systems module](../course/modules/systems-foundations.md) adds M12 compiler/Rust study and explicit M5/M7 mechanism assessments. The rows below select references; our Rust exercises and estimates are course-authored adaptations, not claims of completing the original authors' courses. Each source is read for a bounded question. No book or source checkout is required to be completed cover to cover.

Selected September 28, 2026 for M5/M7/M8. Official source landing pages and topic indexes were inspected on this date. Assignments below are our teaching design; they do not claim full courses or labs were completed or validated locally. Choose precise sections and runtime-matched instructions when preparing the active lesson.

| Source | Role and selected coverage | Demonstration in this program |
|---|---|---|
| [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) | Primary OS mechanism text for M5: processes/process API, CPU scheduling, address spaces/paging, threads/locks, I/O, files and persistence. Teach a narrow C-reading bridge where examples need it. | Explain process/memory/file behavior in a Linux lab, predict scheduling or concurrency behavior, and diagnose a failure. Select chapters by mechanism, not a cover-to-cover prerequisite. |
| [Kurose/Ross networking resources and Wireshark labs](https://gaia.cs.umass.edu/kurose_ross/wireshark.php) | M5 network observation: selected HTTP, DNS, TCP, IP and TLS labs from the authors. Attribute their materials and link to originals. | Explain an observed request path and distinguish name-resolution, transport, TLS and application failures in a controlled lab. |
| [Docker Get Started](https://docs.docker.com/get-started/) | M5 container introduction. Follow relevant official documentation from the index for the selected environment and workload. | Containerize an understood service and explain image/runtime, data persistence, networking and resource boundaries; publishing an image is not required. |
| [Kubernetes Concepts](https://kubernetes.io/docs/concepts/) | M8 reference: workloads, controllers, scheduling/resources, services/DNS, storage, configuration/secrets and recovery. Use documentation matched to the selected cluster version. | Deploy an understood workload, explain ownership and reachability, then observe a controlled failure and recovery. |
| [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.824/) | M7 conceptual foundation, reused in M8/M10: [selected D1–D6 route](university-course-integration.md) for RPC, linearizability, Raft, ZooKeeper, Ray and assessment. Original Go labs require a separate bridge and scope. | Defend failure timelines, consistency histories and one paper claim, then transfer them to the existing worker/broker artifact. Full MIT lab completion remains optional. |

The existing [Linux/Node/Bash resource catalog](resource-catalog.md) supplies practical foundations. These selections complement it with explicit mechanisms and research depth. Runtime commands, VPS vendors, prices, credential handling and deployment choices are resolved for a concrete lab, not by treating a course link as installation authorization.

## Compiler and Rust selections — M12

| Source | Selected role | Boundary |
|---|---|---|
| [The Rust Programming Language](https://doc.rust-lang.org/book/) | R1: ownership, borrowing, structs/enums, errors, generics/traits/lifetimes, smart pointers and selected tests/modules | Foundation for learner implementations and M4 source reading; async mechanisms belong to M5 O3. |
| [Crafting Interpreters — author's repository](https://github.com/munificent/craftinginterpreters) | K1/K2/K3: selected scanner, parser, scope/evaluator, bytecode and call-frame explanations | Original implementations use Java/C. Our smaller typed Rust language is an adaptation; type checking is not attributed to the book's dynamically typed Lox. The book website fetch failed on September 30; the author's repository was accessible. |
| [Cornell CS 4120 lecture notes](https://www.cs.cornell.edu/courses/cs4120/2023sp/notes/) | K1/K2/K4 theory reference: lexical/syntactic structure, static semantics, IR and optimization reasoning | Historical official course notes, not current enrollment or full assignment completion. Select exact notes at lesson preparation; no university assessment credit. |
| [LLVM frontend tutorial](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html) | K4: connect parsing/AST with IR, optimization and object generation | The original tutorial uses C++. Teach the required reading bridge and a tiny Rust-emitted IR subset; a complete LLVM binding or JIT is not required. Match installed LLVM version before executing anything. |
| [Rust Compiler Development Guide](https://rustc-dev-guide.rust-lang.org/overview.html) | K5: locate compiler representations and the relevant checking/code-generation stage | Selected source trace after small-compiler evidence, not an entry-level cover-to-cover rustc assignment. Pin the actual toolchain/source before interpreting internal dumps. |

## Machine, OS and network selections — M13/M5

The later September 30 agreement adds required [M13–M15](../course/modules/core-foundations.md), with the computer-organization, algorithm and discrete-math source map there. Former F0 is now credited and budgeted through M13 A1–A4; M5 retains OS/network/security mechanisms.

OSTEP remains the primary OS source for O1–O3; selected chapters on process APIs/scheduling, address spaces/paging/TLBs, concurrency/locks/condition variables, files and persistence support the module. The authors' security chapters support S1. Use their linked chapters rather than redistributing PDFs. Explain the C examples; Rust can implement adapted experiments, while narrow C/Python examples can keep a language prerequisite from blocking a mechanism lesson.

| Source | Selected role | Evidence connection |
|---|---|---|
| [CS:APP author lab overview](https://csapp.cs.cmu.edu/3e/labs.html) | M13 A1–A4 (former F0) reference for machine representation, assembly, cache and linking concepts | Choose small original experiments, not all CS:APP labs. Inspect the learner's architecture; x86 examples are not native ARM observations. No hardware purchase is implied. |
| [Rust Book concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html) and [Async Book execution](https://rust-lang.github.io/async-book/02_execution/01_chapter.html) | O3 ownership/synchronization and a small executor/wakeup trace | Language memory safety, scheduling and protocol correctness are separately explained. Reuse queue/worker artifacts. |
| [Kurose/Ross Wireshark labs](https://gaia.cs.umass.edu/kurose_ross/wireshark.php) | N1/N2 application, transport and network observations | Use controlled personal traffic or published trace fixtures; state what the trace does and does not prove. |
| [Tokio framing tutorial](https://tokio.rs/tokio/tutorial/framing) | N1 incremental parsing of messages from a byte stream | A learner-authored bounded protocol fixture; exact APIs checked against the chosen crate version at activation. |

Apply the existing Linux permission, sandbox, service and networking references in [the resource catalog](resource-catalog.md) to S1 and N3. These are enforced access/failure experiments, not a requirement to write cryptography, a kernel or a complete TCP implementation.

## Storage and transactions — M7

[SQLite atomic commit](https://www.sqlite.org/atomiccommit.html) and [SQLite WAL](https://www.sqlite.org/wal.html) supply primary-source contrasts for D2/D3. Keep rollback journaling distinct from WAL. Our D1 append-log KV fixture is a small teaching design, not a reproduction of SQLite. Read/write amplification and B+ tree/LSM comparisons extend the course's existing data-structure/system-design references; implement one bounded design and explain the alternatives. A killed process, a simulated torn record and a real power failure are different evidence.

## Optional extensions and source status

[PyO3](https://pyo3.rs/) and [Embedded Rust Book](https://docs.rust-embedded.org/book/intro/index.html) remain optional choices after the required foundations. Their APIs, host/target compatibility and actual costs must be checked at activation; neither is a required deliverable or an installed dependency here.

Official/author landing pages for OSTEP, Kurose/Ross, CS:APP, Cornell notes, LLVM, rustc and SQLite WAL were opened September 30, 2026. The other named Rust/network/SQLite references were inspected during this conversation. This verifies reading availability and general selection, not local builds, every linked lab, complete source compatibility or learner mastery.
