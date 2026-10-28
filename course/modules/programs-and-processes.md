# M2 — Write and control a program

M2 builds the first project-route artifact: **a controllable local runner**. The learner writes a JavaScript program for Node that reads a task file, starts a fixed harmless child process, reports what happened and stops that child on request. The same runner becomes the execution side of the M3 typed agent and is later adapted to real workers in M4 and supervised on Linux in M5. Language, async, error, file, stream, Bash and basic process/network concepts are taught when the runner needs them.

## Useful result

A bounded task runner: input file → validated task → fake worker → progress and a structured result file. It distinguishes failure modes rather than reporting "it broke".

**Observable acceptance:**
- A valid fixture produces a result.
- A malformed fixture produces an explained error.
- A missing executable, a nonzero exit and success are reported as three different outcomes.
- A record split across output chunks is reassembled correctly.
- Retained output stays within a stated limit.
- A slow fixture is cancelled, and the learner shows that the direct child stopped and its output closed.

The learner explains the order of events for one run. Arbitrary task commands, shell-string execution, process-tree cleanup (M4/M5) and web servers stay out of scope.

## Entry requirements

- M1 tool-cycle orientation. A language/process diagnostic decides the first lesson.
- [M11 E1/E2](engineering-practice.md) Git inspection and recovery begin alongside M2, before substantial edits. Their time is charged to M11.

## Checkpoints

These checkpoints elaborate the roadmap's M2 row: JS/TS, Node, async, errors, files, subprocesses, and basic Bash, process and network literacy, through a bounded task runner. They add no outcome and raise no depth.

| ID | Checkpoint | Observable evidence |
|---|---|---|
| M2.1 | Values, functions, modules and errors | The runner reads a task file. It reports a missing file, malformed JSON and a path containing spaces, each with an explained error. The learner traces argv → path → text → parsed value → output. |
| M2.2 | Async control | The learner predicts and then observes the output order of a small promise example. They trace one awaited read and show where a rejection is caught. They can tell callbacks, promises and emitted events apart in their own code. |
| M2.3 | Subprocess lifecycle | A fixed command is launched with an argument array. The learner distinguishes failed startup, stdout, stderr and nonzero exit, and explains why `exit` does not guarantee that all output was collected (`close` does). |
| M2.4 | Streams and bounded output | JSONL events are parsed correctly when one record spans chunks or two records share a chunk. Retained history has a stated limit and marks truncation. |
| M2.5 | Timeout, cancellation and checks | A slow fixture is cancelled or times out. The learner observes the exit signal and stream closure and states what this does *not* prove about descendants. Automated checks cover a failure, partial output and the timeout. |
| M2.6 | Bash, process and network literacy | A Bash launcher passes an argument with spaces intact, captures logs and propagates the runner's exit status. The learner inspects and signals the running process with `ps`/`kill`. They name host, port and loopback, and show an HTTP error status separately from a connection failure. Deeper DNS/TCP diagnosis is M5. |

## Lab sequence

