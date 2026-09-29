---
title: Coding Agent Course — Material Shelf
created: 2026-09-11
tags:
  - learning/coding-agents
---
# The materials we will use

[[Notes/Coding Agent Course/00 Start Here|Start Here]] · [[Notes/Coding Agent Course/02 Study Route|Study route]]

These selections preserve the September 10 course agreement. Each resource has a specific job. Use the assigned portions when their stage begins; only Boot.dev JS and TS retain whole-course completion tasks.

## Language and runtime

| Material | Use it for | Selection |
|---|---|---|
| [Boot.dev JavaScript](https://www.boot.dev/courses/learn-javascript) | Main JS instruction and practice | Start at Variables; work through the course and apply functions, objects, errors, modules and async in Stage 2 |
| [Boot.dev TypeScript](https://www.boot.dev/courses/learn-typescript) | Main type-system instruction and practice | Stage 3 after JS foundations; apply unions, narrowing and interfaces to the same program |
| [Node.js Learn](https://nodejs.org/learn/getting-started/introduction-to-nodejs) | Explain the runtime and its mechanisms | Stage 2: CLI → files → async I/O → processes → streams → cancellation |
| [Node API reference](https://nodejs.org/api/) | Check exact implementation behavior | Use the API version matching the runtime selected for the lab |
| [You Don't Know JS Yet — local](file:///Users/seanmacbook/Self-learn/You-Dont-Know-JS/README.md) | Resolve a specific JS misunderstanding | Get Started 1–3; Scope & Closures 1–3, 5, 7–8 as needed. Defer deeper coercion/this reading until a concrete example needs it |

Node reading sequence, after the relevant JS prerequisites:

1. [Introduction](https://nodejs.org/learn/getting-started/introduction-to-nodejs) and [running scripts](https://nodejs.org/learn/command-line/run-nodejs-scripts-from-the-command-line): arguments, working directory and environment.
2. [Reading files](https://nodejs.org/learn/manipulating-files/reading-files-with-nodejs): load task JSON, explain paths and missing/malformed input.
3. [Blocking and non-blocking](https://nodejs.org/learn/asynchronous-work/overview-of-blocking-vs-non-blocking): predict order and explain waiting after learning promises.
4. [Child processes](https://nodejs.org/api/child_process.html): selected spawn/execFile/exec and error/exit/close sections; launch a fake worker and collect its result.
5. [Streams](https://nodejs.org/learn/modules/how-to-use-streams) and [backpressure](https://nodejs.org/en/learn/modules/backpressuring-in-streams): partial records, incremental output and bounded retention.
6. Child-process signal/timeout sections and [test runner](https://nodejs.org/learn/test-runner/using-test-runner): explain failure and verify cancellation.

The classroom's [Node teaching sequence](file:///Users/seanmacbook/Projects/agent-workflow-research/learning-resources-research.md) records the fuller lab plan. The first deliverable is one fake-worker task runner, reused for TypeScript and the real worker adapter.

## Agent mechanisms and source reading

| Material | Use it for | Selection |
|---|---|---|
| [learn-claude-code s01](file:///Users/seanmacbook/Self-learn/learn-claude-code/s01_agent_loop/code.py) | First compact loop to trace | `agent_loop()`, lines 87–117 at local revision `0dcafa2ae053`; first assignment |
| [learn-claude-code s02](file:///Users/seanmacbook/Self-learn/learn-claude-code/s02_tool_use/code.py) | Compare tool registration and dispatch | After the first explanation and fixture-reading exercise; later chapters only by mechanism |
| [nanocode](https://github.com/1rgs/nanocode/blob/b009d3dbedf14795a5c10804a5455386563f4b5b/nanocode.py) | Compact multi-tool implementation | Stage 3: `TOOLS`, `make_schema`, `run_tool`, then the inner loop in `main`; compare with s02 and your typed agent. 60 minutes inside existing review time |
| [mini-swe-agent v2](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py) | Separate loop, model and execution environment | Stage 4: `DefaultAgent`, selected `LitellmModel` and `LocalEnvironment` methods before Tau/Pi. 90 minutes inside existing source-study time |
| [Tau loop](file:///Users/seanmacbook/Self-learn/tau/src/tau_agent/loop.py) | Locate the same mechanism in a real agent | `run_agent_loop` and `_execute_tool_call`; introduce async before tracing unfamiliar async portions |
| [Pi agent loop](file:///Users/seanmacbook/Self-learn/pi/packages/agent/src/agent-loop.ts) | Main TypeScript architecture reference | Stage 4: one flow through messages, turns, tools and events |
| [Pi extensions](file:///Users/seanmacbook/Self-learn/pi/packages/coding-agent/docs/extensions.md) and [subagent example](file:///Users/seanmacbook/Self-learn/pi/packages/coding-agent/examples/extensions/subagent/README.md) | Extension boundary and later worker interface | One narrow extension, then a real adapter; the subagent example launches Pi processes |

learn-claude-code is a third-party teaching implementation, not Anthropic's internal source. Generated `agent-learning` chapters and the existing mini-agent are not assigned reading or completed learner work. Tau and Pi were extracted to `Self-learn/tau` and `Self-learn/pi`; the generated parent folder and mini-agent were deleted September 11 at your request.

## Two focused source labs — added September 15

**Section 3 — nanocode, 60 minutes:** after the JS/Node runner and basic TS tool contracts, follow a `read` request from schema through dispatch to its matching result and the next model request. Compare the trace with s02 and your own agent. Explain one failed tool call and what ends the inner loop. Record a source-linked trace and one validation or turn-limit improvement in the existing TypeScript project.

**Section 4 — mini-swe-agent, 90 minutes:** before the larger Tau/Pi source tour, trace `run → step → query → execute_actions` across the model and environment boundaries. Explain who owns messages, executes a command, formats its observation and signals completion. Draw those responsibilities and map them to your own TS agent; use this as preparation for the Pi extension.

These replace part of the existing comparison/review blocks: Section 3 remains 26 hours, Section 4 remains 20, and the course remains 160. Boot.dev is still the language curriculum; the completed opening section stays complete. Read one path in each project; continue building the same TypeScript agent. No live provider run is needed for these reading checkpoints.

Readings are pinned to nanocode `b009d3dbedf14` and mini-swe-agent `04d809ceab9d`, inspected September 15. mini-swe-agent is v2: the selected LiteLLM adapter uses tool calling. Use the pinned code when comparing protocols. These two repositories are online references; the seven existing local source links are unchanged. Full source selections and limitations are in the classroom's [source-lab notes](file:///Users/seanmacbook/Projects/agent-workflow-research/learning-resources-research.md#nanocode-and-mini-swe-agent--added-september-15-2026).

## Tools we will use

See [[Notes/Coding Agent Course/04 Tools and Progress|Tools and progress]] for the complete tool map, adoption stages and current PATH check.

## Terminal, Bash and Linux

| Material | Use it for | Selection |
|---|---|---|
| [Terminal walkthrough](file:///Users/seanmacbook/Projects/agent-workflow-research/terminal-practice/START-HERE.md) and [Herdr practice](file:///Users/seanmacbook/Projects/agent-workflow-research/terminal-practice/HERDR.md) | Everyday navigation, persistent terminal sessions and reconnect practice | Alongside early learning; track practice in [[Projects/Active/terminal-human-in-the-loop\|Terminal workflow]] |
| [YSAP Bash](https://course.ysap.sh/) | Shell and launcher foundations | Early chapters 1–7; quoting, arguments, pipes and status; traps/TTY topics when needed. Run Bash exercises with Bash |
| [Introduction to Linux — LFS101](https://training.linuxfoundation.org/training/introduction-to-linux/) | Main Linux foundation | Selected chapters 3, 7–16 and 18 from the recorded outline; match by topic if numbering changes |
| [Focused operations references](file:///Users/seanmacbook/Projects/agent-workflow-research/learning-resources-research.md) | Fill the gaps needed for actual operation | SSH, packages, networking, services/logs, resource limits and containers; select the reference with the Linux lab |

YSAP and LFS101 remain core sources, with selected readings applied to practical labs. Their official course pages were rechecked September 11. Bash practice is tracked in [[Projects/Active/terminal-agent-02-javascript-node|JavaScript and Node]]; later Linux work is tracked in [[Projects/Active/terminal-agent-06-linux-coordination|Linux and coordination]].

Linux labs use a designated lab environment selected at that stage. Herdr reconnect practice establishes terminal continuity; conversation and task recovery require their own evidence.

## Design references and later workflow trials

| Material | Role and timing |
|---|---|
| [System Design Primer](file:///Users/seanmacbook/Self-learn/system-design-primer/README.md) | Main design reference: requirements/communication early; storage with sessions; queues/backpressure with workers |
| [System Design 101](file:///Users/seanmacbook/Self-learn/system-design-101/README.md) | Visual reinforcement; selected [retry](file:///Users/seanmacbook/Self-learn/system-design-101/data/guides/how-do-we-retry-on-failures.md), [delivery](file:///Users/seanmacbook/Self-learn/system-design-101/data/guides/delivery-semantics.md), [idempotency](file:///Users/seanmacbook/Self-learn/system-design-101/data/guides/top-6-cases-to-apply-idempotency.md) and [observability](file:///Users/seanmacbook/Self-learn/system-design-101/data/guides/logging-tracing-metrics.md) guides when failures make them relevant |
| Claude Code / Codex worker documentation | Official interface documentation and installed CLI help are selected and version-checked during the worker lab; our teaching replica is not the product contract |
| [Paseo](https://paseo.sh/agents) and [T3 Code](https://github.com/pingdotgg/t3code) | GUI-stage comparison; then [one T3 architecture path](https://github.com/pingdotgg/t3code/blob/main/docs/internals/overview.md), with only the React/Effect concepts needed to follow it |
| [OMP](https://github.com/can1357/oh-my-pi) and [Orca](https://github.com/stablyai/orca) | Candidates for the existing-tool team capstone; selection follows trials |
| [Effect](https://effect.website/) | Optional later comparison after an understood plain-TS adapter; broad adoption is not a prerequisite |
| [SDE system-design roadmap](https://github.com/aasthas2022/SDE-Interview-and-Prep-Roadmap/tree/main/System%20Design) | Optional reference for specific questions; does not set the syllabus |

## Optional object-oriented design bridge

[Grokking OOD — local index](file:///Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/readme.md) is included as a targeted optional reference. Use the following only when they help explain your current build, inside the existing study budget:

- During [[Projects/Active/terminal-agent-03-typescript-agent|foundation Section 3 — TypeScript]]: [OO analysis and design](file:///Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/object-oriented-design-and-uml/object-oriented-analysis-and-design.md) and selected [class relationships](file:///Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/object-oriented-design-and-uml/class-diagram.md). Name responsibilities and state ownership for your tool contracts. Allow 20–30 minutes if needed.
- Before [[Projects/Active/terminal-agent-05-worker-adapter|foundation Section 5 — worker adapter]]: [sequence diagrams](file:///Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/object-oriented-design-and-uml/sequence-diagram.md). Trace startup, output, failed startup and cancellation. Allow 20–30 minutes if needed.

The repository mixes teaching sketches with newer implementations and tests; the September 11 pull did not run or validate those implementations. Use them for discussion; ground the implementation in the existing TypeScript lessons and official language documentation. Whole-repository completion is not an assignment. [Teacher's assessment](file:///Users/seanmacbook/Projects/agent-workflow-research/ood-material-assessment.md) records the selection and limitations. Evidence belongs in the linked project notes.

## Availability

All seven linked source repositories were refreshed with fast-forward-only Git pulls and matched their upstream default-branch HEADs on September 11. Pi gained 7 commits; Grokking OOD gained 25; the other five were already current. Selected reading paths and the opening source anchor are unchanged. Grokking has an unrelated case-only Java README filename collision on this Mac; [the refresh record](file:///Users/seanmacbook/Projects/agent-workflow-research/material-versions.md) explains it and links both preserved originals. Online links are the course references selected in the September 10 resource audit; enrollment, account access and current product behavior are checked when used. No new course purchase is part of this organization.

Local file links open on this Mac; they are not copies stored in iCloud. The [classroom source shelf](file:///Users/seanmacbook/Projects/agent-workflow-research/materials/README.md) lists their locations and revisions. Use [[Notes/Coding Agent Course/02 Study Route|Study route]] to choose what matters now.

## Long-term additions — September 28, 2026

The [expanded study plan](</Users/seanmacbook/Projects/agent-workflow-research/expanded-research-plan.md>) adds official Claude courses, Codex and comparative agent source study, and a full inference progression through vLLM. Its tables provide the current links, purposes, prerequisites and checkpoints. These additions extend the earlier foundation estimate and continue after the exam.

Begin with the official subagent course using the monitoring skill as a concrete example. In parallel, begin the inference prerequisite check and trace one generated token before studying KV-cache optimization. Existing annotations, task states and source-reading pins remain authoritative for work already recorded.
