# M4 — Explain real harnesses and integration boundaries

M4 is the Stage II milestone where the learner's own typed agent meets real harnesses. It covers selected mini-swe-agent and Pi source, a Pi extension, a real-worker adapter, and terminal and GUI session ownership. It keeps the required Codex source study, which comes after the smaller traces and after M12 R1 Rust readiness. CS329Z design material supports harness, memory and framework comparisons, but it does not replace the source traces. The [roadmap row](../../ROADMAP.md#stages-and-milestones) owns the scope. This page arranges that scope into checkpoints and lab briefs.

## Useful result

Connect the runner and typed agent from M2/M3 to a real harness, and explain who owns each part of the work. The deliverable has five parts: annotated source traces, one narrow Pi extension written by the learner, a bounded worker adapter, a comparison of terminal and GUI session ownership, and a Codex trace with one understood change. Use a harmless fixture repository and the same bounded task in every harness: read a fixture, make one controlled edit, run a check, report the result.

**Observable acceptance:** the runner starts a real harness task on the fixture through the adapter and streams its state. When asked, it cancels the task and shows that the task stopped. It reports failed startup differently from a completed or failed task. The extension blocks one out-of-scope tool call and lets an allowed call through. For both a terminal client and a GUI client, the learner explains which process owns the session, the model request, tool execution and the checkout, and what survives a disconnect.

## Place in the project route

