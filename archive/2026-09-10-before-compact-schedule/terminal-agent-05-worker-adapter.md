---
type: project
status: later
area: tools
start: 2027-02-08
deadline: 2027-03-07
outcome: Connect Pi to one real coding harness through an explicit, observable worker interface.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 6
---
# 05 — Delegate to one real worker

**Planned start:** 2027-02-08 · **Target finish / deadline:** 2027-03-07

[[coding-agent-course|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[gui-human-in-the-loop|Previous — GUI workflow]] · [[terminal-agent-06-linux-coordination|Next section]]

Dates are study targets, not actual start/completion records. Planned allocation: **40 hours** within the shared **10 hours/week** course budget, including reserve. Reforecast with the overview if the preceding checkpoint takes longer.

## Project goal:

Connect Pi to one real coding harness through an explicit, observable worker interface.

## Done when:

The adapter handles output, failure, timeout, cancellation and needs-input. A bounded real edit returns an actual diff and check results for human review.

## Start here:

Reuse the fake-worker runner from Section 2 and the Pi extension from Section 4. Verify that interface before connecting Claude Code or Codex; start with a read-only task, then a bounded edit.

## Tasks:

- [ ] Build one plain TypeScript adapter for a Claude Code or Codex worker; test failure and cancellation

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- [Claude Code programmatic usage](https://code.claude.com/docs/en/headless) or installed `codex exec --help`.
- [Node subprocess API](https://nodejs.org/api/child_process.html) and [streams guide](https://nodejs.org/learn/modules/how-to-use-streams).
- Current Pi extension API and examples.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
