# Personal agent workflow design

Research date: 2026-09-09. This is a proposed architecture, not an installed or tested configuration. Product facts below come from primary documentation; recommendations and trial criteria are design judgments. Assume “single thread” means one active harness conversation per task and “ghosty” means Ghostty. Execution location and first target workload remain open questions.

## Recommendation

Start with Ghostty + Herdr for terminal-first collaboration if Herdr is a firm preference. Choose cmux instead when a native sidebar, integrated browser, and Mac-oriented navigation matter more than using Herdr as the primary interface. Add Paseo for sessions that need GUI/mobile access. Evaluate Orca with an already familiar harness before adding OMP. This sequencing lets each new layer earn its place.

Do not treat every named tool as a required part of one stack. Assign one owner to each running session, one writer to each task checkout, and one coordinator to each delegated run.

## Verified tool boundaries

| Tool | Documented responsibility | Design implication |
|---|---|---|
| Ghostty | Terminal application with configurable rendering, keys, and windows | A straightforward client for Herdr. [Docs](https://ghostty.org/docs) |
| Herdr | Background server owns terminal panes; clients detach/reattach, including over SSH | Use for terminal lifetime and navigation. [Persistence](https://herdr.dev/docs/persistence-remote/) |
| cmux | Native terminal workspaces, notifications, and programmable browser | Can be the primary desktop environment. [Product](https://cmux.com/) |
| Claude Code, Codex, Pi | Agent harnesses with their own conversation/session behavior | Choose one for the current task; a model accessed through Pi is still running under Pi's harness. [Claude sessions](https://code.claude.com/docs/en/sessions), [Codex](https://learn.chatgpt.com/docs/codex/cli), [Pi](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) |
| Paseo | GUI/mobile/CLI management with adapters for Claude, Codex, Pi, and OMP | Potential common GUI; adapter support does not establish live attachment to arbitrary Herdr terminals. [Providers](https://paseo.sh/agents) |
| OMP | Separate Pi-derived coding harness | Count it separately when budgeting harness maintenance. See companion research. |
| Orca | Worktree-oriented agent environment with structured orchestration | Candidate for delegated implementation and review. [Orchestration](https://www.onorca.dev/docs/cli/orchestration) |

cmux restores layouts and can launch native resume commands for supported agents; it explicitly does not checkpoint arbitrary running processes. Herdr detach keeps server-owned processes alive. Neither statement means a local agent computes while the host is asleep or powered off. [cmux restore](https://cmux.com/docs/session-restore), [Herdr persistence](https://herdr.dev/docs/persistence-remote/)

Herdr's status is useful evidence for attention routing, not proof a task is correct. Its documentation explains that unfamiliar prompts can be classified as idle. Use tests and explicit completion reports for task acceptance. [Agent detection](https://herdr.dev/docs/agents/)

## Workflow A: direct collaboration

Recommended shape:

```text
Human
  -> Ghostty
      -> Herdr on the execution machine
          -> one selected harness / named task
          -> shell for verification
          -> development server or logs, if needed
```

Use a short task brief: goal, acceptance examples, constraints, relevant paths, and explicit out-of-scope work. Discuss uncertainties with the agent, implement a small coherent slice, inspect the diff or actual behavior, and continue in that same conversation.

Keep one writer per checkout. Multiple independent tasks can use separate worktrees, even when you personally steer only one at a time. Read-only reviewers can inspect the same snapshot; freeze or identify that snapshot so their findings are reproducible.

Keep the selected model stable during a task initially. Deliberate switches are possible, but frequently changing harness and model simultaneously makes it difficult to understand which change helped. Choose the default harness using your own completed tasks, intervention effort, and review burden; do not assign universal planner/coder roles based on branding.

For switching harnesses, save an artifact handoff:

```text
Task and acceptance criteria:
Execution host and absolute checkout path:
Branch and commit; uncommitted changes:
Completed work and decisions:
Checks actually run and results:
Known failures or unknowns:
Next bounded action:
Actions still needing human authorization:
```

The portable handoff is the code plus this record. Native transcripts remain harness-specific. Claude's docs explicitly warn that two terminals resuming the same session interleave transcript messages. Treat session input ownership as exclusive. [Claude sessions](https://code.claude.com/docs/en/sessions)

## Choosing the terminal

| Preference | Initial choice | Tradeoff |
|---|---|---|
| Herdr-centered workflow, portable terminal interaction | Ghostty + Herdr | Learn Herdr's navigation and manage its daemon |
| Mac workspace sidebar and browser beside code | cmux + native harness | Less need for Herdr locally; distinguish resume from live persistence |
| cmux browser plus Herdr lifetime/SSH behavior | cmux + Herdr | Two sets of panes and state; give each a narrow role |

If nesting cmux and Herdr, use cmux for the outer project/browser surface and Herdr for agent terminals. Do not begin by automatically mirroring every tab, pane, and notification. Community bridges exist, but are an additional versioned integration to test, not a prerequisite. [Bridge repository](https://github.com/lachieh/herdr-plugin-cmux)

## Paseo ownership

For a task that needs phone/GUI access, start it under Paseo and use its clients. Its CLI can launch, attach to output, and send follow-ups to Paseo-managed agents. Codex uses app-server; Claude uses the Agent SDK. These are different interfaces from viewing the native terminal TUI. [CLI](https://paseo.sh/docs/cli), [Codex adapter](https://paseo.sh/docs/codex), [Claude adapter](https://paseo.sh/docs/claude-code)

No verified automatic Herdr-to-Paseo live-session handoff was established in this investigation. Before relying on one, test session ID continuity, permissions, pending prompts, transcript integrity, and exclusive input ownership on a disposable task. Until then, choose the owner at task creation and transfer finished artifacts when changing owners.

Paseo can also create worktrees and coordinate agents; it could cover modest delegated workloads without Orca. Compare the actual review experience before maintaining both managers. [Orchestration](https://paseo.sh/docs/orchestration)

## Workflow B: delegated execution, human review

```text
Human-approved brief and acceptance examples
  -> single coordinator
      -> worker A / owned worktree
      -> worker B / owned worktree
      -> fresh reviewer / fixed candidate revision
  -> coordinator integrates and verifies combined result
  -> human reviews evidence and approves merge/release
```

The coordinator owns dependencies, dispatches, retries, and integration. Workers own bounded deliverables. The reviewer reports findings with evidence and does not silently expand scope. A final combined test run matters because separately passing branches can fail together.

Start with two implementation workers at most. Parallelize genuinely separable modules or tests against a stable interface. Keep tightly coupled API/schema changes sequential until contracts are settled. Large does not automatically mean parallelizable.

Use stop rules: fixed concurrency, a run budget, a retry cap, and escalation after repeated identical failures or missing acceptance information. Worker-local helpers must count toward the same overall budget. Avoid recursive delegation by default.

Require a review packet with: acceptance results; candidate commit; diff; exact checks and outcomes; unresolved findings; and a suggested demonstration. For experiments, substitute run configuration, provenance, evaluation artifacts, and reproducibility evidence where appropriate. Human reviewer mode works only when workers produce material a human can efficiently judge.

Orca currently labels structured orchestration experimental. Its Run stores coordination context; a coordinator still schedules workers. Its documented launch defaults use permission-bypass flags, including sandbox bypass for Codex. Use Manual launches on a personal machine initially, or put unattended work in an explicitly bounded environment. A Git worktree is not an OS sandbox. [Orchestration](https://www.onorca.dev/docs/cli/orchestration), [Agent defaults](https://www.onorca.dev/docs/agents/supported)

## Adoption experiment

1. Complete three representative direct-collaboration tasks with one harness in the chosen terminal arrangement. Confirm interrupt, resume, detach, clipboard, and attention behavior.
2. Repeat one modest task through Paseo and test switching between its desktop and mobile/web clients. Record actual differences from the TUI.
3. Delegate a small two-part feature through Orca using the familiar harness. Add a separate review pass and test the combined result.
4. Run a comparable delegated task with OMP. Keep it only if it reduces human interventions or improves accepted outcomes enough to justify another harness.

Record wall time, active human minutes, review time, repair turns, model usage where available, and recovery problems. Choose based on accepted results and attention saved, not how many agents can be launched.

## Evidence limits

This was documentation research, not a benchmark, installation audit, or interoperability test. Sources and software may evolve. The linked X post returned no readable original body; Ghostty recommendations rely on official documentation rather than reconstructing that post. No existing configurations, services, or credentials were changed.
