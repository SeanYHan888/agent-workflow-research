---
type: course
start: 2026-09-14
deadline: 2027-05-23
created: 2026-09-10
---
# Coding-agent course — three workflows

**Start:** September 14, 2026 · **Working finish:** May 23, 2027 · **10 focused hours/week**.

Build a workflow you can use, explain, change and recover. This course joins three distinct projects: [[terminal-human-in-the-loop|terminal collaboration]], [[gui-human-in-the-loop|GUI collaboration]], and [[multi-agent-human-review|agent teamwork with final human review]]. Shared language, runtime, agent and Linux foundations are learned once.

## Start now

Open [[terminal-agent-01-agent-loop]]. Read only `agent_loop()` in `/Users/seanmacbook/Self-learn/learn-claude-code/s01_agent_loop/code.py` (currently lines 87–117). Explain who executes a tool, why the result is appended, and what stops the loop. Allow 30–45 minutes. Review those answers before the dispatcher exercise; no API setup is needed.

## Ordered project roadmap

| Order | Project and purpose | Start | Deadline | Hours |
|---|---|---|---|---:|
| 1 | [[terminal-agent-01-agent-loop\|Agent loop]] — explain request, execution and result | 2026-09-14 | 2026-09-20 | 10 |
| 2 | [[terminal-agent-02-javascript-node\|JavaScript, Node and process basics]] — build a fake-worker runner | 2026-09-21 | 2026-11-08 | 70 |
| 3 | [[terminal-agent-03-typescript-agent\|TypeScript and a small agent]] — implement typed tools, bounded turns and history | 2026-11-09 | 2026-12-27 | 70 |
| 4 | [[terminal-agent-04-pi-extension\|Real agent architecture]] — trace Tau/Pi and make one Pi extension | 2026-12-28 | 2027-01-17 | 30 |
| 5 | [[gui-human-in-the-loop\|GUI collaboration]] — compare Paseo/T3 and trace one T3 source path | 2027-01-18 | 2027-02-07 | 30 |
| 6 | [[terminal-agent-05-worker-adapter\|One real worker]] — reliable lifecycle and reviewable output | 2027-02-08 | 2027-03-07 | 40 |
| 7 | [[terminal-agent-06-linux-coordination\|Two workers and Linux recovery]] — isolation, integration and failure diagnosis | 2027-03-08 | 2027-04-18 | 60 |
| 8 | [[multi-agent-human-review\|Existing-tool team capstone]] — coordinator-led execution and final human review | 2027-04-19 | 2027-05-23 | 50 |
| | **Total, including practice/review/debugging reserve** | | | **360** |

The original section filenames remain stable; table order includes the two inserted workflow projects. Planned dates never mark work complete. A checkpoint must be demonstrated before dependent work starts; move dates when necessary.

## Why the two projects belong here

**GUI workflow:** use an interface early if helpful, then understand it after JS/TS, Node events and Pi architecture. T3 source adds a client/server/provider boundary to an already understood agent loop. Study only the React and Effect constructs encountered in that trace. A 1–2-hour optional early preview replaces workflow-practice time and is deducted from the GUI allocation, not added to the week.

**Multi-agent workflow:** first make one worker reliable, then two workers recoverable. The capstone changes who directs execution: a coordinator carries out the approved brief and presents the integrated result. The user confirmed existing tools first. It reuses earlier adapters, tests and design knowledge; it does not require building a new coordination framework. Start with two writers and a separate review pass, then justify any expansion through measured results.

Paseo, T3, Pi, OMP and Orca have different responsibilities. A tool is adopted only after its trial helps the user's work. No requirement to operate all of them together.

## Taskflow and progress

The installed and running Taskflow version was checked as **0.5.6** on September 10. Its project reader uses **start**, **deadline**, **status** and **order**. The old `start_date` property was replaced in this course's notes. Future starts defer attention in hybrid pacing; `now` overrides the future date. Dates do not enforce prerequisites or automatically complete/start a project.

- Keep one learning section `now`; the terminal workflow may also stay `now` for shared daily practice. Future sections use `next`/`later` with start dates.
- Complete tasks only in their owning project, under the exact `## Tasks:` heading. This overview deliberately has no duplicate checkboxes.
- At a checkpoint, record what you ran/built/explained and actual hours. Then promote the next project and revise dates if necessary.
- Link prerequisites in prose: this plugin version does not implement parent/child rollups or dependency enforcement.
- This navigation note lives in `Projects/`, outside Taskflow's configured `Projects/Active` scan, so it does not consume an extra active-project slot. It is not another execution backlog.

## Estimate and scope

**Working estimate: 360 hours / 36 weeks**, consisting of the prior 280-hour foundation/terminal plan + 30 hours GUI + 50 hours team trials. My uncertainty range is **300–440 hours / 30–44 weeks**, corresponding to **April 11–July 18, 2027** from the planned start. These are planning judgments, not measured course durations.

The range comes from 188–272 base hours for the original sections, 20–30 GUI hours and 40–60 team hours, plus approximately 20% reserve, rounded. The working allocation already includes reserve; do not add it again.

Review the estimate **September 27** using actual focused hours and next-session recall. Default weekly split: 6 hours hands-on, 3 reading/explanation, 1 review. Avoid running all subjects concurrently.

Includes Boot.dev JS/TS, selected Node/Bash/Linux and system-design work, Tau/Pi/Claude teaching comparisons, GUI use and focused T3 reading, plus a bounded existing-tool team. Full React training, recreating T3, adopting Effect, Rust internals, every book/course chapter, distributed fleets and a custom scheduler are follow-on scope.

## Materials and evidence

Project notes own their readings, tasks and evidence. `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md` explains the course design; `learning-resources-research.md` records source findings. Generated `agent-learning` prose is not the syllabus. Material availability and planning do not establish learning completion.

## Change record

- 2026-09-10: Integrated the existing GUI and multi-agent project notes, assigned dates, preserved original tasks, and corrected Taskflow start metadata. No learning checkpoint marked complete. Earlier March 28 course finish is superseded by this expanded scope.
