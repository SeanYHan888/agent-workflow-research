---
type: project
status: later
area: tools
start: 2026-11-09
deadline: 2026-12-27
outcome: Use TypeScript contracts and runtime validation to build a small agent whose behavior I understand.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 3
---
# 03 — TypeScript and a small agent

**Planned start:** 2026-11-09 · **Target finish / deadline:** 2026-12-27

[[coding-agent-course|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[terminal-agent-02-javascript-node|Previous section]] · [[terminal-agent-04-pi-extension|Next section]]

Dates are study targets, not actual start/completion records. Planned allocation: **70 hours** within the shared **10 hours/week** course budget, including reserve. Reforecast with the overview if the preceding checkpoint takes longer.

## Project goal:

Use TypeScript contracts and runtime validation to build a small agent whose behavior I understand.

## Done when:

My small agent has typed tools, runtime input validation, a real provider boundary, bounded turns and saved history. I can add a tool and explain success, failure and resume.

## Start here:

Continue from the Node runner in Section 2. Begin Boot.dev TypeScript, type its messages/results, and grow it into a small loop. Keep the implementation small; use a few mechanisms well before adding features.

## Tasks:

- [ ] 找个时间专门再学习下js/ts
    - [ ] Complete Boot.dev TypeScript; implement typed tasks/events and a local subprocess adapter
- [ ] 之前搞的agent学习文件夹
    - [ ] Build a small typed agent and compare its mechanisms with Pi; generated chapter completion is not required
- [ ] Define component responsibilities, adapter contracts, and task/session state

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- [Boot.dev TypeScript](https://www.boot.dev/courses/learn-typescript).
- Node runner from Section 2 and selected Tau/Pi source comparisons.
- `/Users/seanmacbook/Self-learn/system-design-primer` — state ownership and interface tradeoffs.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
