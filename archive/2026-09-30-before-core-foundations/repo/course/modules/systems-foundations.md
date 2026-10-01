# Systems foundations through Rust

Approved September 30, 2026. The student asked for deeper compiler, operating-system and network study after primarily using Python, then explicitly selected storage and security as required and Python extensions/embedded systems as electives. This module specifies learning outcomes; execution tasks, dates and evidence stay in Obsidian. Sources and their limits are in the [reading map](../../materials/systems-reading-map.md).

## Placement and boundaries

- **M12 is new and required:** Rust foundations and a small language compiler, with a bytecode VM, bounded optimization/backend experiment and a source-guided explanation of rustc. It is substantially deeper than reading Rust syntax.
- **M5 retains its ID:** deepen its existing OS/network/security outcomes with the F/O/N/S checkpoints below. Linux command familiarity alone cannot complete them.
- **M7 retains its ID:** add local storage foundations D1–D3 before relying on distributed durability. Existing MIT, RabbitMQ/Kafka and multi-host requirements remain.
- The original M4 Rust bridge is credited through R1 rather than taught twice. Basic harness reading needs R1, not the entire compiler project. OS/network lessons can begin using familiar Python and narrow C examples without waiting for M12.
- Python/native extensions, embedded/no_std work, a complete kernel/network stack, production compiler backends and advanced lock-free structures are optional. Existing independent Rust CLI tasks remain an optional exercise choice, not a second mandatory build.
- Computer organization and algorithm/discrete-reasoning gaps are supporting prerequisites selected by diagnosis, not newly assigned full degree courses. The F0 allowance pays for the bounded machine bridge; larger gaps require a revised estimate.

The mastery standard is artifact/experiment + explanation + unfamiliar change under [ASSESSMENT.md](../ASSESSMENT.md). No source download, AI-written implementation or successful build grants learning credit.

## Prerequisites and sequence

At entry, ask the learner to explain aliasing/copying, a tree traversal, a stack/queue, time/space cost, and a simple state invariant. Credit demonstrated knowledge. Teach recursion, maps/trees, logical conditions and induction only where the next mechanism needs them. Rust is the main new implementation language, not a prerequisite for every systems lesson.

Suggested order, with one primary module at a time:

1. Relevant M2 programming/process readiness → R1 and the relevant F0 machine concepts.
2. K1–K3 compiler construction; O1/O2 and N1/N2 may instead be taught first when useful to the current service question.
3. K4/K5 with F0 and R1 evidence; remaining M5 operation/isolation and network checkpoints.
4. D1–D3 local storage and N3 failure reasoning → remaining M7 distributed work.

This is a dependency map, not a calendar. Existing JS/TS/API-course completion, M1 credit, the October 5–11 break and project dates remain. M10 defense must reference M12 evidence as well as its existing engineering, distributed and serving evidence; the capstone need not embed the teaching compiler.

## M12 — Rust and compiler construction (60–95h total)

Hours include instruction, selected reading, learner implementation, debugging and assessment. Each row is a learning block, not a single side project.

