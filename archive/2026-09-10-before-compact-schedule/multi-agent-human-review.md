---
type: project
status: later
area: tools
deadline: 2027-05-23
outcome: Multi-agent — Human Review Only workflow is documented and validated on one real task.
created: 2026-09-09
tags:
  - project-file
start: 2027-04-19
order: 8
---
# Multi-agent — Human Review Only

[[coding-agent-course|Course overview]] · [[terminal-agent-06-linux-coordination|Prerequisite — two workers and Linux recovery]]

**Planned start:** 2027-04-19 · **Target finish / deadline:** 2027-05-23 · **50 hours / 5 weeks**, inside the shared 10 hours/week.

**Confirmed direction, 2026-09-10:** assemble a working team with existing tools first. Building a new coordination framework is outside this course estimate.

## Project goal:

Deliver one modest feature through a coordinator-led team, with the human defining the brief and reviewing the integrated result. Reuse the existing adapters, worktrees, checks and Linux recovery knowledge. Start with two implementation workers and a separate review pass; expand only when accepted output and human effort justify it. “Large” is a later scaling ambition, not an initial headcount target.

Define the outcome and acceptance criteria, let agents coordinate implementation, and review their resulting work. OMP and Orca are candidates, not a finalized setup. The original Grok exploration task is provisionally placed here as optional bot/automation exploration; its intended scope was unspecified.

### Material audit — 2026-09-09
The previously supplied [OMP site](https://omp.sh/) and [Orca site](https://www.onorca.dev/) have no personal reading-completion record in the searched vault notes. Treat reading status as unknown. The agentic-engineering video is tracked once in [[terminal-human-in-the-loop]].

### Migration

Tasks moved from [[pi-agent]] and [[dev-setup]] on 2026-09-09. Original task wording, nesting, and completion states were retained. Workflow next steps are newly added.

Related projects: [[terminal-human-in-the-loop]], [[gui-human-in-the-loop]].

## Done when:

- One coordinator owns task dependencies, dispatch, retries and integration; each writer owns a separate checkout and a bounded assignment.
- A run produces a review packet: candidate revision, combined diff, acceptance evidence, checks actually run, remaining findings and recovery notes.
- A failed or interrupted worker is detected and reconciled without blindly duplicating its work; concurrency, time/cost budget and retry limits are demonstrated.
- I compare at least two completed trial runs with a direct-workflow baseline, recording human interventions, review time, correctness and usage where available.
- I can accept or reject the integrated result from the evidence and justify whether to increase team size. More agents are not required for completion.

## Tasks:

Complete these in sequence; expand one trial at a time.

### Workflow next steps

- [ ] Review OMP and Orca and choose a small multi-agent trial.
- [ ] Define trial acceptance criteria, agent ownership, and final human review steps.

- [ ] Reuse the Section 6 two-worker example to compare one coordinator configuration with the direct-workflow baseline
- [ ] Run a bounded feature with two writers, a separate review pass and one integration owner; verify the combined result
- [ ] Inject one worker failure or interruption and demonstrate bounded retry, reconciliation and escalation
- [ ] Repeat a comparable trial, record review effort and results, and decide whether a third writer would help

### Optional exploration — not required for course completion

- [ ] grok bot 看看能干啥

## Decisions and blockers:

- Entry gate: Section 5 real-worker lifecycle and Section 6 isolated work, integrated checks and Linux recovery demonstrated. GUI study supplies review experience but no particular GUI is mandatory for this team.
- Evaluate existing Pi/Paseo capabilities first; compare OMP and Orca for a specific missing capability. They remain candidates, not adopted tools. Choose one coordination authority for the trial.
- OMP is a separate Pi-derived harness, not merely a GUI. Its subagent features may substitute for custom implementation; they do not remove the need to understand ownership and failure behavior.
- The human normally reviews at the end; missing requirements, authorization needs or exceeded limits still trigger explicit escalation. Publication and merges remain separately authorized.
- Distributed multi-host fleets, recursive agent trees, a new scheduler and production-scale reliability are follow-on projects requiring a new estimate.

## Resources:

- [OMP source](https://github.com/can1357/oh-my-pi) and [task/subagent documentation](https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md).
- [Orca source](https://github.com/stablyai/orca) and [orchestration documentation](https://www.onorca.dev/docs/cli/orchestration). The documentation fetch failed on 2026-09-10; recheck current interfaces before the trial.
- Existing research: `/Users/seanmacbook/Projects/agent-workflow-research/omp-orca.md` and `workflow-design.md` (dated research, not installation or reliability evidence).
- Selected system-design readings already assigned in [[terminal-agent-06-linux-coordination]]; apply ownership, dependencies, queues, retries and observability to the trial.

## Progress log:

- 2026-09-10: User chose an existing-tools team first. Added the final course capstone with a 50-hour budget; original tasks preserved and no run marked complete.