Each increment extends the same runner. Follow the [session workflow](../../teaching/README.md#prepare-and-teach). The learner predicts and attempts first, and concepts or readings answer the question in front of them.

| Increment | Deliverable | Acceptance check | Learner's first action | Timebox |
|---|---|---|---|---:|
| 1. Task-file CLI | A CLI that reads a tiny fixture and prints a task summary | M2.1: a valid fixture and one malformed fixture are each predicted, run and explained | Sketch the data path from argv to output and mark every place it can fail | 4–6h |
| 2. Async probe | An annotated prediction and the observed output for one awaited read and one rejected read in the CLI | M2.2: explain how the resolved value reaches its consumer and where the rejection is handled | Write the expected output order before running | 1–2h |
| 3. Observable fake worker | The runner launches a fixed harmless command and records a structured outcome | M2.3: success, missing executable and nonzero-exit fixtures give three distinct, explained outcomes | Predict which Node event fires first in each of the three cases | 5–7h |
| 4. Controllable runner | Framed JSONL parsing, bounded retained output, cancellation and timeout, with checks | M2.4 and M2.5: split-record and oversized-output fixtures pass. A slow fixture is cancelled with exit and close observed. Tests cover failure, partial output and timeout. | Decide who owns the child when the caller cancels, and how to establish that it stopped | 5–7h |
| 5. Bash launcher | A launcher script around the runner, plus a short process-inspection log | M2.6 Bash/process: an argument with spaces arrives intact, the exit status matches, and a trapped INT/TERM is explained | Predict the exit status of a failing pipeline with and without `PIPESTATUS` | 2–4h |
| 6. One network request | One request made with `curl` and with Node to a local or public endpoint, in a success case and a failure case | M2.6 network: the learner says which layer reported an HTTP error status and which reported a connection failure | Predict both outcomes before running | 1–2h |

Increments 1, 3 and 4 match the runner slices in the [project catalog](../PROJECTS.md#select-the-next-hands-on-slice). Prepare only the next ready increment. A useful failure with a reasoned next experiment can close a session.

## Failure experiments

- Missing file, empty file, malformed JSON, a valid JSON value of the wrong shape, and a path with spaces.
- A missing executable: the `error` event versus a nonzero `exit`. A child that writes only to stderr.
- A child that writes a lot while nothing reads the pipe. Node documents that the bounded pipe capacity can block the child.
- One JSONL record split across two chunks, and two records in one chunk.
- `exit` arriving before `close`. A cancel arriving after the child already exited.
- A cancelled child that started its own grandchild. Observe whether it survives; process-tree cleanup is assessed in M4/M5.
- A reading-based case: in nanocode's `bash()`, why can the `readline` loop block before `wait(timeout=30)` is reached? Compare it with s01's `subprocess.run(..., timeout=120)`.

## Materials

| Source | Role | Supports |
|---|---|---|
| [Boot.dev Learn JavaScript](https://www.boot.dev/courses/learn-javascript) | Required completion goal, charged to M2. Prioritize errors, modules, promises, async/await and the event loop. | M2.1, M2.2 |
| [Node Learn: introduction](https://nodejs.org/learn/getting-started/introduction-to-nodejs), [run scripts](https://nodejs.org/learn/command-line/run-nodejs-scripts-from-the-command-line), [reading files](https://nodejs.org/learn/manipulating-files/reading-files-with-nodejs) | Entry point, argv/cwd/environment, file I/O | M2.1 |
| [Blocking vs non-blocking](https://nodejs.org/learn/asynchronous-work/overview-of-blocking-vs-non-blocking), with the Event Loop and Event Emitter guides from the Learn index | Async model behind the runner | M2.2 |
| [Node `child_process` API](https://nodejs.org/api/child_process.html): spawn/execFile, error/exit/close, signal and timeout sections | Subprocess lifecycle and cancellation reference. Match it to the installed Node version. | M2.3, M2.5 |
| [How to use streams](https://nodejs.org/learn/modules/how-to-use-streams), [Backpressuring in streams](https://nodejs.org/en/learn/modules/backpressuring-in-streams) | Framing and bounded consumption | M2.4 |
| [Using the test runner](https://nodejs.org/learn/test-runner/using-test-runner) | Built-in checks for the runner | M2.5 |
| [YDKJS Get Started](../../materials/sources/javascript/you-dont-know-js/get-started/README.md), chapters 1–3; [Scope & Closures](../../materials/sources/javascript/you-dont-know-js/scope-closures/README.md), chapters 1–3, 5 and 7–8 (`044120ef5556`) | Selected depth alongside Boot.dev: closures in callbacks and module state | M2.1, M2.2 |
| [YSAP Bash course](https://course.ysap.sh/), with the pinned notes on [I/O](../../materials/sources/linux/bash-course/notes/03-05-io/readme.md), [arguments](../../materials/sources/linux/bash-course/notes/06-00-bash-arguments/readme.md), [`PIPESTATUS`](../../materials/sources/linux/bash-course/notes/06-01-pipestatus/readme.md) and [trapping signals](../../materials/sources/linux/bash-course/notes/13-00-trap-signals/readme.md) (`0fb288afb1a3`) | Launcher, exit status and signals. Run labs explicitly with Bash. | M2.6 |
| [Ubuntu networking key concepts](https://ubuntu.com/server/docs/explanation/networking/networking-key-concepts/) | Host, port and loopback vocabulary only | M2.6 |
| [nanocode `bash()`](../../materials/sources/agents/nanocode/nanocode.py), lines 78–97 (`b009d3dbedf1`); [s01 `run_bash()`](../../materials/sources/agents/learn-claude-code/s01_agent_loop/code.py), lines 71–84 | Two harness subprocess patterns to critique, not copy | M2.3–M2.5 |

The [resource catalog](../../materials/resource-catalog.md#nodejs--required-runtime-material) records why these were selected. Use ES modules and promise-based file APIs for the build, and explain CommonJS or callback syntax when it appears in readings. Do not assign whole API references as reading.

## Hours

[WORKLOAD](../WORKLOAD.md) estimates **25–45 directed hours** for M2. That covers JS/Node/Bash completion and the runner. TypeScript language work is charged to M3, although it also satisfies the "JS/TS" part of M2. The increments above total about 18–28h. The remainder covers Boot.dev JavaScript completion, YSAP selections and assessment, but it is not proof that all course work fits: diagnose first and reforecast from observed pace. M11 E1/E2 time is deducted from the same week's allocation rather than added. Keep each execution slice within 6–9 project hours and 21 days.

## Assessment

Use the [shared rubric](../ASSESSMENT.md). The evidence is the learner-authored runner with its failure fixtures and checks, an end-to-end explanation of one run, and an unfamiliar change or failure. For example, the teacher might introduce a new failure mode or change the output framing, and the learner predicts before running. A passing generated script or a finished Boot.dev badge does not establish M2 by itself. M18 AS2 and M19 MC1 reuse M2 file, process and stdio evidence.
