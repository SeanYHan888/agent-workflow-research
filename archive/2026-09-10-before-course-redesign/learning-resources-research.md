# Learning resources for the terminal agent workflow

Verified against public primary sources on 2026-09-10. Course listings establish advertised coverage, not completion or hands-on proficiency. Recommendations and proposed exercises below are project-specific judgments.

## JavaScript and TypeScript

Keep the two courses already selected, in sequence:

| Resource | Verified coverage | Recommended project connection |
| --- | --- | --- |
| [Boot.dev Learn JavaScript](https://www.boot.dev/courses/learn-javascript) | Lists 25 hours and 113 lessons. Covers language basics, objects/classes/prototypes, collections, errors, promises, async/await, event loop, runtimes and modules. Assumes prior programming basics. | Prioritize async, errors, modules and the event loop. Build a small CLI that reads a task file and writes a result. |
| [Boot.dev Learn TypeScript](https://www.boot.dev/courses/learn-typescript) | Lists 20 hours and 105 lessons. Covers types, functions, unions, collections, interfaces, narrowing, classes, utility/conditional types, generics and local development. Explicitly requires JavaScript fundamentals first. | Model tasks and agent events as discriminated unions; define one typed adapter contract for Claude Code and Codex. |

Those advertised hours are content estimates, not a personal completion schedule. Neither public chapter list establishes full coverage of terminal process orchestration. Add focused practice with Node.js subprocesses: `spawn` versus `exec`, stdout/stderr streaming, exit versus close, working directory/environment, cancellation, and child-process lifecycle. Node's documentation explains that subprocess pipes have bounded capacity and that failing to consume output can block the child. This directly matters for agent adapters. [Node.js child-process documentation](https://nodejs.org/api/child_process.html)

Suggested language checkpoint: write and explain a plain TypeScript adapter that starts a harmless local process, streams output, preserves its exit result, times out, and cleans up. Use fake workers before connecting paid model calls. This is an exercise recommendation, not course content.

## Effect: useful later, optional now

Effect fits problems this project may encounter: typed failure handling, retries/timeouts, bounded concurrency, resource cleanup, runtime validation, logging and streams with backpressure. Those are documented capabilities. [Effect guides](https://effect.website/docs/v3/getting-started)

Recommendation: learn JavaScript and TypeScript first, implement one working adapter with ordinary async code, then refactor only that adapter into Effect as a comparison. Evaluate whether cancellation, error handling and cleanup become easier to explain and test. Adopt it when the improvement is concrete. It is not a prerequisite for learning agent loops or building the first workflow.

Version caution: the live homepage currently promotes **Effect 4.0 release candidate** and `effect@rc`, while the older getting-started URL redirects to **v3** docs. Pin a chosen version and use matching documentation; do not mix examples across generations. Recheck the release state when starting the exercise. [Effect homepage](https://effect.website/), [versioned guides](https://effect.website/docs/v3/getting-started)

## Bash

Keep [Dave Eddy's ysap Bash course](https://course.ysap.sh/). Its published chapters include file operations/permissions, input/output, functions, conditions, loops, arrays, substitutions, text tools, arguments, pipe status, expansions, signal traps, named pipes and TTY detection. These align closely with launcher scripts and terminal integration. The page links [its source repository](https://github.com/bahamas10/bash-course). It also contains a “Coming Soon” notice alongside full-video links and timestamps, so the public page alone is not verification of video playback.

Recommendation: first use chapters 1–7, then signal traps and TTY detection. Build a launcher that accepts arguments, preserves spaces, captures logs and propagates exit status. Keep orchestration state and complex scheduling in TypeScript; use Bash for small process and environment tasks. Learn Bash explicitly even if the interactive shell is zsh, and check the Bash version used for each lab.

## One main Linux course

Choose **[Linux Foundation: Introduction to Linux (LFS101)](https://training.linuxfoundation.org/training/introduction-to-linux/)** as the main foundation. Its current listing is free, self-paced, beginner-oriented and includes hands-on labs; it advertises 60 hours of material and 90 days of online access. The outline includes startup, command-line operations, documentation, processes, files, user environment, text processing, networking, Bash and local security. Check enrollment terms when beginning.

For this project, prioritize chapters 3, 7–16 and 18. Skim GUI applications and printing unless personally useful. This is a recommendation for studying the course, not an alternative official syllabus. Its public outline does **not** establish complete coverage of agent service supervision, SSH operations, containers, resource limits or process-group cancellation. No single introductory course should be treated as “everything needed.”

Use one disposable Linux VM or an existing explicitly designated Linux development machine for the Linux labs. Keep macOS as the daily terminal. A full Linux environment makes startup, service supervision and Linux process behavior observable; do not assume macOS terminal familiarity verifies those skills.

## Focused Linux gaps and evidence of completion

Treat these as short project labs, not another list of courses. Consult only the matching official reference when a lab needs it.

| Competency | Evidence to produce | Reference |
| --- | --- | --- |
| Files, permissions, ownership, environment | Run a worker as an ordinary user with a known working directory; explain a permission failure and repair the specific cause. | LFS101 foundation above |
| Processes, signals, pipes and exit status | Inspect a worker's process tree; handle interruption and timeout; verify no child worker remains. | ysap course and Node subprocess docs above |
| SSH and packages | Connect to the designated lab host, transfer a task/result, install a required package and record its version. | [Ubuntu OpenSSH](https://ubuntu.com/server/docs/how-to/security/openssh-server/), [package management](https://ubuntu.com/server/docs/how-to/software/package-management/) |
| Networking | Explain DNS, IP, ports and loopback; diagnose a refused connection separately from name-resolution failure. | [Ubuntu networking concepts](https://ubuntu.com/server/docs/explanation/networking/networking-key-concepts/) |
| Services and logs | Run a harmless worker under systemd; stop/restart it and locate its logs. | Official systemd manual sources: [service units](https://github.com/systemd/systemd/blob/main/man/systemd.service.xml), [journalctl](https://github.com/systemd/systemd/blob/main/man/journalctl.xml) |
| Resource limits | Apply a small worker memory/CPU/task budget; explain the observed termination or throttling. | [systemd resource-control manual source](https://github.com/systemd/systemd/blob/main/man/systemd.resource-control.xml) |
| Containers | Package the worker, choose its mounted directories and ports, inspect logs, apply CPU/memory limits and remove the container. | [Docker getting started](https://docs.docker.com/get-started/), [resource constraints](https://docs.docker.com/engine/containers/resource_constraints/) |

## Recommended order

1. Begin JavaScript plus a small Bash/Linux practice track. Read agent-loop material concurrently.
2. Move to TypeScript after JavaScript foundations; build one local worker adapter.
3. Add the second worker, clear ownership of task directories, cancellation, logs and a human review step.
4. Use the Linux labs to make that same workflow portable and diagnosable.
5. Evaluate Effect using the existing adapter after the ordinary implementation is understood.

Progress should be recorded through working artifacts and explanations, alongside course completion. These recommendations do not imply that any course, lab or adapter has already been completed.

## System design and deeper JavaScript — added September 10, 2026

Recommendation: study selected system-design concepts alongside the agent implementation. The exercises below extend the original workflow and agent-construction goals. Full interview preparation and complete cover-to-cover reading of every supplied resource remain outside this project's estimate.

### Resource roles and audit

| Resource | Observed contents | Role in this project |
|---|---|---|
| [System Design Primer](</Users/seanmacbook/Self-learn/system-design-primer/README.md>) | Local `donnemartin/system-design-primer`, commit `b02784f`; explanations, tradeoffs, interview exercises and solutions | Main system-design reference: requirements, latency/throughput, storage, queues, backpressure, communication |
| [System Design 101](</Users/seanmacbook/Self-learn/system-design-101/README.md>) | Local `ByteByteGoHq/system-design-101`, commit `b28380a`; visual guide index and local Markdown under `data/guides/` | Short visual review after learning a concept; use retry, delivery, idempotency and observability guides |
| [SDE roadmap: System Design](https://github.com/aasthas2022/SDE-Interview-and-Prep-Roadmap/tree/main/System%20Design) | REST and microservices notes; Resources folder lists DDIA and Alex Xu PDFs | Supplemental question/reference bank. Use REST/interface questions when relevant; defer a broad microservices curriculum |
| [You Don't Know JS Yet](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/README.md>) | Local `getify/You-Dont-Know-JS`, commit `e3f784b`, second edition | Targeted depth alongside Boot.dev; not a replacement language curriculum |

Audit covered indexes and representative local guides, not every page or the linked PDFs. ByteByteGo's Markdown exists locally, but many embedded illustrations use remote asset URLs, so the checkout is not necessarily a complete offline visual library. Use the learning sources for explanations; verify implementation-specific behavior against the relevant official API/library documentation when building.

### System-design exercises — 20–30 additional hours

| When | Topic and reading | Apply it to the agent project |
|---|---|---|
| After the basic loop, Oct–Nov | Primer: requirements, constraints, latency vs throughput, communication | Draw human → Herdr → Pi → adapter → worker. Name who owns terminal lifetime, task state, and conversation history. Define success/failure and the adapter's input/output contract |
| Sessions and mini-agent, Nov–Jan | Primer: database and consistency sections; ByteByteGo: storage and event-sourcing overview | Compare JSONL and SQLite for task/session records. Explain how a task record and a transcript differ. Describe recovery after a write or process failure |
| First adapter, Dec–Jan | Primer: asynchronism, task queues, backpressure | Design a bounded task queue and a concurrency limit. Show how you detect a blocked worker and avoid unlimited output buffering |
| Two workers, Jan–Feb | ByteByteGo: retry strategies, delivery semantics, idempotency | Give each task an ID; simulate a lost response and a retry. Explain which operations are safe to retry and how to avoid repeating a completed side effect |
| Linux operation, Feb–Mar | ByteByteGo: logging, tracing, metrics; existing Linux security/process labs | Trace one task across coordinator and worker; diagnose a timeout from logs; state which files, credentials, and processes each worker can access |
| Final review | Revisit the requirements and measured bottlenecks | Present the design, one failure/recovery demonstration, and the tradeoffs you chose. Explain what would need to change for 2 workers versus 20 |

Local guide starting points: [retry strategies](</Users/seanmacbook/Self-learn/system-design-101/data/guides/how-do-we-retry-on-failures.md>), [delivery semantics](</Users/seanmacbook/Self-learn/system-design-101/data/guides/delivery-semantics.md>), [idempotency](</Users/seanmacbook/Self-learn/system-design-101/data/guides/top-6-cases-to-apply-idempotency.md>), [observability](</Users/seanmacbook/Self-learn/system-design-101/data/guides/logging-tracing-metrics.md>).

These are proposed design exercises, not claims that the initial implementation requires a message broker, database server, or microservices. Use the simplest design that meets the task. Large-scale feeds, CDNs, multi-region consensus, deep sharding, and exhaustive interview question banks are optional future study.

Produce a small architecture drawing, a task-state description, an adapter contract, and failure/recovery evidence as part of the existing build. Link them from Obsidian; keep progress there. The separate engineering-skill setup draft remains pending approval, so this addition does not create placeholder CONTEXT/ADR files or apply that setup.

### You Don't Know JS — 10–15 additional hours

Keep Boot.dev JavaScript → TypeScript as the main sequence. Pair selected reading with a small example you can explain:

1. **After basic JS syntax:** [Get Started](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/get-started/README.md>), chapters 1–3. Use chapter 2 as a review where it overlaps Boot.dev.
2. **When writing callbacks and modules:** [Scope & Closures](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/scope-closures/README.md>), chapters 1–3, 5, 7–8. Trace captured variables in a worker callback and explain module state; consult chapter 6 if scope exposure is unclear.
3. **When an example requires it:** [Objects & Classes](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/objects-classes/README.md>), especially chapter 4 on `this`; selected coercion sections from [Types & Grammar](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/types-grammar/README.md>). JavaScript runtime types/coercion are different from TypeScript's static type system.

The author's current second-edition index labels Objects & Classes draft-stable, Types & Grammar a rough draft, and Sync & Async / ES.Next & Beyond canceled. The local async folder contains placeholders. Use Boot.dev and [agent-learning chapter 11](</Users/seanmacbook/Self-learn/agent-learning/11-async-js.md>) for promises, async generators and cancellation. [Author's edition status](https://github.com/getify/You-Dont-Know-JS).

### Schedule effect

The additions are net new reading/design time; implementation and Linux exercises already budgeted elsewhere are not counted twice. Budget **30–45 extra hours**, working allocation **40** (25 system design + 15 JS depth). Full scope becomes **250–325 hours**, with a **300-hour / 30-week working plan** at the provisional 10 hours/week. Revised milestones are in ROADMAP.md. Reading every supplied resource would require a separate estimate.