| ID | Mechanism and directed hours | Required evidence |
|---|---|---|
| R1 | Rust foundations, 12–18h: enums/match, Option/Result, ownership/move/borrow/lifetimes, traits/generics/modules, heap allocation and Drop; compare with Python aliasing | Explain and modify a small parser or existing CLI; predict a rejected borrow, a move versus clone and resource cleanup. Explain that lifetime annotations do not keep objects alive. R1 absorbs an estimated 6–10h Rust-reading share of the former M4 envelope; this share is a new planning allocation, not measured historical effort. |
| K1 | Lexing/parsing, 8–12h: tokens, source spans, grammar, precedence, recursive descent or Pratt parsing; relate regular token patterns to finite-state recognition | Learner-authored expression parser with precedence and associativity cases, malformed input and useful error positions. Explain why tokenization and nesting need different structures. |
| K2 | Meaning and reference execution, 10–16h: names/scopes, a small static type system, evaluation order, environments, functions and errors | Define a tiny language with integers/booleans, bindings, branching and first-order functions. Reject unbound names and invalid types before evaluation. Build an AST evaluator as a reference; state overflow/error semantics explicitly. This typed language is our adaptation, not the book's Lox implementation. |
| K3 | Bytecode compiler and VM, 14–22h: lowering, operands, branch targets, call frames and returns | Compile the same language to inspectable bytecode; execute with a small stack VM. Compare evaluator and VM results/errors on shared fixtures. Add one unfamiliar language operation through parser, checker, compiler and VM. This is a compiler even though its target is bytecode. |
| K4 | Optimization and native pipeline, 10–17h: basic blocks/control-flow edges, a bounded dataflow analysis, constant folding/propagation, IR versus machine code and linking | Explain and verify one optimization including an overflow or branch counterexample. For a tiny supported expression/function subset, emit LLVM IR or another explicitly selected backend input and inspect resulting object/assembly behavior. Record target architecture/tool versions; distinguish reused backend work from learner implementation. Full JIT/register allocation is elective. |
| K5 | rustc mechanisms and defense, 6–10h: selected AST/HIR/MIR path, borrow checking as static analysis, monomorphization versus dynamic dispatch | Trace one accepted/rejected Rust example through appropriate compiler output/source at a pinned toolchain. Explain what the small compiler does not implement, defend semantics and diagnose an unseen bug. Do not implement Rust's borrow checker as a hidden requirement. |

Implementation slices should each consume **at most 6–9 project hours** if using the three-hour weekly project slot: expression parser; name/type checker; evaluator/function calls; expression bytecode; branch/call-frame extension; one optimization; tiny backend experiment. Larger blocks use explicit core/lab allocation or split further. Each slice has a working independent checkpoint; none grants all of M12 by itself. The teacher provides questions, hints and review, not completed student solutions.

## M5 — OS, networking and security depth (75–110h total)

The total includes the existing service, SSH, container and recovery work. These are requirements within M5, not an additional total to add again.

| ID | Mechanism | Required evidence |
|---|---|---|
| F0 | Machine bridge: bits/integer representation, pointers/layout, instructions/registers, call stack, cache locality, objects/linking versus loading | Inspect one small compiled function on the actual lab architecture; explain a call/return and one data-layout or locality measurement. Distinguish virtual addresses from physical memory. Selected C/assembly reading only; no full C course assumed. |
| O1 | Processes and CPU: user/kernel mode, system calls, process creation/exec/wait, scheduling, signals, pipes/file descriptors | Trace and explain an existing runner's process tree and output flow. Diagnose a blocked pipe or lingering child and demonstrate cancellation/cleanup. A scheduler simulation is labeled as such. |
| O2 | Memory: address spaces, virtual memory, pages/page tables, TLB, page faults, allocation and mapping | Predict and measure a selected locality/allocation experiment; explain which observations show application allocation, OS paging or CPU caching. Use a bounded simulator where privileged measurements are unavailable. |
| O3 | Concurrency: threads, shared state, locks/condition variables, deadlock, atomics and happens-before; async polling/wakeup and blocking | Implement one bounded producer/consumer queue or reuse the worker queue. Explain a deadlock/race history and compare synchronization choices. Trace a tiny executor's wakeup path; safe Rust does not prove protocol correctness. Advanced atomics/lock-free implementation is optional. |
| N1 | Network layers: application framing, sockets, TCP streams, UDP datagrams, IP/subnets/routing, link layer and ARP/ND concepts | Implement a bounded framed protocol that handles partial reads/writes and multiple messages per read. Trace a request across application/transport/network layers. |
| N2 | End-to-end communication: DNS, TCP connection/retransmission/flow versus congestion control, HTTP/TLS, NAT/firewalls, connection reuse | Capture only learner-owned lab traffic or use authors' trace fixtures. Explain packet evidence and diagnose DNS, listener, TLS and HTTP failures separately. Encrypted payloads need not be decrypted to explain connection behavior. |
| N3 | Failure and overload: timeouts, partial failure, request identity, bounded buffering and backpressure | Inject delay/disconnection and a slow reader into the existing service. Demonstrate bounded memory/queue behavior and an unknown-outcome reconciliation path. Reuse this evidence in M7; transport retry is not proof of exactly-once effects. |
| S1 | Security: users/groups, rwx/ownership, umask, least privilege, authentication/authorization, real paths/symlinks, check/use races, secrets and sandbox boundaries | With harmless fixtures, demonstrate a denied access and its specific repair; test path traversal/symlink escape against the selected file boundary. Explain enforcement and residual race risks. Demonstrate non-root execution, constrained mounts, resource limits and network restrictions using existing M5 labs. Never treat string-prefix validation as sufficient isolation. |

