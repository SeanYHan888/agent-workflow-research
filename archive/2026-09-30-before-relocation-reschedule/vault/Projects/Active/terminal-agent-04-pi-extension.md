---
type: project
status: later
area: tools
start: 2026-10-19
deadline: 2026-11-01
outcome: Read a larger agent by following behavior through its modules, then extend Pi at an appropriate boundary.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 12
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 4
---
# 04 — Real agent architecture and a Pi extension

**Planned start:** 2026-10-19 · **Target finish / deadline:** 2026-11-01

[[Notes/Coding Agent Course/00 Start Here|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[terminal-agent-03-typescript-agent|Previous section]] · [[gui-human-in-the-loop|Next — GUI workflow]]

Dates are study targets, not actual start/completion records. Planned allocation: **20 hours** within the shared **10 hours/week** course budget. This compact target has limited slack; reforecast if the preceding checkpoint takes longer.

## Project goal:

Read a larger agent by following behavior through its modules, then extend Pi at an appropriate boundary.

## Done when:

I can locate conversation/tool ownership and async event flow in current source, compare it with my small agent, and demonstrate one narrow Pi extension.

## Start here:

**Compact pace:** attempt the checkpoint first, read only what you cannot yet explain, and reuse the existing runner/agent. Keep the recorded completion criteria and Boot.dev tasks; a skipped explanation is not a completed course exercise. Dates are ambitious targets with limited slack at 10 hours/week. Review the pace on September 26; move dependent dates if needed.

Pick one behavior already understood in Section 3 and trace it in Tau and Pi. Choose later Claude teaching chapters by mechanism rather than assigning every chapter.

## Tasks:

- [ ] Trace mini-swe-agent v2 loop/model/environment boundaries, message ownership, one limit/exit path and saved trajectory; map them to my TS agent before Tau/Pi (90 minutes within source-study time)

- [ ] Trace selected Tau functions after learning the required async/process concepts
- [ ] claude code 学习
    - [ ] Select later chapters by mechanism using the refreshed 17-chapter index: context/memory s08–s09, tasks/background s10–s11, teams s13, workflow/goal s16–s17
- [ ] Implement one narrow Pi extension and explain its entry point and verification

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-26: At the user’s request, shifted the planned start and target finish / deadline four days later (2026-10-15–2026-10-28 → 2026-10-19–2026-11-01) while they work on another project. Duration, effort allocation, task states and completion records are unchanged.

- 2026-09-15: Added a focused source comparison within the existing allocation. Dates and previous task states retained; reading checkpoint is pending.

- 2026-09-13: Reforecast after Section 1 completion: JavaScript starts September 13; remaining stages shifted four days earlier with allocations unchanged at 10 focused hours/week. Pace review September 26. Dates remain forecasts.

- 2026-09-10: Compressed at the user’s request to 2026-10-19–2026-11-01, 20 hours. Prior allocations below are historical; tasks and completion states retained.

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- [mini-swe-agent pinned agent](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py), [model](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/models/litellm_model.py) and [environment](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/environments/local.py); see [[Notes/Coding Agent Course/01 Material Shelf#Two focused source labs — added September 15|reading scope]].

- `/Users/seanmacbook/Self-learn/tau`.
- `/Users/seanmacbook/Self-learn/pi`, especially the agent loop and coding-agent extension examples.
- `/Users/seanmacbook/Self-learn/learn-claude-code` — current 17-chapter index.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
