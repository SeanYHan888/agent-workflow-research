# Agent-first Linux distribution — project direction

This is the main goal that connects the course. The student set this direction on October 4, 2026. The final design is open. Use the course to learn, test choices and build toward a published distribution that can run across several remote VPS machines with limited resources.

**Student's keywords:** Rust; easy remote SSH; distributed system; agentic first; safety; lightweight.

This folder owns the project goals and their course connections. The [release brief](../agentic-linux-distribution.md) owns deliverables and acceptance criteria. The [course roadmap](../../../ROADMAP.md) owns milestone requirements. Obsidian project notes own execution tasks and learning evidence.

## What the keywords mean for this project

| Goal | Design direction | Evidence to collect |
|---|---|---|
| **Rust** | Prefer Rust for new systems components that we own, such as a worker, supervisor or management CLI. Select the component through a small experiment. Reuse existing tools where appropriate. | Explain ownership, errors, concurrency and resource use in a useful Rust component. Measure its behavior and test failure cases. Rust alone is not proof of safety or low resource use. |
| **Easy remote SSH** | Make setup, connection, inspection, updates and recovery clear from a remote terminal. A node must be usable without a graphical session. | From a clean client setup, connect with verified host identity, inspect a job, disconnect, reconnect and recover useful state. Record setup steps and human time. Test access revocation and a recovery route for a bad configuration. |
| **Distributed system** | Support useful agent work across multiple remote VPS nodes. Define ownership of jobs, state and results, with bounded retries and concurrency. | Test at least two real remote VPS nodes. Observe disconnects, uncertain outcomes, duplicate delivery, node loss and recovery. Local simulation can prepare these tests but cannot replace remote evidence. |
| **Agentic first** | Make starting, observing, controlling and reviewing agent work central to normal system use. Keep execution state and human control visible. | Run a representative task from request to reviewed result. Demonstrate cancellation, permissions, logs and resume. Compare the workflow with a plain upstream setup. |
| **Safety** | Limit what an agent can affect. Separate untrusted task content from authority. Protect credentials, workspaces and hosts; make changes inspectable and recoverable. | Test a denied operation, a cross-workspace access attempt, an untrusted instruction that requests more authority, and interruption/recovery. Show enforced boundaries and clear records of actions. A prompt or approval dialog alone is not an OS boundary. |
| **Lightweight** | Make small VPS machines a normal target. Keep required services few and resource use bounded. The node must work without a desktop, GPU or local model weights; model execution can use a separate endpoint. | Measure the base OS and the added agent components separately: idle/peak RAM, CPU, disk/image size, process count, startup time, network traffic and log/state growth. Test under memory, disk and concurrency limits. |

## Decisions to make through study

The Linux base, distribution name, image/install format, init/service manager, control interface, network topology and Rust component boundaries are not selected. T3 Code and Omarchy Quattro are case studies. Their useful ideas can inform the design without making either product a dependency on every VPS.

Before the first build slice, choose one supported architecture and VPS profile. Set numerical resource limits and a repeatable workload before comparing implementations. No minimum RAM, CPU, storage or performance claim is established yet. Select the installation format from the target's supported deployment path; a desktop ISO is not assumed.

Compare a small headless node with an optional richer client or controller. Decide where coordination, storage and model serving belong from evidence. Kubernetes, RabbitMQ, Kafka and inference engines remain course subjects; their study does not require putting each service on every small VPS.

## How the whole course contributes

| Milestone | Contribution to this project |
|---|---|
| M1 — Tool cycle | Explain how a request becomes a tool action and how execution stops. Preserve the existing demonstrated evidence. |
| M2 — Programming and processes | Build the small runner that starts, observes and stops work; practice files, streams, errors and shell control. |
| M3 — Typed agent | Define task, tool, provider and result contracts. Reuse the runner as the first agent prototype. |
| M4 — Harnesses and interfaces | Trace actual harnesses; select or adapt an execution interface. Explain ownership across terminal, client, server and provider. |
| M5 — Linux, networks and security | Operate a small node over SSH. Explain processes, memory, files, services, network failures, permissions and isolation. |
| M6 — Inference | Explain the cost and behavior of the model endpoint. Distinguish agent overhead from model memory and compute. |
| M7 — Storage and distributed work | Add durable job state, bounded queues, retries, deduplication and node recovery. Use storage and protocol experiments to defend guarantees. |
| M8 — Kubernetes | Compare orchestration with the simpler service deployment. Measure added cost and explain when a separate controller or cluster is justified. |
| M9 — Efficient/distributed inference | Decide where model execution should run. Use resource and latency evidence; a small VPS is not assumed to run large models locally. |
| M10 — Integration and release | Combine the proven parts, validate the six goals on remote VPS nodes, and publish the supported distribution and recovery guide. |
| M11 — Engineering practice | Apply Git, tests, review, CI, release acceptance and recovery to each useful project change. |
| M12 — Rust and compilers | Use Rust foundations for a suitable systems component. Compiler work teaches parsing, validation and execution semantics; the teaching compiler can remain a separate learning artifact. |
| M13 — Computer organization | Explain memory/CPU limits, binaries, caches and loading when diagnosing a small node. |
| M14 — Algorithms and data structures | Analyze queue, index and scheduling choices, including their time and memory cost. |
| M15 — Discrete mathematics | State invariants, reason about retries and ownership, and analyze failure histories and probability assumptions. |
| M16 — Programming design | Compare pure logic, effects, objects and types in the shared task/service design. Defend the boundaries used. |
| M18 — Agent Skills | Package one useful runner/service workflow with explicit scope, evidence, evaluation and rollback. Reuse the tested behavior in the distribution where justified; do not require a marketplace or every reviewed skill. |
| M19 — Model Context Protocol | Expose node job state and gated controls to MCP hosts through a narrow server, using `ssh` stdio where suitable. Decide with evidence whether the release ships an MCP surface, which transport and which enforced limits; keep it inside the measured resource budget. |
| M17 — T3 Code and Omarchy Quattro | Study agent control and desktop integration, then identify what to reuse, adapt or omit for a small remote node. |

## Project-first course — adopted October 6, 2026

The [project route](../../../ROADMAP.md#project-route) now drives lessons through useful builds, experiments and debugging tasks. The first scheduled learning slice remains the local JS/Node runner, taught through concrete increments and point-of-need explanations. The six product goals guide each choice; foundation labs may remain separate teaching artifacts.

The [October 4 options](BUILD-FIRST-OPTIONS.md) additionally compare early VPS, Rust-first and declarative-OS routes and propose reduced graduation scope. Those choices remain open. The adopted teaching change retains required subjects, current dates and explicit resource-completion goals.

## Working method through the course

Follow one evolving path: runner → typed agent → worker adapter → Linux service → remote nodes → measured distribution release. Use Rust where the selected systems component benefits from it; an early JavaScript/TypeScript prototype can remain a reference or test driver. Do not translate every earlier exercise by default.

At the start of each module, name the project question that the module can answer. At its end, retain one useful component, experiment or design decision with evidence in its owning project. Explain how it supports one of the six goals. Some foundations need isolated exercises; record their connection without forcing every teaching artifact into the release.

M10 integrates and publishes work developed through the course. Keep one primary module and one active practical project within 15 hours/week. Each execution slice must fit within 21 days at its allocated capacity. Count reused work once. Existing deadlines and learning credit remain; this document does not activate another project or record completed work.

The current effort forecast remains provisional. Review it after the first target and resource experiment, especially for Rust implementation and VPS image delivery. A keyword is a design goal, not a finished architecture or a measured result.