Planning allocation inside M5: F0 **6–10h**, O1–O3 **24–34h**, N1–N3 **18–26h**, S1 **6–8h**, existing operations/container/recovery practice **21–32h** = **75–110h**. Shared permission/network experiments count once. Deeper kernel development is optional; M5 requires mechanism explanations, controlled experiments and diagnosis.

## M7 — storage before distributed state (+20–30h inside M7)

| ID | Mechanism and directed hours | Required evidence |
|---|---|---|
| D1 | Storage models/indexes, 6–9h: pages, append logs, B+ tree versus LSM design, read/write amplification and compaction | Build a small append-log key/value store with an in-memory index and compare its costs with tree/LSM designs. Implementing both complete index families is not required. Define record framing/checksums and incomplete-tail handling. |
| D2 | Durability/recovery, 8–12h: buffering, flush/fsync, write ordering, commit markers, WAL/checkpointing | Demonstrate acknowledged-write and incomplete-write behavior under controlled process kills and simulated torn records; explain assumptions and recovery limits. Process-kill evidence is not power-loss validation. Compare with SQLite's actual journal/WAL contract. |
| D3 | Transaction/concurrency reasoning, 6–9h: atomicity/isolation/durability, lost updates, snapshots/MVCC concepts and local versus replicated commit | Use SQLite transactions in a small concurrent-history experiment; explain one anomaly and prevention method. Relate local durable state to M7 replication/acknowledgment and uncertain external effects. Reuse existing job IDs and failure traces. |

D1 implementation can be one 6–9h practical slice; D2 recovery work is another bounded slice with theory charged separately. The toy store remains a teaching fixture; the real agent can retain SQLite/Redis. Extend that fixture with N1 framing if useful; a production database or a second Raft implementation is not required. Full SQL/query optimization and full database-course completion are elective depth.

## Diagnosis and optional directions

The student's Python experience suggests these systems questions are worth investigating, but it does not establish a deficit in algorithms, mathematics or engineering. Before adding remediation, check:

- Data structures/algorithms: trees, hash maps, graphs, recursion and asymptotic costs used in parsing, indexing and routing.
- Discrete reasoning: logic, sets/relations, state machines and invariants used in types, protocols and concurrency.
- Measurement: repeatable inputs, a baseline, units and variance before performance claims.

Python extensions/PyO3 and embedded/no_std are captured electives, without mandatory deliverables or hours in the required forecast. Existing M11 engineering and M6/M9 mathematics/inference stay in scope; no new full algorithm, discrete-math or computer-architecture course is silently added.

## Progress ownership

The [live overview](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Notes/Coding Agent Course/00 Start Here.md>) routes to current work. The existing Linux/coordination note retains its tasks/evidence and links to these expanded M5/M7 criteria; split it before activation rather than enlarging its old 30-hour sprint. M12 has no active execution project yet. Create only the next bounded owner when ready; the optional Rust CLI may supply some R1 evidence if selected, without duplicating its checklist.
