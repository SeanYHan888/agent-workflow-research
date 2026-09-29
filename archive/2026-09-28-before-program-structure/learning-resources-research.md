# Learning resources for the terminal agent workflow

Resource audit dated 2026-09-10; this is a source catalog, not the syllabus. Follow [ROADMAP.md](ROADMAP.md) for the redesigned course and [material-versions.md](material-versions.md) for the subsequent Git refresh. The generated agent-learning chapters are not required or authoritative.

Verified against public primary sources on 2026-09-10. Course listings establish advertised coverage, not completion or hands-on proficiency. Recommendations and proposed exercises below are project-specific judgments.

## JavaScript and TypeScript

Keep the two courses already selected, in sequence:

| Resource | Verified coverage | Recommended project connection |
| --- | --- | --- |
| [Boot.dev Learn JavaScript](https://www.boot.dev/courses/learn-javascript) | Lists 25 hours and 113 lessons. Covers language basics, objects/classes/prototypes, collections, errors, promises, async/await, event loop, runtimes and modules. Assumes prior programming basics. | Prioritize async, errors, modules and the event loop. Build a small CLI that reads a task file and writes a result. |
| [Boot.dev Learn TypeScript](https://www.boot.dev/courses/learn-typescript) | Lists 20 hours and 105 lessons. Covers types, functions, unions, collections, interfaces, narrowing, classes, utility/conditional types, generics and local development. Explicitly requires JavaScript fundamentals first. | Model tasks and agent events as discriminated unions; define one typed adapter contract for Claude Code and Codex. |

Those advertised hours are content estimates, not a personal completion schedule. Neither public chapter list establishes full coverage of terminal process orchestration. Add focused practice with Node.js subprocesses: `spawn` versus `exec`, stdout/stderr streaming, exit versus close, working directory/environment, cancellation, and child-process lifecycle. Node's documentation explains that subprocess pipes have bounded capacity and that failing to consume output can block the child. This directly matters for agent adapters. [Node.js child-process documentation](https://nodejs.org/api/child_process.html)

Suggested language checkpoint: write and explain a plain TypeScript adapter that starts a harmless local process, streams output, preserves its exit result, times out, and cleans up. Use fake workers before connecting paid model calls. This is an exercise recommendation, not course content.

## Node.js — required runtime material

Added September 10, 2026. **Main reading: [Node.js Learn](https://nodejs.org/learn/getting-started/introduction-to-nodejs)**, the official explanatory guides. **Implementation reference: [Node.js API documentation](https://nodejs.org/api/)**, especially [child_process](https://nodejs.org/api/child_process.html). These are live documentation, not a single graded course. Our project supplies the practice sequence and checkpoints below. No additional paid course is required for this module.

JavaScript is the language; Node.js is a runtime that executes it outside the browser and provides access to files, processes and other system facilities. TypeScript adds static checking; learning it does not replace learning the Node APIs used by a worker adapter.

### Placement and prerequisites

Begin runtime/CLI basics in **Step 2** after JS functions, objects, errors and modules. Learn promises/async in Boot.dev before the asynchronous I/O exercises. Node practice and the remaining JS course can overlap; completing TypeScript is not required to begin. Carry the same runner into Step 3's typed agent. Revisit streaming/cancellation in Step 5 for real worker integration; Linux process-tree recovery remains Step 6.

This supplies material for the Node work already in the roadmap, rather than adding another independent course or resetting the active Step 1. Expand these proposed exercises only when their step is active.

| Topic and official reading | Why it matters | Proposed project checkpoint |
|---|---|---|
| Runtime and CLI: [Introduction](https://nodejs.org/learn/getting-started/introduction-to-nodejs), [run scripts](https://nodejs.org/learn/command-line/run-nodejs-scripts-from-the-command-line); use the Learn index's npm and environment-variable guides as needed | Know how code starts and receives its working environment | Run a small script with an argument and nonsecret environment setting; explain the entry point, cwd and package scripts |
| Files and modules: [Reading files](https://nodejs.org/learn/manipulating-files/reading-files-with-nodejs), plus File Paths and Writing Files from the same section | Tools inspect a workspace and persist task/results | Load a task JSON file and write a result; explain a missing file, malformed JSON and a path with spaces |
| Async I/O: [Blocking vs non-blocking](https://nodejs.org/learn/asynchronous-work/overview-of-blocking-vs-non-blocking), then the Learn index's Event Loop and Event Emitter guides | Keep the runner responsive while waiting for I/O | Predict output order, trace an awaited read and handle a rejected operation; distinguish callbacks, promises and emitted events |
| Subprocesses: [child_process](https://nodejs.org/api/child_process.html), selected spawn/execFile/exec and error/exit/close sections | Run a worker program and collect its result | Launch a harmless fake worker with an argument array; distinguish stdout, stderr, failed startup and nonzero exit; wait for output completion |
| Streams: [How to use streams](https://nodejs.org/learn/modules/how-to-use-streams), [Backpressuring in Streams](https://nodejs.org/en/learn/modules/backpressuring-in-streams) | Workers emit incremental output that may outpace the reader | Consume fake JSONL events when one record spans chunks or multiple records share a chunk; retain a bounded output history |
| Cancellation and verification: child_process signal/timeout sections above; [Using the test runner](https://nodejs.org/learn/test-runner/using-test-runner) and Debugging from the Learn index | An adapter must detect failure and stop work predictably | Cancel a slow fake worker, observe its exit and output closure, and write meaningful checks for failure, partial output and timeout |

**Module deliverable:** a small local task runner that reads an input file, starts a fake worker, reports progress and writes a structured result. First build the simplest successful path; add each failure case after its mechanism is understood. Reuse the runner when introducing TS types and later Claude Code/Codex instead of starting another project.

Teaching choices: use ES modules and promise-based filesystem examples for the main build; explain CommonJS/callback syntax when encountered in readings. Match API documentation to the selected runtime version when implementing. Use the project's existing test tooling where present; the built-in test runner is enough for a standalone initial lab. This planning update does not install or change Node or package managers.

A process exit alone does not establish that all output has been collected: the documented `close` event follows process termination and closure of its stdio streams. Likewise, sending a cancellation signal does not establish that every descendant stopped. Observe the direct child in Step 2, then verify process-tree cleanup during worker/Linux integration. These are separate checkpoints, not promises that AbortController handles the entire lifecycle automatically.

Read the guides in short selections, then predict/run/change/explain one example. Avoid assigning the whole API reference as a lesson. HTTP client basics can be added at the provider boundary; an Express server, full web backend, native addons and advanced profiling are outside this module's initial scope.

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

### Small Agent Runtime — added September 24, 2026

These required Section 6 checkpoints extend the existing runner and worker adapter. Keep one project and use references as needed; detailed lessons and implementation follow learner attempts. Progress belongs in the existing Obsidian Linux project. The 30-hour allocation and recorded dates are provisional and must be reassessed at entry now that scope has expanded.

| Checkpoint | Evidence to produce | Focused reference |
| --- | --- | --- |
| Linux command practice | Explain files, users/groups and least privilege using `id`, `sudo`, `chmod`, `chown`; inspect and interrupt a harmless process with `ps`, `top`, `kill`, signals and `jobs`/`fg`/`bg`. | Selected LFS101/YSAP above; installed Linux command manuals |
| Networking commands | Explain IP, ports, localhost, DNS and HTTP; use `curl`, `ss` or `lsof`, and `getent hosts` to distinguish a missing listener, failed name lookup and an HTTP error. | Ubuntu networking reference above; installed command manuals |
| Periodic scheduling | Schedule a harmless health/status script with a user crontab. Specify environment, absolute paths, working directory and log output; observe execution, prevent overlapping runs, then remove the lab entry. Explain scheduling versus keeping a service alive. | [crontab manual](https://man7.org/linux/man-pages/man5/crontab.5.html); check the lab host's cron implementation |
| Docker fundamentals | Explain image versus container, writable layers, bind mounts versus named volumes and network/port mappings. Reuse the existing packaging and CPU/memory lab. | Docker getting-started and resource-constraint references above |
| Isolation and least privilege | Explain how namespaces separate process/resource views and cgroups account for and limit resources. Run a task as a non-root user with narrow mounts, a read-only root filesystem and CPU/memory/PID limits; demonstrate a denied write and inspect configured limits. | [namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html), [cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html), [Docker security](https://docs.docker.com/engine/security/) |
| Network restrictions | Run a fixture task with networking disabled and verify outbound access fails. For a real provider-backed task, define required destinations and demonstrate an enforced egress policy that permits them and blocks unrelated destinations; document where enforcement lives. | [Docker none network](https://docs.docker.com/engine/network/drivers/none/); selected lab host firewall/proxy documentation when implementing |
| Redis + RQ workers | Enqueue a fixed task function, return a job ID, retrieve status/result, bound concurrency and admission, and demonstrate a capped retry plus duplicate-submission handling. Explain what survives worker/API restart and what Redis persistence/result retention actually preserve. | [RQ queues](https://python-rq.org/docs/), [RQ retries](https://python-rq.org/docs/exceptions/), [Redis security](https://redis.io/docs/latest/operate/oss_and_stack/management/security/) |

Build this on one designated Linux lab host:

```text
FastAPI: POST /tasks → job ID; GET /tasks/{id} → status/result
    ↓
Redis + RQ task queue
    ↓
trusted worker adapter
    ↓
per-task Docker container invoking the existing runner/agent
    ↓
task-ID logs + result + deadline + CPU/memory/PID limits
```

Use a thin Python API/queue wrapper around the existing agent command. Start with one worker and a harmless fixture, then a bounded agent task, then the planned second worker with separate workspaces. RQ is the initial queue choice; Celery is optional follow-on reading, not another required implementation. API source: [FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/); compare [in-process background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) with the separate worker lifecycle.

The trusted adapter owns container launch and cleanup. Task containers receive only their intended workspace and credentials, never the host Docker socket. Keep Redis and the initial API local/private; accept validated task inputs for a fixed handler rather than arbitrary commands or Python functions. A container is a bounded lab isolation mechanism, not proof that arbitrary hostile code is safe. The offline fixture uses no network; the provider-backed task needs the separately verified egress policy.

Completion requires a successful task trace and injected failures: nonzero exit, timeout, a resource-limit failure, worker interruption and duplicate submission. Capture job state, correlated logs and result evidence; verify that cancellation/timeout removes the task container and descendants. Kill the worker during a task and demonstrate recovery that finds orphaned containers and reconciles uncertain results before retrying. An RQ timeout alone does not establish container cleanup or exactly-once effects. Reuse the systemd/journalctl lab to supervise the API and worker, and the cron lab for a status check.

Keep basic queues, retries, idempotency and backpressure in this build. Study distributed deployment and Kubernetes only after this single-machine runtime works and measurements show why more infrastructure is needed. This addition records study scope, not completed implementation or learning.

## Course sequence and progress

Use the dependency-based sequence and opening block in [ROADMAP.md](ROADMAP.md). The user can write small Python scripts but is unfamiliar with async, subprocesses and larger codebases. Build those prerequisites before broad source reading. Existing files and advertised course hours do not establish learning or a personal schedule. Progress belongs in Obsidian.

## System design and deeper JavaScript — added September 10, 2026

Recommendation: study selected system-design concepts alongside the agent implementation. The exercises below extend the original workflow and agent-construction goals. Full interview preparation and complete cover-to-cover reading of every supplied resource remain outside the core course scope.

### Resource roles and audit

| Resource | Observed contents | Role in this project |
|---|---|---|
| [System Design Primer](</Users/seanmacbook/Self-learn/system-design-primer/README.md>) | Local `donnemartin/system-design-primer`, commit `ae9bbd7`; explanations, tradeoffs, interview exercises and solutions | Main system-design reference: requirements, latency/throughput, storage, queues, backpressure, communication |
| [System Design 101](</Users/seanmacbook/Self-learn/system-design-101/README.md>) | Local `ByteByteGoHq/system-design-101`, commit `b28380a`; visual guide index and local Markdown under `data/guides/` | Short visual review after learning a concept; use retry, delivery, idempotency and observability guides |
| [SDE roadmap: System Design](https://github.com/aasthas2022/SDE-Interview-and-Prep-Roadmap/tree/main/System%20Design) | REST and microservices notes; Resources folder lists DDIA and Alex Xu PDFs | Supplemental question/reference bank. Use REST/interface questions when relevant; defer a broad microservices curriculum |
| [You Don't Know JS Yet](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/README.md>) | Local `getify/You-Dont-Know-JS`, commit `044120e`, second edition | Targeted depth alongside Boot.dev; not a replacement language curriculum |

Audit covered indexes and representative local guides, not every page or the linked PDFs. ByteByteGo's Markdown exists locally, but many embedded illustrations use remote asset URLs, so the checkout is not necessarily a complete offline visual library. Use the learning sources for explanations; verify implementation-specific behavior against the relevant official API/library documentation when building.

### System-design exercises — introduced by the build

| When | Topic and reading | Apply it to the agent project |
|---|---|---|
| After the basic loop | Primer: requirements, constraints, latency vs throughput, communication | Draw human → Herdr → Pi → adapter → worker. Name who owns terminal lifetime, task state, and conversation history. Define success/failure and the adapter's input/output contract |
| Sessions and small typed agent | Primer: database and consistency sections; ByteByteGo: storage and event-sourcing overview | Compare JSONL and SQLite for task/session records. Explain how a task record and a transcript differ. Describe recovery after a write or process failure |
| First adapter | Primer: asynchronism, task queues, backpressure | Design a bounded task queue and a concurrency limit. Show how you detect a blocked worker and avoid unlimited output buffering |
| Two workers | ByteByteGo: retry strategies, delivery semantics, idempotency | Give each task an ID; simulate a lost response and a retry. Explain which operations are safe to retry and how to avoid repeating a completed side effect |
| Linux operation | ByteByteGo: logging, tracing, metrics; existing Linux security/process labs | Trace one task across coordinator and worker; diagnose a timeout from logs; state which files, credentials, and processes each worker can access |
| Final review | Revisit the requirements and measured bottlenecks | Present the design, one failure/recovery demonstration, and the tradeoffs you chose. Explain what would need to change for 2 workers versus 20 |

Local guide starting points: [retry strategies](</Users/seanmacbook/Self-learn/system-design-101/data/guides/how-do-we-retry-on-failures.md>), [delivery semantics](</Users/seanmacbook/Self-learn/system-design-101/data/guides/delivery-semantics.md>), [idempotency](</Users/seanmacbook/Self-learn/system-design-101/data/guides/top-6-cases-to-apply-idempotency.md>), [observability](</Users/seanmacbook/Self-learn/system-design-101/data/guides/logging-tracing-metrics.md>).

These are proposed design exercises, not claims that the initial implementation requires a message broker, database server, or microservices. Use the simplest design that meets the task. Large-scale feeds, CDNs, multi-region consensus, deep sharding, and exhaustive interview question banks are optional future study.

Produce a small architecture drawing, a task-state description, an adapter contract, and failure/recovery evidence as part of the existing build. Link them from Obsidian; keep progress there. The separate engineering-skill setup draft remains pending approval, so this addition does not create placeholder CONTEXT/ADR files or apply that setup.

### You Don't Know JS — selected depth

Keep Boot.dev JavaScript → TypeScript as the main sequence. Pair selected reading with a small example you can explain:

1. **After basic JS syntax:** [Get Started](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/get-started/README.md>), chapters 1–3. Use chapter 2 as a review where it overlaps Boot.dev.
2. **When writing callbacks and modules:** [Scope & Closures](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/scope-closures/README.md>), chapters 1–3, 5, 7–8. Trace captured variables in a worker callback and explain module state; consult chapter 6 if scope exposure is unclear.
3. **When an example requires it:** [Objects & Classes](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/objects-classes/README.md>), especially chapter 4 on `this`; selected coercion sections from [Types & Grammar](</Users/seanmacbook/Self-learn/You-Dont-Know-JS/types-grammar/README.md>). JavaScript runtime types/coercion are different from TypeScript's static type system.

The author's current second-edition index labels Objects & Classes draft-stable, Types & Grammar a rough draft, and Sync & Async / ES.Next & Beyond canceled. The local async folder contains placeholders. Use Boot.dev for promises and the event loop; add small Node.js async, streaming and cancellation exercises using official documentation. The generated agent-learning chapter is not a required source. [Author's edition status](https://github.com/getify/You-Dont-Know-JS).

### Schedule status

The earlier additive hour estimates and calendar assignments are superseded. They are preserved in [the historical research snapshot](archive/2026-09-10-before-course-redesign/learning-resources-research.md). Resource quantity does not determine course scope or duration. The user confirmed 10 hours/week and requested compact pacing. ROADMAP.md now targets 160 hours / 16 weeks, ending January 3, 2027. Check actual pace September 30; source quantity does not impose reading time.

## GUI and team projects integrated — September 10, 2026

These are curriculum decisions based on a focused primary-source check, not hands-on product validation.

- **Paseo:** the current [supported-agent page](https://paseo.sh/agents) lists Claude Code, Codex, Pi and OMP. Use it to compare human steering/review/reconnect with the terminal baseline; supported agents do not establish live takeover of a Herdr-owned session.
- **T3 Code:** the [README](https://github.com/pingdotgg/t3code) describes a harness control surface for desktop/web/mobile. The [architecture document](https://github.com/pingdotgg/t3code/blob/main/AGENTS.md) describes a Node WebSocket server, typed contracts and provider adapters; the server uses Effect and web uses React. Read the [internals overview](https://github.com/pingdotgg/t3code/blob/main/docs/internals/overview.md), then trace one request and its returned events at a recorded source revision. This motivates placing the source lab after JS/TS and Pi architecture. A narrow Effect/React reading bridge is included; no full frontend rebuild. Its current documented provider list should not be read as Pi support.
- **OMP:** current [task documentation](https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md) describes subagent task batches and optional isolation. It is a candidate existing harness for a team, not an assumed plugin for upstream Pi. Compare ownership, failure behavior and review evidence on a small trial.
- **Orca:** retained as a candidate from the existing user project and earlier research. The [orchestration page](https://www.onorca.dev/docs/cli/orchestration) returned a fetch error twice in this update; no fresh API or reliability claim is made. Recheck current documentation and launch behavior before use.

The user selected an existing-tools team first. Reuse earlier adapter/worktree/recovery labs; test a coordinator-led feature with two writers and a review pass, then repeat a comparable trial. Record candidate revision, integrated checks, unresolved findings, human interventions and review time. Full custom orchestration infrastructure and distributed fleets require a later project.

Current compact allocations: GUI 10 hours, existing-tool team capstone 30 hours. The full course targets 160 hours at the user’s requested faster pace. Earlier 360-hour estimates are archived; current dates are in ROADMAP.md and the Obsidian overview. Source-reading and task-completion states remain unchanged.

## nanocode and mini-swe-agent — added September 15, 2026

The user requested both repositories in the course. Inspected their README files and the selected source below; this was a source review, not a live provider or benchmark run. Keep Boot.dev JS/TS and the same evolving TypeScript build. Assign these as bounded comparative readings in the existing stages.

| Source and inspected revision | Read in order | Course placement and evidence |
|---|---|---|
| [nanocode](https://github.com/1rgs/nanocode/blob/b009d3dbedf14795a5c10804a5455386563f4b5b/nanocode.py) · master `b009d3dbedf14795a5c10804a5455386563f4b5b` | `TOOLS` → `make_schema` → `run_tool` → `main` inner loop; inspect `read` and `edit` as needed | Section 3, 60 minutes within its 4-hour review allocation. Trace a read request/result ID, failed dispatch and stopping; compare with s02 and identify one improvement for your typed agent |
| [mini-swe-agent agent](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py) · main `04d809ceab9df28f9adaed044884180159172930` | `DefaultAgent.run`, `step`, `query`, `execute_actions`, then `save` | Section 4, 90 minutes within its 20 hours, replacing part of the broad source tour. Draw message ownership and loop/model/environment boundaries, explain a limit/exit path, then map those boundaries onto your TS agent and Tau/Pi |
| [mini-swe-agent model](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/models/litellm_model.py) · same revision | `LitellmModel._query`, `query`, `_parse_actions`, `format_observation_messages` | Follow one action and returned observation across the provider boundary |
| [mini-swe-agent environment](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/local.py) · same revision | `LocalEnvironment.execute`, `_check_finished`; `_run` after process prerequisites | Locate execution, command output, completion signaling and timeout cleanup |

### Why these selections

**nanocode:** one file exposes six tools and generates their API schemas from a shared registry. `run_tool` converts exceptions into text; the inner loop pairs results with tool-use IDs and stops when no tool results were produced. Schemas sent to a provider do not establish local runtime input validation. History here is an in-memory list; do not equate it with the saved-history/resume checkpoint required in our build. These observations make it a useful comparison after the tiny dispatcher.

**mini-swe-agent:** the inspected v2 implementation separates the loop from model and environment objects. The loop appends messages, checks configured limits and saves a trajectory; an exit-role message ends the run. The selected LiteLLM adapter sends a bash tool schema and parses tool calls, so do not teach the README's broad no-tool-calling claim as a description of this adapter. The local environment starts command processes and recognizes an explicit completion marker. This supplies a small architecture example before the larger Pi source tour.

### Teaching boundaries

Use a scripted response or paper trace for the first checkpoint; live API access is unnecessary. If a later lab runs either agent, select the provider and a disposable fixture repository at that point. nanocode's shell reader can block before reaching its `wait(timeout=30)` call, so that code is not a reliable whole-command timeout pattern. Compare process behavior using the existing Node lab. mini-swe-agent's local environment executes on the host; an environment interface alone is not isolation.

Source-reading links are pinned to the inspected commits; revisit symbols if updating revisions. No clone, package installation, paid run, separate Python rebuild, extra phase or completion claim is part of this addition. Keep the current JS/Node stage, dates and 160-hour forecast. Progress and the two new reading checkpoints belong in the existing Section 3 and Section 4 Obsidian projects.

## Claude, agent source and inference — added September 28, 2026

The [expanded research plan](expanded-research-plan.md) contains the new resource selection, prerequisite graph and lab checkpoints. Official course listings and repository/documentation entry points were checked on September 28; proposed lessons are distinguished from executed code traces. The additions are self-paced and extend beyond the historical 160-hour foundation estimate.

- Claude: official Academy subagents, skills, Claude Code 101/In Action, Platform 101, Building with the Claude API, and introductory/advanced MCP; context and agent architecture companion articles.
- Agent source: preserve earlier nanocode/mini-swe-agent pins and Tau/Pi lessons; add Codex internals with a Rust bridge, optional OpenCode, and the unverified local Claude Code snapshot as its own investigation.
- Inference: PyTorch/Hugging Face foundations, selected Stanford CS336 lectures, local nanochat, FlashAttention and PagedAttention papers, vLLM docs, and optional nano-vllm, llama.cpp/MLX and SGLang comparisons.

New source lessons pin their revisions before tracing. No full source audit, local build or benchmark is implied by inclusion in this catalog. See the plan's local-source provenance and hardware sections for what was actually checked.
