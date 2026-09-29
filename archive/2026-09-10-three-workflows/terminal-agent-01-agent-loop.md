---
type: project
status: now
area: tools
start_date: 2026-09-14
deadline: 2026-09-20
outcome: Explain how a model tool request becomes program execution and how its result reaches the next model call.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 1
---
# 01 — Understand the agent loop

**Planned start:** 2026-09-14 · **Target finish / deadline:** 2026-09-20

[[terminal-human-in-the-loop|Course overview]] · First section · [[terminal-agent-02-javascript-node|Next section]]

Dates are study targets, not actual start/completion records. Planned allocation: **10 hours** within the shared **10 hours/week** course budget, including reserve. Reforecast with the overview if the preceding checkpoint takes longer.

## Project goal:

Explain how a model tool request becomes program execution and how its result reaches the next model call.

## Done when:

I can trace one complete cycle, change a harmless tool, and explain the failure and stopping paths in my own words.

## Start here:

Spend 30–45 minutes on the short explanation from our conversation, then read only `agent_loop()` in `/Users/seanmacbook/Self-learn/learn-claude-code/s01_agent_loop/code.py` (current lines 87–117). Identify the model call, tool execution, result append and stop condition. Answer: who executes the command, why append the result, and what if tool requests continue? No API call or installation is needed. Review the answers before Session 2.

## Tasks:

- [ ] Explain one tool-call cycle using a small trace, then implement/change a tiny fixture-reading dispatcher
    - [ ] Session 1: trace the cycle in s01 agent_loop and answer the three questions in my own words
    - [ ] Session 2: implement/change the fixture-reading tool and handle an unknown tool name
- [ ] Use selected current s01/s02 examples to compare loop/tools; add permissions/hooks when the build reaches them

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- `/Users/seanmacbook/Self-learn/learn-claude-code/s01_agent_loop/code.py` — selected function only.
- `/Users/seanmacbook/Self-learn/agent-learning/tau/src/tau_agent/loop.py` — narrow source comparison after the simple trace.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
