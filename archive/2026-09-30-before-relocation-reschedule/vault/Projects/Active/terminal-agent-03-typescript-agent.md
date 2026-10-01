---
type: project
status: later
area: tools
start: 2026-10-01
deadline: 2026-10-18
outcome: Use TypeScript contracts and runtime validation to build a small agent whose behavior I understand.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 9
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 3
---
# 03 — TypeScript and a small agent

**Planned start:** 2026-10-01 · **Target finish / deadline:** 2026-10-18

[[Notes/Coding Agent Course/00 Start Here|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[terminal-agent-02-javascript-node|Previous section]] · [[terminal-agent-04-pi-extension|Next section]]

Dates are study targets, not actual start/completion records. Planned allocation: **26 hours** within the shared **10 hours/week** course budget. This compact target has limited slack; reforecast if the preceding checkpoint takes longer.

## Project goal:

Use TypeScript contracts and runtime validation to build a small agent whose behavior I understand.

## Done when:

My small agent has typed tools, runtime input validation, a real provider boundary, bounded turns and saved history. I can add a tool and explain success, failure and resume.

## Start here:

**26-hour sprint:** use roughly 10 hours for fast Boot.dev TS progression, 12 for evolving the same runner into a small agent, and 4 for validation/review. Do not rebuild a separate Python agent.

**Compact pace:** attempt the checkpoint first, read only what you cannot yet explain, and reuse the existing runner/agent. Keep the recorded completion criteria and Boot.dev tasks; a skipped explanation is not a completed course exercise. Dates are ambitious targets with limited slack at 10 hours/week. Review the pace on September 26; move dependent dates if needed.

Continue from the Node runner in Section 2. Begin Boot.dev TypeScript, type its messages/results, and grow it into a small loop. Keep the implementation small; use a few mechanisms well before adding features.

## Tasks:

- [ ] Trace nanocode schema → dispatch → matching tool result → next request; compare with s02 and my TS agent, explain one failure and stopping, and record one improvement (60 minutes within review time)

- [ ] Use selected current s01/s02 examples to compare loop/tools; add permissions/hooks when the build reaches them

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

- 2026-09-26: At the user’s request, shifted the planned start and target finish / deadline four days later (2026-09-27–2026-10-14 → 2026-10-01–2026-10-18) while they work on another project. Duration, effort allocation, task states and completion records are unchanged.

- 2026-09-15: Added a focused source comparison within the existing allocation. Dates and previous task states retained; reading checkpoint is pending.

- 2026-09-13: Reforecast after Section 1 completion: JavaScript starts September 13; remaining stages shifted four days earlier with allocations unchanged at 10 focused hours/week. Pace review September 26. Dates remain forecasts.

- 2026-09-10: Compressed at the user’s request to 2026-10-01–2026-10-18, 26 hours. Prior allocations below are historical; tasks and completion states retained.

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- [nanocode pinned source](https://github.com/1rgs/nanocode/blob/b009d3dbedf14795a5c10804a5455386563f4b5b/nanocode.py) — `TOOLS`, `make_schema`, `run_tool`, then `main`; see [[Notes/Coding Agent Course/01 Material Shelf#Two focused source labs — added September 15|reading scope]].

Optional design reading: [[Notes/Coding Agent Course/01 Material Shelf#Optional object-oriented design bridge|Grokking OO analysis and class relationships]], 20–30 minutes only if responsibilities or tool-state ownership are unclear. Use the existing type/contract checkpoint; record the explanation here.

- [Boot.dev TypeScript](https://www.boot.dev/courses/learn-typescript).
- Node runner from Section 2 and selected Tau/Pi source comparisons.
- `/Users/seanmacbook/Self-learn/system-design-primer` — state ownership and interface tradeoffs.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