This milestone is the "A real harness connection" row of the [project route](../../ROADMAP.md#project-route). It sits between the typed agent (M3) and the supervised Linux worker (M5). In the [distribution](../projects/agentic-linux-distribution/README.md) it selects or adapts the execution interface. Later modules reuse its evidence without charging it again: M7 reuses the worker boundary, [M17 T1](agentic-linux.md) is the GUI trace below, [M19 MC3](mcp.md) runs alongside the Pi study, [M18 AS4](agent-skills.md) uses these harness boundaries, and the [M11 review/CI lab](../projects/agent-review-ci-lab.md) can use the adapter as its component.

## Entry requirements

- **M3:** validated tool contracts, a bounded loop, persistence and cancellation in the learner's agent. M4 extends that agent; it does not start a second one.
- **M11 E1/E2** before substantial edits. E4–E6 are practised during M3/M4 delivery.
- **M12 R1** before deeper Codex tracing. Completing K1–K5 is not required for the first source traces, and M12 owns the Rust-reading share.
- **Before GUI or service experiments:** a disposable workspace, synthetic inputs and no personal credentials in fixtures. A live provider is optional for the first traces; a scripted response or a paper trace is enough.

## Checkpoints

These checkpoints spell out the roadmap's M4 row in more detail. They add no required outcome, depth or scope.

| ID | Checkpoint | Observable evidence |
|---|---|---|
| M4.1 | Small-harness boundaries (mini-swe-agent) | Pinned trace of loop → model → environment. The learner predicts and locates one limit or exit path, then maps the boundaries onto their own agent. |
| M4.2 | Pi request path | Trace of one prompt through the agent loop to tool preparation, execution and the result message, with the revision recorded. The learner identifies where a call can be blocked or refused. |
| M4.3 | Pi extension | A narrow extension written by the learner, with allowed and blocked cases observed and removal shown. The learner explains what Pi enforces and what only the OS could enforce. |
| M4.4 | Real-worker adapter | A written contract plus fixture tests covering start, framed events, result, failed startup, timeout and cancellation. The learner shows evidence that the work actually stopped. |
| M4.5 | Terminal session ownership | One real task completed with review, interrupted and resumed. A record of what came back (transcript, checkout, processes) and what was lost. |
| M4.6 | GUI/client session ownership | T3 Code trace of client → server → provider → events, with the revision recorded. A comparison with M4.5 for interruption, reconnect and input ownership. |
| M4.7 | Codex source study (required, after R1) | One source record per session: entry and one turn, tool authority, state/context, cancellation, app-server. One narrow change in a separate exercise checkout, with checks and an explained diff. |
| M4.8 | Harness design comparison (CS329Z S2) | A design defense covering memory/state ownership, tool boundaries, stopping and what a framework abstracts. It reuses the M4.1–M4.7 traces against the learner's agent. |

## Lab sequence

Use one increment at a time, following the [session workflow](../../teaching/README.md#prepare-and-teach). The learner predicts first and gets the smallest useful hint. The teacher prepares fixtures but writes no extension, adapter or Codex change for the learner.

| Increment | Deliverable | Acceptance check | Learner's first action | Timebox |
|---|---|---|---|---|
| L1 → M4.1 | Boundary diagram of `DefaultAgent` | Learner points to the code that ends a run at the step, cost or wall-time limit, and names the exit status recorded | Predict where the loop stops before reading `run` | 90 min; nanocode refresher 60 min only if needed |
| L2 → M4.2 | Event trace for one read tool call | Learner identifies the function that refuses a truncated call and the one that emits the result message | Predict the events emitted for one tool call | 2 × 90 min |
| L3 → M4.3 | One-rule extension (for example, a path or command gate) | Fixture call outside the rule is blocked with a reason; allowed call proceeds; disabling restores default | Write the allowed/blocked case pair before coding | One slice of at most 6–9h |
| L4 → M4.4 | Adapter from the runner to one real harness (for example, Pi RPC mode) | Cancel during a tool call leaves the harness idle and emits no further tool events; failed startup is reported distinctly | Write states, messages and who stops what, plus failure cases | One 6–9h slice; split stream from cancel/timeout if needed |
| L5 → M4.5 | Terminal pilot record | After an interrupt and resume, learner shows restored versus lost state; the reviewer's acceptance is recorded | Write a brief with acceptance examples | 4h |
| L6 → M4.6 | GUI ownership trace and comparison table | Learner predicts, then observes, what a client reconnect does to a running turn | Predict which process owns session state before reading | Inside the existing M4 GUI allocation |
| L7 → M4.7 | Codex source records, then one narrow change | Each record names revision, question, entry, key functions, state owner, authority and a failure path; the change passes the relevant checks | Fetch the pinned checkout; record the commit and working tree | 90-min sessions; change as one 6–9h slice |
| L8 → M4.8 | Closed-resource design defense | Learner handles one unfamiliar variation | List the boundaries of their own agent before comparing | 4–6h (S2) |

## Failure experiments

- **mini-swe-agent:** trigger a step or time limit and a repeated format error, then compare the recorded exit messages. Time out a command in `LocalEnvironment.execute`. It returns `returncode` −1; do not assume the child process was cleaned up, so check. The local environment runs on the host and is not isolation.
- **Pi:** a tool call cut off by the output limit is refused, not executed. An extension blocks a call; then fixture text tells the agent to work around the block. Pi's security notes state that it has no built-in sandbox, so name what actually enforces the limit.
- **Adapter:** test four cases: the harness fails to start, it crashes mid-stream, a JSONL record is split, and a cancel arrives during a tool call. Pi RPC uses LF-only framing, and its docs warn that Node `readline` is not compliant. Add a timeout after an uncertain external effect and avoid repeating that effect blindly.
- **Sessions:** two clients send input to one session; the network drops during a running tool; the harness restarts before resume. Give each session one input owner and each checkout one writer.
- **Codex:** a multi-file patch that fails part-way. The runtime records committed changes but does not roll back as one transaction. A hunk whose context does not match is resolved by deterministic tolerance, not by a model.

## Materials

The local checkouts are git submodules. Pi is pinned at the v1.4.0 release (`4a080252f06c`), which includes the built-in MCP/Codemode support M19 uses. Record the revision at each lesson entry, and recheck symbols after any update.

| Source | Role | Checkpoint |
|---|---|---|
| mini-swe-agent [`default.py`](../../materials/sources/agents/mini-swe-agent/src/minisweagent/agents/default.py) (`run`, `step`, `query`, `execute_actions`, `save`), [`litellm_model.py`](../../materials/sources/agents/mini-swe-agent/src/minisweagent/models/litellm_model.py) (`query`, `_parse_actions`, `format_observation_messages`), [`local.py`](../../materials/sources/agents/mini-swe-agent/src/minisweagent/environments/local.py) (`execute`, `_check_finished`, `_run`) | Small loop/model/environment reference; pinned to `04d809ce`, matching the [catalog readings](../../materials/resource-catalog.md#nanocode-and-mini-swe-agent--added-september-15-2026) | M4.1 |
| [`nanocode.py`](../../materials/sources/agents/nanocode/nanocode.py) | Optional compact dispatch refresher | M4.1 |
| Pi [`agent-loop.ts`](../../materials/sources/agents/pi/packages/agent/src/agent-loop.ts) (`runLoop`, `executeToolCalls`, `prepareToolCall`, `failToolCallsFromTruncatedMessage`); Tau [`loop.py`](../../materials/sources/agents/tau/src/tau_agent/loop.py) `_execute_tool_call` | Main TypeScript reference; Tau is a focused comparison | M4.2 |
| Pi [extensions guide](../../materials/sources/agents/pi/packages/coding-agent/docs/extensions.md) (`tool_call`, `tool_result`), examples [`permission-gate.ts`](../../materials/sources/agents/pi/packages/coding-agent/examples/extensions/permission-gate.ts), [`protected-paths.ts`](../../materials/sources/agents/pi/packages/coding-agent/examples/extensions/protected-paths.ts), [security notes](../../materials/sources/agents/pi/packages/coding-agent/docs/security.md) | Extension lifecycle and blocking, and the limits of enforcement | M4.3 |
| Pi [RPC mode](../../materials/sources/agents/pi/packages/coding-agent/docs/rpc.md), [sessions](../../materials/sources/agents/pi/packages/coding-agent/docs/sessions.md), [tmux](../../materials/sources/agents/pi/packages/coding-agent/docs/tmux.md) | Worker protocol, resume and terminal lifetime (v1.4.0 removed the earlier experimental server/client packages; RPC mode is the supported worker interface) | M4.4, M4.5 |
| T3 Code [architecture](../../materials/sources/agents/t3code/docs/internals/overview.md), [connection runtime](../../materials/sources/agents/t3code/docs/internals/connection-runtime.md), [terminal runtime](../../materials/sources/agents/t3code/docs/internals/terminal-runtime.md), [Pi provider](../../materials/sources/agents/t3code/docs/user/providers-pi.md); [M17 source map](../../materials/agentic-linux.md) | Ownership across client, server and provider | M4.6 |
| Codex `materials/sources/agents/codex`: pinned [`e16b631`](https://github.com/openai/codex/tree/e16b631d08cdf82773831f9bbfb793da687d5299), not checked out by default. Fetch it with `git submodule update --init --checkout materials/sources/agents/codex`. Also the [Track B Codex route](../../materials/advanced-study.md#codex-from-behavior-to-code) and the [`apply_patch` trace](../../research/codex-edit-tools-2026-10-16.md) | Required production Rust harness; tool authority traced through a pinned edit path | M4.7 |
| [Claude Code edit interfaces](../../research/claude-code-edit-tools-2026-10-16.md); optional OpenCode (`materials/sources/agents/opencode`, not checked out) | Interface comparison only; the public Claude Code repository does not contain the core tool implementation | M4.7 |
| [Workflow design](../../research/workflow-design.md), [OMP/Orca](../../research/omp-orca.md) | Vocabulary: one input owner per session, one writer per checkout; worktree ≠ sandbox | M4.5, M4.6 |
| [CS329Z S2](../../materials/university-course-integration.md#required-stanford-selections--m3m4m7m10), [fit review](../../research/stanford-cs329z-course-fit.md) | Harness, memory and framework design questions | M4.8 |
| [Cua course fit](../../research/cua-course-fit.md) | Optional: one observation → action → verification trace | M4.6 (optional) |
| [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) | The remaining M4 share of an explicit course-completion goal | Throughout |

## Assessment and hours

Use the [shared rubric](../ASSESSMENT.md). M4.1–M4.8 each need a working artifact or source trace, an explanation in the learner's own words, and an unfamiliar change or fault. Evidence that is already valid counts once; for example, the M4.6 trace also counts for M17 T1. A working adapter or an installed extension alone does not establish mastery.

The [workload forecast](../WORKLOAD.md) estimates **39–60 directed hours**. It covers the source traces and Pi extension, the worker adapter, terminal and GUI ownership work (including the four-hour terminal pilot), the remaining API-course share and the CS329Z S2 selection. The 6–10h of Rust readiness is charged to M12 R1, and M19 MC3 hours are charged to M19. Each practical slice is at most 6–9 project hours and gives a useful result within 21 days at the allocated capacity, inside the 15h weekly cap.
