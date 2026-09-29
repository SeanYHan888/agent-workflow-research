---
title: Coding Agent Course — Study Route
created: 2026-09-11
tags:
  - learning/coding-agents
---
# Your study route

[[Notes/Coding Agent Course/00 Start Here|Start Here]] · [[Notes/Coding Agent Course/01 Material Shelf|All material links]] · [[Projects/coding-agent-course|Schedule and projects]]

The agreed order is below. Only the first block has a detailed handout today; later lessons will be prepared around your demonstrated understanding. Each project link owns its tasks and evidence.

| Stage | Read and study | Produce or demonstrate | Progress owner |
|---|---|---|---|
| 1. One tool cycle · 4h | [[Notes/Coding Agent Course/03 One Tool Cycle\|Current handout]], s01, then selected s02/Tau | Explain the full cycle, change a fixture-reading tool, handle an unknown tool | [[Projects/Active/terminal-agent-01-agent-loop\|Agent loop]] |
| 2. JavaScript and Node · 20h | Boot.dev JS; selected Node Learn/API; YDKJS for gaps; early YSAP | Task-file CLI and fake-worker runner with output, startup failure, nonzero exit and basic cancellation | [[Projects/Active/terminal-agent-02-javascript-node\|JS and Node]] |
| 3. Small TypeScript agent · 26h | Boot.dev TS; s01/s02 plus a 60-minute nanocode dispatch comparison; optional OOD responsibility/class reading; provider documentation at the implementation boundary | Typed messages/tools, runtime input validation, bounded turns, saved history and a real provider boundary | [[Projects/Active/terminal-agent-03-typescript-agent\|TS agent]] |
| 4. Real agent architecture · 20h | 90-minute mini-swe-agent loop/model/environment trace, then selected Tau/Pi files and Pi extensions; relevant learn-claude-code mechanisms | Trace state/events in source, compare to your agent and write one narrow extension | [[Projects/Active/terminal-agent-04-pi-extension\|Pi extension]] |
| 5. GUI workflow · 10h | Paseo/T3 user material, then one T3 internals path | Compare a bounded task, follow-up, review and reconnect; explain client/server/provider ownership | [[Projects/Active/gui-human-in-the-loop\|GUI workflow]] |
| 6. One real worker · 20h | Pi extension API, chosen worker's official interface, Node processes/streams; optional OOD sequence diagram | Fake adapter → read-only worker → bounded edit; failure, partial output, timeout, cancellation and needs-input | [[Projects/Active/terminal-agent-05-worker-adapter\|Worker adapter]] |
| 7. Linux and two workers · 30h | Selected LFS101/YSAP, operations/worktree docs, Primer/101 failure topics | Second adapter, isolated edits, bounded concurrency, integration checks and Linux failure/recovery | [[Projects/Active/terminal-agent-06-linux-coordination\|Linux and coordination]] |
| 8. Existing-tool team · 30h | Selected team tool's documentation; reuse earlier design and recovery work | Coordinator, two writers, separate review pass, integrated evidence, failed-worker recovery and two measured trials | [[Projects/Active/multi-agent-human-review\|Team capstone]] |

These are eight positions in the course, while the foundation project filenames retain their original 01–06 numbering. The GUI project sits between foundation sections 4 and 5; the team project follows section 6.

**Total: 160 hours at 10 hours/week.** Forecast dates and the September 26 pace check live in [[Projects/coding-agent-course|the existing course overview]]. Terminal/Herdr practice and supporting readings count inside these hours. Reuse the same small task and evolving implementation.

For every checkpoint, record what you ran, changed or explained; link the evidence and record actual focused time. Advance when ready. If an important gap remains, update the forecast instead of treating a date or a downloaded resource as completion.

## Extended research route — September 28, 2026

The [long-term expansion](</Users/seanmacbook/Projects/agent-workflow-research/expanded-research-plan.md>) adds three connected tracks alongside and after the foundation stages above:

1. Official Claude courses with demonstrations in the user's real workflows.
2. Small agents and Pi → Rust reading bridge → Codex source, plus focused OpenCode and local Claude snapshot comparisons.
3. Python/tensor and attention foundations → generation/KV cache → memory and kernels → scheduling/vLLM → advanced serving and benchmarks.

Bring the tracks together by connecting the existing agent to a model server and explaining measured latency, memory, correctness and failure handling. The old 160-hour total applies to the foundation only. No exam deadline governs this expanded route; check demonstrated prerequisites before advancing and retain Obsidian as the owner of progress.
