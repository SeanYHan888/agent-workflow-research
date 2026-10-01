---
type: project
status: later
area: tools
deadline: 2026-11-08
outcome: GUI — Human in the Loop workflow is documented and validated on one real task.
created: 2026-09-09
tags:
  - project-file
start: 2026-11-02
order: 11
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 5
---
# GUI — Human in the Loop

[[Notes/Coding Agent Course/00 Start Here|Course overview]] · [[terminal-agent-04-pi-extension|Previous — Pi architecture]] · [[terminal-agent-05-worker-adapter|Next — worker adapter]]

**Planned start:** 2026-11-02 · **Target finish / deadline:** 2026-11-08 · **10 hours / 1 week**, inside the shared 10 hours/week.

The required block follows JS/TS and Pi architecture. An optional 1–2-hour GUI preview after the first reviewed terminal task can replace that week's workflow practice; log it here and subtract it from this 10-hour allocation. It is not another parallel course.

## Project goal:

Learn what the interface adds around an existing harness: input, visible state, approvals, review and reconnect. Compare Paseo and T3 Code on the same small task, then study one T3 Code request-to-result path. Reuse the earlier agent and Node concepts rather than rebuilding a GUI application.

Use a graphical interface for ongoing human-agent collaboration. Paseo is the proposed GUI/mobile route; T3 Code source learning belongs here. Shared foundations remain in [[terminal-human-in-the-loop]].

### Material audit — 2026-09-09
The previously supplied [Paseo site](https://paseo.sh/) has no personal reading-completion record in the searched vault notes. Treat reading status as unknown. Review it while evaluating this workflow.

### Migration

Tasks moved from [[pi-agent]] and [[dev-setup]] on 2026-09-09. Original task wording, nesting, and completion states were retained. Workflow next steps are newly added.

Related projects: [[terminal-human-in-the-loop]], [[multi-agent-human-review]].

## Done when:

- I have tried both interfaces on comparable bounded work and selected a daily GUI with evidence about follow-up, diff review and resume.
- I can trace one T3 request through client, server, provider adapter and returned events, linking actual source files at a recorded revision.
- I can explain who owns the process and conversation, what reconnect restores, and what remains uncertain about switching from a terminal-owned session.
- I have a short workflow guide and can explain when I prefer terminal versus GUI collaboration.

## Tasks:

- [ ] 整理 T3 Code 相关视频，记录任务输入、人工介入、代码审查和交付流程

来源：[[Daily Notes/2026/09/09-18, Fri]]、[[Daily Notes/2026/09/09-24, Thu]]；2026-09-24 从补充项目合并。


**Compact pace:** attempt the checkpoint first, read only what you cannot yet explain, and reuse the existing runner/agent. Keep the recorded completion criteria and Boot.dev tasks; a skipped explanation is not a completed course exercise. Dates are ambitious targets with limited slack at 10 hours/week. Review the pace on September 26; move dependent dates if needed.

Work in this order: interface trial → source trace → workflow decision. The original task below owns the source-learning work.

- [ ] Compare Paseo and T3 Code on one bounded task; include follow-up, change review and session resume; record human minutes, review effort, interruption and reconnect behavior
- [ ] Draw the GUI/client, server, harness and checkout ownership boundaries; record the chosen workflow

- [ ] t3 code 源码学习
    - [ ] Read the current internals overview and trace one request through contracts, provider execution and returned events
    - [ ] Learn only the React and Effect concepts encountered on that path; translate one small flow into familiar plain TypeScript
    - [ ] Explain how disconnect, cancellation and an outstanding permission request affect the selected path

### Workflow next steps

The bounded comparison and workflow decision above own GUI selection and the complete task trial; do not track the same trial twice.

## Decisions and blockers:

- The user’s “pesdo” is interpreted as Paseo, matching this existing project; T3 Code means pingdotgg/t3code.
- Required prerequisite: Section 3's typed agent and Section 4's source trace. A short hands-on preview only needs the first direct-workflow checkpoint.
- T3 Code's server uses Effect and its web client uses React. A narrow reading bridge is included here; full React development and adopting Effect in our adapter remain outside the core requirement.
- T3 source reading does not establish that its providers include Pi. Use a documented common harness for the comparison. Recheck provider support and source paths when this block begins.
- Setup completion recorded in the terminal note is not evidence that the GUI study is complete.

## Resources:

- [Paseo supported agents](https://paseo.sh/agents) and [documentation](https://paseo.sh/docs).
- [T3 Code repository and user guide](https://github.com/pingdotgg/t3code), [internals overview](https://github.com/pingdotgg/t3code/blob/main/docs/internals/overview.md), and [architecture map](https://github.com/pingdotgg/t3code/blob/main/AGENTS.md).
- [Effect](https://effect.website/) — use the version required by the inspected T3 source, only for the selected trace.

## Progress log:

- 2026-09-26: At the user’s request, shifted the planned start and target finish / deadline four days later (2026-10-29–2026-11-04 → 2026-11-02–2026-11-08) while they work on another project. Duration, effort allocation, task states and completion records are unchanged.

- 2026-09-13: Reforecast after Section 1 completion: JavaScript starts September 13; remaining stages shifted four days earlier with allocations unchanged at 10 focused hours/week. Pace review September 26. Dates remain forecasts.

- 2026-09-10: Compressed at the user’s request to 2026-11-02–2026-11-08, 10 hours. Prior allocations below are historical; tasks and completion states retained.

- 2026-09-10: Integrated into the course after Pi architecture; dates and 30-hour budget assigned. Existing tasks preserved; no study completion recorded.
