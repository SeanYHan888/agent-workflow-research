---
type: project
status: later
area: tools
start: 2027-03-08
deadline: 2027-04-18
outcome: Operate the workflow with both worker harnesses, bounded parallelism, explicit task state and recoverable Linux execution.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 7
---
# 06 — Coordination and Linux recovery

**Planned start:** 2027-03-08 · **Target finish / deadline:** 2027-04-18

[[coding-agent-course|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[terminal-agent-05-worker-adapter|Previous section]] · [[multi-agent-human-review|Next — team capstone]]

Dates are study targets, not actual start/completion records. Planned allocation: **60 hours** within the shared **10 hours/week** course budget, including reserve. Reforecast with the overview if the preceding checkpoint takes longer.

## Project goal:

Operate the workflow with both worker harnesses, bounded parallelism, explicit task state and recoverable Linux execution.

## Done when:

This is the supervised two-worker foundation. The later [[multi-agent-human-review]] project reuses it to test coordinator-led execution and final human review; it does not repeat the language or Linux course.

I can integrate and verify two isolated changes, diagnose an interrupted run, reconcile uncertain outcomes before retrying, and demonstrate Linux recovery using logs.

## Start here:

First operate one worker on a designated Linux lab host. Then add the second adapter, separate worktrees and bounded concurrency. Apply the design readings to observed failure cases.

## Tasks:

- [ ] Add the second harness, then two separate worktrees and integrated verification
- [ ] Apply focused system design to the personal agent workflow
    - [ ] Design bounded queues and demonstrate retry/duplicate-task handling
    - [ ] Explain logs, access boundaries, and recovery in a final architecture walkthrough
- [ ] Learn Linux for agent operations using LFS101 and focused labs
    - [ ] Complete command line, permissions, processes, user environment, networking, and security foundations
    - [ ] Demonstrate SSH, signals, services/logs, resource limits, and container/workspace boundaries in a designated lab environment
- [ ] Verify remote attachment alongside the Termius/Tailscale task and document daemon/host restart recovery separately
- [ ] 手机通过termius + tailscale 连接

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- [LFS101](https://training.linuxfoundation.org/training/introduction-to-linux/) — selected relevant topics; Bash/process basics began earlier.
- `/Users/seanmacbook/Self-learn/system-design-primer` and `/Users/seanmacbook/Self-learn/system-design-101`.
- Official Git, Linux service/network and container references linked in the repository resource guide.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
