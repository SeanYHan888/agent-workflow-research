---
type: project
status: now
area: tools
start: 2026-09-17
deadline: 2026-10-02
outcome: Write JavaScript programs that read files and start, observe and stop another program.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 4
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 2
---
# 02 — JavaScript, Node.js and process basics

**Planned start:** 2026-09-17 · **Target finish / deadline:** 2026-10-02

[[Notes/Coding Agent Course/00 Start Here|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[terminal-agent-01-agent-loop|Previous section]] · [[terminal-agent-03-typescript-agent|Next section]]

Dates are study targets, not actual start/completion records. Planned allocation: **20 hours** within the shared **10 hours/week** course budget. This compact target has limited slack; reforecast if the preceding checkpoint takes longer.

## Project goal:

Write JavaScript programs that read files and start, observe and stop another program.

## Done when:

I can explain and modify a task-file CLI and fake-worker runner, including failed startup, nonzero exit, streamed output and basic cancellation.

## Start here:

**Available now, September 13:** Begin Boot.dev JavaScript Variables, then values/types, conditions, functions and objects. Section 1 is complete.

**Two-week sprint:** about 8 hours for fast Boot.dev JS progression, 8 hours for the Node runner, and 4 hours for Bash, failure cases and review. These are provisional timeboxes; keep unfamiliar async/process concepts explicit. Extra YDKJS depth can wait until a concrete question needs it.

**Compact pace:** attempt the checkpoint first, read only what you cannot yet explain, and reuse the existing runner/agent. Keep the recorded completion criteria and Boot.dev tasks; a skipped explanation is not a completed course exercise. Dates are ambitious targets with limited slack at 10 hours/week. Review the pace on September 26; move dependent dates if needed.

A short Boot.dev Variables session can start alongside Section 1. The main block begins here: follow JavaScript in order; add Node CLI/files after functions, objects, errors and modules, then async I/O after promises. The runner remains JavaScript until Section 3.

## Tasks:

- [ ] Complete Boot.dev JavaScript; apply async, errors, and modules in a small CLI
- [ ] Use selected You Don't Know JS chapters to explain scope, closures, modules, and relevant runtime behavior
- [ ] Learn Node.js through the official Learn guides and a small task runner
    - [ ] After JS prerequisites, run a CLI with arguments/environment and read/write task JSON files
    - [ ] Explain async I/O and launch a fake worker, handling startup failure, stdout/stderr and exit/close
    - [ ] Read streamed JSONL across chunk boundaries, limit retained output and verify cancellation
    - [ ] Add meaningful failure/timeout checks, then reuse the runner for the TS agent and real worker adapter
- [ ] bash course https://course.ysap.sh/
    - [ ] Practice quoting, pipes, exit codes, arguments, and traps in a launcher that handles spaces and interruption

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-26: At the user’s request, shifted the planned start and target finish / deadline four days later (2026-09-13–2026-09-28 → 2026-09-17–2026-10-02) while they work on another project. Duration, effort allocation, task states and completion records are unchanged.

- 2026-09-13: Reforecast after Section 1 completion: JavaScript starts September 13; remaining stages shifted four days earlier with allocations unchanged at 10 focused hours/week. Pace review September 26. Dates remain forecasts.

- 2026-09-10: Compressed at the user’s request to 2026-09-17–2026-09-30, 20 hours. Prior allocations below are historical; tasks and completion states retained.

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- [Boot.dev JavaScript](https://www.boot.dev/courses/learn-javascript).
- [Node.js Learn](https://nodejs.org/learn/getting-started/introduction-to-nodejs) and [subprocess API](https://nodejs.org/api/child_process.html).
- [YSAP Bash](https://course.ysap.sh/).
- `/Users/seanmacbook/Self-learn/You-Dont-Know-JS` — selected scope/closure explanations.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
