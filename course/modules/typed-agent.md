# M3 — Build a small typed agent

M3 builds the second project-route artifact: **a typed agent using the runner**. The learner turns the M1 cycle and the M2 runner into one small TypeScript agent. Explicit contracts sit between the agent and both the provider and the tools. Each model-supplied tool request is validated at runtime before the runner executes it. The loop is bounded, the session persists and reloads, and the whole run can be cancelled. The roadmap requires extending the runner rather than starting several independent agents, so M4 can attach a real worker harness to the same contracts. M16, M18 and M19 reuse this artifact.

## Useful result

The result is one agent that completes a fixture task through the runner, first against a scripted provider and then against one real provider, with the same loop code in both cases. It is sized for a single-learner build.

**Observable acceptance:**
- An invalid tool request is rejected with a structured error that the model sees. Nothing is executed.
- A run that never stops stops at its limit with a distinct stop reason.
- A run killed during a tool call is reloaded, and the learner explains what the session record does and does not prove about that effect.
- A cancellation stops both a pending provider call and the runner's child.
- Tests cover these cases.

## Entry requirements

- The relevant M2 language, async, file and process checkpoints, normally M2.1–M2.5. M2.6 can finish in parallel.
- [M11 E1/E2](engineering-practice.md) before substantial agent edits. E3–E6 are practiced on this artifact through M3/M4 and charged to M11.
- Boot.dev TypeScript can run alongside the build; finishing it first is not required. The CS329Z S1 comparison waits for language/API readiness.

## Checkpoints

These checkpoints elaborate the roadmap's M3 row: provider/tool contracts, runtime validation, context, persistence, cancellation, tests, and the selected CS329Z component/baseline lessons, all built by extending the runner. They add no outcome and raise no depth.

| ID | Checkpoint | Observable evidence |
|---|---|---|
| M3.1 | Provider and tool contracts | A learner-authored contract module covers task, tool definition, tool call, tool result, provider response and stop reason. The learner shows one invalid state that a discriminated union excludes and one value from JSON or a model that the types cannot rule out. |
| M3.2 | Runtime validation | Task input and tool arguments are checked at the boundary. An unknown tool, a wrong type, a missing field and a path outside the workspace each yield a structured error result with no execution. The learner explains why a schema sent to the provider does not validate anything locally. |
| M3.3 | Context and bounded loop | A trace of one multi-step run shows the context assembled for each request. Tool output entering the context is bounded. An explicit step limit produces its own stop reason. |
| M3.4 | Persistence and recovery | One session persists and reloads. After a kill during a tool call, the learner identifies the recorded intent without a result and applies a chosen policy: report, re-run only a replay-safe tool, or ask. They justify the policy. |
| M3.5 | Cancellation | One cancellation signal reaches the provider wait and the runner's child. Cancelling during a provider call, during a tool and between steps each produces an `aborted` outcome, and the child is shown to have stopped (reusing M2.5). |
| M3.6 | Tests and provider swap | Scripted-provider tests cover the normal path and the M3.2–M3.5 failures. One real provider adapter runs the same fixture task without loop changes. The learner explains one difference that the real responses exposed. |
| M3.7 | Baseline comparison (CS329Z S1) | On a public or synthetic fixture with held-out cases, the learner compares a fixed workflow with the bounded agent. They give a results table, error analysis, and a defended conclusion, which may be "the workflow is enough". |

## Lab sequence

