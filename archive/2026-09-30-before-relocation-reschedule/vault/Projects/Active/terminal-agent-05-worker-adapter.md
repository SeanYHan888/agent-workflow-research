---
type: project
status: later
area: tools
start: 2026-11-09
deadline: 2026-11-22
outcome: Connect Pi to one real coding harness through an explicit, observable worker interface.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 13
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 6
---
# 05 — Delegate to one real worker

**Planned start:** 2026-11-09 · **Target finish / deadline:** 2026-11-22

[[Notes/Coding Agent Course/00 Start Here|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[gui-human-in-the-loop|Previous — GUI workflow]] · [[terminal-agent-06-linux-coordination|Next section]]

Dates are study targets, not actual start/completion records. Planned allocation: **20 hours** within the shared **10 hours/week** course budget. This compact target has limited slack; reforecast if the preceding checkpoint takes longer.

## Project goal:

Connect Pi to one real coding harness through an explicit, observable worker interface.

## Done when:

The adapter handles output, failure, timeout, cancellation and needs-input. A bounded real edit returns an actual diff and check results for human review.

## Start here:

**Compact pace:** attempt the checkpoint first, read only what you cannot yet explain, and reuse the existing runner/agent. Keep the recorded completion criteria and Boot.dev tasks; a skipped explanation is not a completed course exercise. Dates are ambitious targets with limited slack at 10 hours/week. Review the pace on September 26; move dependent dates if needed.

Reuse the fake-worker runner from Section 2 and the Pi extension from Section 4. Verify that interface before connecting Claude Code or Codex; start with a read-only task, then a bounded edit.

## Tasks:

- [ ] After a working adapter, compare a small Effect refactor and decide whether to adopt it (optional, at most two hours within this project's budget; split into a later project if larger)

- [ ] Build one plain TypeScript adapter for a Claude Code or Codex worker; test failure and cancellation

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-26: At the user’s request, shifted the planned start and target finish / deadline four days later (2026-11-05–2026-11-18 → 2026-11-09–2026-11-22) while they work on another project. Duration, effort allocation, task states and completion records are unchanged.

- 2026-09-13: Reforecast after Section 1 completion: JavaScript starts September 13; remaining stages shifted four days earlier with allocations unchanged at 10 focused hours/week. Pace review September 26. Dates remain forecasts.

- 2026-09-10: Compressed at the user’s request to 2026-11-09–2026-11-22, 20 hours. Prior allocations below are historical; tasks and completion states retained.

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

Optional design reading: [[Notes/Coding Agent Course/01 Material Shelf#Optional object-oriented design bridge|Grokking sequence diagrams]], 20–30 minutes only if useful for worker startup/output/failure/cancellation. Record the diagram here as evidence for the existing adapter task.

- [Claude Code programmatic usage](https://code.claude.com/docs/en/headless) or installed `codex exec --help`.
- [Node subprocess API](https://nodejs.org/api/child_process.html) and [streams guide](https://nodejs.org/learn/modules/how-to-use-streams).
- Current Pi extension API and examples.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
