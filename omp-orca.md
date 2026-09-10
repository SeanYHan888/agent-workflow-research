# OMP and Orca: delegated workflow findings

Research date: 2026-09-09. Primary-source documentation review; no installation or live integration test.

## Identity and compatibility

**OMP at omp.sh is a coding harness, and Orca is its possible environment and outer orchestration layer.** The correct OMP repository is `can1357/oh-my-pi`: a fork of Mario Zechner's Pi with built-in coding tools, subagents, model providers, sessions, and extensions. Search also returns unrelated repositories called oh-my-pi; do not follow their installation instructions. Keeping Claude Code, Codex, upstream Pi, and OMP means maintaining four harnesses, even if the last two share ancestry. [OMP repository](https://github.com/can1357/oh-my-pi)

Orca launches CLI agents in terminals and supplies worktrees, review surfaces, browser panes, and remote capabilities. Its supported-agent table specifically lists **both Pi and OMP**, each with auto-setup, hooks, and status. Consequently OMP inside Orca is documented integration, not merely a speculative terminal workaround. However, that does not establish that Orca exposes every OMP internal subagent as a separate managed worker. [Supported agents](https://www.onorca.dev/docs/agents/supported)

## What owns the work?

Orca's structured orchestration is explicitly **Experimental**. It has Runs, tasks with dependencies, dispatch attempts, supervised workers, messages, and coordinator-owned decision gates. A Run is a durable namespace/inbox and explicitly does not schedule or place workers. A coordinator must create tasks, launch workers, process completion and escalation deliveries, acknowledge them, and decide follow-ups. A worker's completion includes task and dispatch IDs so an old attempt cannot complete a later retry. [Orchestration](https://www.onorca.dev/docs/cli/orchestration)

OMP independently has subagent orchestration inside its own session: batching, concurrency limits, peer messaging, saved child transcripts, custom agents, and model routing. Child sessions do not inherit the parent's full conversation, so assignment/context quality matters. Non-isolated children use the parent's working directory. Optional isolated tasks produce patches or branches; their workspace is cleaned up at completion and they cannot be revived like non-isolated parked children. [OMP task documentation](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/tools/task.md)

**Recommendation:** choose a single authority for each level of work. Start with Orca owning feature/task worktrees and a coordinator owning task acceptance. Let OMP manage small internal subtasks only inside one assigned task. Avoid simultaneously having OMP and Orca independently split the same feature, assign the same files, integrate patches, and retry failures. This recommendation is an architectural inference from the two independent lifecycle systems, not a vendor-prescribed combined topology.

## Two useful configurations

1. **Simpler fleet:** Orca runs Claude Code and Codex workers; one coordinator and one integration owner; human reviews final diffs. Upstream Pi remains available for interactive terminal work. This preserves the user's maximum of three maintained harnesses and does not require OMP.
2. **OMP-centric delegation:** Orca runs one OMP coordinator/session per feature; OMP creates bounded children internally. Orca supplies feature worktrees and the human review surface. Choose this if OMP's built-in subagent controls materially improve outcomes; it replaces upstream Pi in the daily toolset if the three-harness limit is firm.

These are proposed operating designs, not claims that the products automatically enforce them. For initial experiments, use at most two independent writers and one reviewer, disallow recursive delegation, and designate one integration owner. Increase concurrency only after measuring accepted output and reviewer effort.

## Isolation and approval: defaults matter

Orca's agent docs say new launches pre-fill permission-bypass arguments, including Claude's skip-permissions and Codex's bypass-approvals-and-sandbox flag. The global Agent Permissions setting can switch uncustomized agents to Manual; custom arguments can opt an agent out of later global migrations. Therefore inspect actual launch arguments, rather than assuming a global toggle controls every session. [Supported agents](https://www.onorca.dev/docs/agents/supported)

OMP's tool approval default is `yolo`. Its headless subagents run with that mode so they cannot block on local UI; the parent task approval is the documented authorization boundary, while explicit per-tool deny/prompt settings still apply. This is materially different from a human approving every child command. [OMP approval modes](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/approval-mode.md)

A worktree isolates checked-out files and branches, not the operating system or credentials. Orca also supports shared directories and copies of gitignored files: dependencies/caches may be shared, while `.worktreeinclude` may copy files such as `.env`. Treat shared mutable caches and environments as explicit design choices. [Worktree behavior](https://www.onorca.dev/docs/model/worktrees)

For a reviewer-only unattended run, the practical boundary should therefore be an isolated runtime with only needed credentials and resources, plus a final human merge/release gate. This is a recommendation; the reviewed worktree documentation does not establish automatic OS sandboxing.

## Human as reviewer workflow

Write a bounded task contract: outcome, non-goals, owned files/modules, acceptance checks, maximum scope, and when to escalate. Workers return commits/diffs, checks performed, and unresolved questions. One integration owner combines accepted changes and runs checks against the combined result. The human then reviews behavior and diff, requests targeted corrections, and authorizes merge/release. This preserves reviewer control without requiring continual command-by-command steering.

Orca's diff annotations provide a concrete correction loop: line comments can be batched and sent back to an agent. Its worktree lifecycle includes review against the starting ref, commit/push/PR, and cleanup. [Diff annotations](https://www.onorca.dev/docs/review/annotate-ai-diff), [Worktree lifecycle](https://www.onorca.dev/docs/model/worktrees)

## Maturity and adoption decision

Both projects provide public source and MIT licensing. Orca describes frequent releases; its orchestration guide warns that command flags evolve and directs installed agents to obtain the current full skill. Retired orchestration commands can return recovery text without taking action. Treat old blog posts and copied command recipes as version-sensitive. [Orca repository](https://github.com/stablyai/orca), [OMP repository](https://github.com/can1357/oh-my-pi), [Orchestration guide](https://www.onorca.dev/docs/cli/orchestration)

Do not infer reliability or productivity from agent counts or marketing multipliers. Pilot one small feature that naturally separates into two modules. Compare with the same class of work in a single harness using elapsed time, human interventions, review minutes, integration failures, actual usage/cost, and accepted correctness. OMP + Orca is compatible and can be useful; it is not necessary merely to have parallel Claude Code/Codex workers.