Follow the [session workflow](../../teaching/README.md#prepare-and-teach). Every increment changes the same repository and gets one reviewable change under M11. Read the source comparisons only after the learner has made their own attempt.

| Increment | Deliverable | Acceptance check | Learner's first action | Timebox |
|---|---|---|---|---:|
| 1. Contracts | Types-only contract module, compiled under strict settings | M3.1 | List every value that crosses a boundary in the M1 dispatcher and the M2 runner | 2–4h |
| 2. Validation | A boundary validator and four malformed fixtures | M3.2: each fixture returns an error result, and a log or spy shows nothing executed | Predict which of the four the compiler would catch and which it cannot | 3–4h |
| 3. Scripted provider, bounded loop | A loop over a provider interface backed by a scripted response list, with tools run through the runner | M3.3: the fixture task finishes in the expected steps, and an endless script stops at the limit | Write the scripted responses for one task before writing the loop | 4–6h |
| 4. Persistence | Append-only session records, reload, and a deliberate kill mid-tool | M3.4 | Decide what is written before and after a tool effect, and predict what a crash between the two leaves behind | 4–6h |
| 5. Cancellation | One signal threaded through provider and tool calls | M3.5: three cancel positions, each with an observed outcome | Draw who owns each pending operation at the moment cancel arrives | 3–4h |
| 6. Real provider and tests | A provider adapter and a scripted test suite | M3.6 | List what a real response carries that the scripted one does not: IDs, stop reasons, usage, errors | 3–4h |
| 7. Baseline | A workflow-versus-agent comparison with held-out cases | M3.7, within the 6h practical cap for a CS329Z slice | Choose the fixture and define success and scoring before running anything | 4–6h |

The shape below is a sketch of what increment 1 should make explicit. It is not a solution and not a required design:

```ts
type StopReason = "done" | "tool_use" | "step_limit" | "aborted" | "error";
type ToolResult = { callId: string; ok: true; content: string } | { callId: string; ok: false; error: string };
```

Fixtures stay harmless and offline-first. The learner supplies and controls any real provider credentials, and records the provider, model and cost conditions.

## Failure experiments

- Tool arguments arrive as a JSON string instead of an object, with extra properties, or with a number sent as a string. Should the agent coerce? Compare Pi's `validateToolArguments`, which converts before checking.
- A response cut off by the token limit while it carries tool calls. Pi fails every call in such a message rather than executing it.
- A duplicate call ID, a tool that throws, and a tool that returns oversized output.
- A provider error or timeout during a request, as distinct from a tool failure.
- A torn or partial last line in the session file, and a crash between recording intent and recording the result.
- After recovery, the model requests the same side-effecting tool again. Compare Pi's per-tool `replay` policy.
- A cancel that arrives after the child has already exited, or while the agent is between steps.

## Materials

| Source | Role | Supports |
|---|---|---|
| [Boot.dev Learn TypeScript](https://www.boot.dev/courses/learn-typescript) | Required completion goal, charged to M3: unions, narrowing, interfaces, generics | M3.1 |
| [TypeScript Handbook: Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | Discriminated unions and exhaustiveness | M3.1 |
| [Claude Academy: Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) (A6) | Completion goal shared across M3/M4. Take tool use and agents first. | M3.6 |
| [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Workflow versus agent; what to put in context | M3.3, M3.7 |
| [CS329Z S1 selection](../../materials/university-course-integration.md#required-stanford-selections--m3m4m7m10) | Components, structured I/O, simple baseline, held-out cases | M3.7 |
| [nanocode](../../materials/sources/agents/nanocode/nanocode.py) (`b009d3dbedf1`): `TOOLS` from line 102, `run_tool` 136–140, `make_schema` 143–167, inner loop in `main` 222–259 | One-hour comparison: a registry generates schemas, exceptions become text, and the loop stops when there are no results. Schema ≠ local validation and in-memory history ≠ persistence. Name one improvement for the learner's agent. | M3.1, M3.2, M3.4 |
| Pi (v1.4.0, `4a080252f06c`): [`AgentTool`](../../materials/sources/agents/pi/packages/agent/src/types.ts) 466–499 (execute with `AbortSignal`, `replay` at 490); [`Tool`/`Context`](../../materials/sources/agents/pi/packages/ai/src/types.ts) 762–783; [`validateToolArguments`](../../materials/sources/agents/pi/packages/ai/src/utils/validation.ts) 317–353; [`prepareToolCall` and `runLoop`](../../materials/sources/agents/pi/packages/agent/src/agent-loop.ts) 718–787 and 172–330 | A production TypeScript reference for contracts, validation, truncated-call handling (273–279) and abort paths. The full Pi trace is M4. | M3.1, M3.2, M3.4, M3.5 |
| [Tau `_execute_tool_call`](../../materials/sources/agents/tau/src/tau_agent/loop.py) 283–340 (`55df51608b8b`) | Python async comparison: blocked, cancelled, not-found and error results | M3.2, M3.5 |
| [mini-swe-agent `DefaultAgent`](../../materials/sources/agents/mini-swe-agent/src/minisweagent/agents/default.py) (`04d809ceab9d`): `run` 88–124 (saves in `finally`), `query` 130–152 (step, cost and time limits) | Limits and per-step trajectory saving to compare. The full trace is M4. | M3.3, M3.4 |
| [System Design Primer](../../materials/sources/design/system-design-primer/README.md), database and consistency sections | Supporting reading for comparing JSONL and SQLite session records | M3.4 |

## Hours

[WORKLOAD](../WORKLOAD.md) estimates **35–55 directed hours** for M3. That includes Boot.dev TypeScript, the typed agent, the validation/state/provider boundary, the selected agent-component lessons and M3's share of the API course. The 14–20h API-course allowance is split across M3/M4, and CS329Z S1 takes 6–8h within M3/M4. The increments above total about 23–34h. Reforecast at entry if TypeScript completion alone exceeds the remainder. M11 E3–E6 and M16 P1/P3 work on this artifact are charged to their own milestones, counted once. Keep each execution slice within 6–9 project hours and 21 days.

## Assessment

Use the [shared rubric](../ASSESSMENT.md). Required evidence is a learner-authored agent that extends the runner, with tests for the M3.2–M3.5 failures. The learner explains one run end to end, with state ownership, and handles an unfamiliar change such as a new tool, a new stop reason or a recovery-policy variant. For M3.7, the evidence is a baseline with held-out cases and error analysis. A working demo or a generated agent alone does not establish M3. M19 MC2 and M18 reuse this validation and fixture evidence.
