# M1 — Explain and implement an agent tool cycle

M1 is the first stage of the [project route](../../ROADMAP.md#project-route). The learner works out which part of an agent system actually does things. The model returns content that may include a structured tool request. The harness decides whether to run that request, runs the registered code, and returns the result in the next request. Everything later in the course depends on this distinction: the M2 runner, the M3 typed agent, the M4 worker adapter and the M19 MCP server. M1 starts from a paper trace and a scripted dispatcher. It needs no model API, installation or credentials.

Learners who have already demonstrated M1 evidence keep that credit and are not assigned the work again. For them, this page is review material for specific gaps or for comparison.

## Useful result

The learner builds a tiny fixture-reading dispatcher that takes **scripted** tool requests in place of a model. It runs the registered handler, pairs each result with its request ID and handles requests it cannot serve. With it comes a short trace, in the learner's own words, of one iteration of a real teaching loop.

**Observable acceptance:** the learner points to the line that executes the tool and says who owns each value that changes in one iteration. The dispatcher returns the fixture contents for a valid request and an explained error result for an unknown tool, and it keeps running afterwards. The learner also explains what makes the loop stop and what happens if tool requests never stop.

## Entry requirements

- Small-script orientation as needed. The learner can read and write a short Python or JavaScript program. Async code is not required.
- No M11 Git practice is needed yet. The dispatcher can live in any scratch directory.

## Checkpoints

These checkpoints elaborate the roadmap's M1 row: model output versus harness execution, messages, validation, stop conditions and failures. They add no outcome and raise no depth.

| ID | Checkpoint | Observable evidence |
|---|---|---|
| M1.1 | Model output versus harness execution | The learner states that the model returns a request, not an effect, and identifies the function call that performs the effect. If they say "the AI runs it", they are asked to point to that call. |
| M1.2 | Messages carry the cycle | A written trace of one iteration lists what is appended after the model responds and after the tool runs, how results are paired with call IDs, and why the next request needs both. |
| M1.3 | Validation and failure paths | The dispatcher returns an error result, rather than crashing, for an unknown tool name and one malformed request. The learner predicts how a reference loop behaves on the same input and checks the prediction against the source. |
| M1.4 | Stop conditions | The learner locates the normal return and explains the absence of a turn limit. They distinguish a per-call `max_tokens` from a bound on loop iterations, and an exception that aborts the loop from a normal return. Implementing a bounded loop belongs to M3. |

## Lab sequence

Follow the [session workflow](../../teaching/README.md#prepare-and-teach). [Session 01](../../teaching/SESSION-01.md) is a prepared example of increment 1. The learner predicts before reading code, and the teacher gives the smallest useful hint.

| Increment | Deliverable | Acceptance check | Learner's first action | Timebox |
|---|---|---|---|---:|
| 1. Trace one cycle | A written trace of a scripted read-file exchange, then of `agent_loop()` in s01 | M1.1 and M1.2: name the owner and the changed value for each event in one iteration | Predict the order of events in a scripted request → execute → result → answer exchange before opening the file | 30–45 min |
| 2. Scripted dispatcher | A dispatcher that reads scripted requests (ID, tool name, arguments), runs a fixture-reading handler confined to one directory, and emits results paired by ID | A valid request returns the fixture contents with the matching ID. An unknown tool yields an error result and the next scripted request still runs. | Write the shape of one request and one result on paper, then decide where the registry of tools lives | 60–90 min |
| 3. Failures and stopping | One malformed-request case added to the dispatcher, plus a written comparison with the s02 dispatch map | M1.3 and M1.4: predict s02's behavior on a missing argument and verify it in the code. Show the dispatcher ending when the script has no more requests, and explain what s01 would do if requests continued. | Predict what `handler(**block.input)` does when a required argument is absent | 45–60 min |

Tau's `_execute_tool_call` is an optional fourth comparison. Assign it only after M2 has introduced async, so that async syntax does not obscure the cycle.

## Failure experiments

Each case needs a prediction first and an explanation afterwards. Run them against the learner's own dispatcher; for the reference loops, trace them on paper.

- An unknown tool name, and a known tool with a missing or wrongly typed argument. Which component notices, and what does the next model request contain?
- A request for a path outside the fixture directory. Compare s02's `safe_path`, which raises, with a handler that returns an error string.
- A handler that raises. In s01/s02, is this caught and turned into an error result, or does it end the loop?
- A result returned without its call ID, or with the wrong one. What can the next model call no longer tell?
- A script that keeps requesting tools. Show where s01 bounds this, or explain why nothing does.

## Materials

| Source (pinned submodule revision) | Role | Supports |
|---|---|---|
| [learn-claude-code s01 `agent_loop()`](../../materials/sources/agents/learn-claude-code/s01_agent_loop/code.py), lines 87–117, `0dcafa2ae053` | Primary trace. Lines 89–92 are the model call, 95 the assistant append, 98–102 the tool-request check and return, 108 execution through `run_bash`, and 110–117 the results paired by `tool_use_id`. | M1.1, M1.2, M1.4 |
| [s01 `run_bash()`](../../materials/sources/agents/learn-claude-code/s01_agent_loop/code.py), lines 71–84 | Harness-side guard, timeout and truncation. Shows that errors become result text. | M1.3 |
| [s01 README](../../materials/sources/agents/learn-claude-code/s01_agent_loop/README.md) | Short motivation, read after the learner's own prediction | M1.1 |
| [learn-claude-code s02](../../materials/sources/agents/learn-claude-code/s02_tool_use/code.py): `safe_path` 71–75, `TOOL_HANDLERS` 143–146, dispatch 170–173 | Dispatch map, unknown-tool text and unvalidated `**block.input` | M1.3 |
| [Tau `_execute_tool_call`](../../materials/sources/agents/tau/src/tau_agent/loop.py), lines 283–340, `55df51608b8b` | Optional comparison after M2 async: blocked, cancelled, not-found and error results | M1.3 |

These are third-party teaching implementations. They show the mechanism, not the full behavior of any product harness. Recheck line numbers if a submodule revision changes. The [resource catalog](../../materials/resource-catalog.md) and [advanced study](../../materials/advanced-study.md) hold the later comparison sources (nanocode for M3; mini-swe-agent, Pi and Codex for M4).

## Hours

[WORKLOAD](../WORKLOAD.md) sets **0 remaining directed hours** for learners whose M1 evidence is already credited. For a learner without that evidence, the increments above total about 2.5–3.5 hours, and the original first-section allocation of 10 hours, including reserve, stays the planning ceiling. Reforecast at entry from a short diagnostic.

## Assessment

Use the [shared rubric](../ASSESSMENT.md). The evidence is the learner's trace and their working dispatcher, including its failure cases. For transfer, the teacher supplies an unseen variation, such as a second tool, a duplicated call ID or a handler that hangs. The learner predicts the outcome before running it. Reading the source alone does not complete M1. M18 AS1 and M19 MC1 reuse this evidence and do not reassess it.
