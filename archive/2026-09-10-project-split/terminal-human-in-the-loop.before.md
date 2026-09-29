---
type: project
status: now
area: tools
deadline:
outcome: Build, understand, and validate a personal terminal agent workflow with Herdr, Pi, Claude Code, and Codex, supported by JS/TS and Bash/Linux skills.
created: 2026-09-09
tags:
  - project-file
order: -1
---
# Terminal — Human in the Loop

## Project goal:

Build a terminal coding-agent workflow that suits me, and learn enough to understand, modify, and operate it.

1. **Personal workflow:** use cmux or Ghostty → Herdr for persistent terminal sessions; evaluate Pi with DeepSeek V4.1 Flash as coordinator for Claude Code and Codex. Start with one direct task, then one worker, then bounded parallel work.
2. **Agent construction:** study Tau/Pi source and selected learn-claude-code examples; treat generated agent-learning prose as untrusted reference; integrate system-design exercises for interfaces, state, queues, reliability, and observability. Codex is a worker; Rust source study is deferred.
3. **Progress:** use this note as the source of current status, tasks, decisions, and completion evidence.
4. **JS/TS:** use Boot.dev JavaScript then TypeScript, with selected You Don't Know JS Yet readings for depth; apply them to the agent exercises. Evaluate Effect after a working plain TypeScript adapter.
5. **Bash/Linux:** use YSAP for Bash and Linux Foundation LFS101 for Linux foundations, then agent-specific process, SSH, service, logging, and container labs.

### Current status — course redesign, 2026-09-10

- **Confirmed baseline:** I can write small Python scripts; async, subprocesses and larger codebases are unfamiliar. No learning checkpoint completed yet.
- **Source correction:** the generated agent-learning chapters were unclear and poorly designed; they are no longer the syllabus. Keep Tau/Pi source as useful references. Existing mini-agent code is an unverified reference, not my completed work.
- **Active step:** understand one tool-call cycle through a small explicit trace. Teach prerequisites before tracing full async implementations.
- **Two connected paths:** use one harness in Herdr on real tasks while building understanding. Main construction progresses through JS/Node → small typed agent → Pi extension → one worker → bounded coordination and Linux recovery.
- **Teaching method:** one concrete question, explanation, prediction, run, trace, small change, then explanation in my own words. Expand only the active step; verify retention next session.
- Terminal practice is recorded in the repository. Pi/DeepSeek and cross-harness delegation remain untested; earlier setup checkboxes do not establish end-to-end validation.

### Material versions and Herdr — 2026-09-10

- Git-fetched all six local repositories and fast-forwarded where needed; every HEAD matches its upstream default branch. Local Finder files preserved.
- Tau: `55df516` (source package 0.4.2); Pi: `d12cd92` (coding-agent source package 0.85.1); learn-claude-code: `0dcafa2` (**17 current chapters**).
- System Design Primer: `ae9bbd7`; System Design 101: `b28380a` (already current); You Don't Know JS: `044120e` (2nd-ed).
- SDE roadmap and YSAP Git upstreams checked; they remain linked materials without local checkouts. Boot.dev, LFS101 and Effect are live websites, not local repositories. The generated agent-learning parent has no Git upstream.
- Herdr client was already 0.9.0. With my explicit approval to stop its pane processes, restarted only terminal-practice from server 0.8.0 to **0.9.0**. Client/server protocol 22 now compatible; no restart required. Attach with `herdr --session terminal-practice`; UI/layout restoration remains to be checked.
- Update evidence: `/Users/seanmacbook/Projects/agent-workflow-research/material-versions.md`. This is source/software maintenance, not learning completion.

### Start here — opening block

1. Trace a scripted request to read a fixture file: user request → model tool request → harness executes a function → result → next model input. Explain who owns each action.
2. Implement/change a tiny Python tool dispatcher and handle an unknown tool. Use a harmless fixture rather than general shell execution.
3. Locate the same dispatch/result mechanism in selected Tau source and compare learn-claude-code s01. Add a small async prerequisite exercise before tracing event streams.

One supporting Boot.dev JavaScript session supplies pace information. Record focused time, difficulty and what I can explain at the next session. These sessions are planned, not completed.

Course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Resources and source observations: `learning-resources-research.md` in the same repository. This note owns tasks and evidence.

### Resource roles

- **Tau/Pi:** real agent code to investigate by behavior; no front-to-back reading requirement.
- **learn-claude-code:** selected teaching examples, not Anthropic's internal source; study actual Claude Code behavior separately.
- **Boot.dev JS then TS:** main language courses. **You Don't Know JS:** targeted depth when a runtime question arises; its unfinished second-edition async book is not the async course.
- **[Node.js Learn](https://nodejs.org/learn/getting-started/introduction-to-nodejs) + [API reference](https://nodejs.org/api/child_process.html):** required runtime material. CLI/environment → files → async I/O → subprocesses → streams → cancellation/checks. Begin after relevant JS basics in Step 2, reuse in Step 3, deepen for Step 5 workers. Selected readings and practice checkpoints are in the repository resource catalog.
- **YSAP / LFS101:** Bash and Linux foundations, with process basics early and Linux operations later.
- **System Design Primer:** tradeoffs; **System Design 101:** visual reinforcement; **SDE interview roadmap:** optional reference. Introduce design through concrete state, queue, retry and recovery problems.
- **Herdr:** terminal continuity and daily practice. **Effect:** optional comparison after a working plain-TS adapter. Codex remains a worker without requiring Rust study.

### Course roadmap and schedule — confirmed 10 hours/week

**User confirmed September 10: 10 focused hours/week.** Estimated selected course scope: **230–330 hours / 23–33 weeks**. Working allocation: **280 hours / 28 weeks**, including review/debugging reserve. First full week September 14, 2026; working finish **March 28, 2027**, with a planning range **February 21–May 2, 2027**. These are provisional forecasts, not completed work or a fixed deadline.

| Working dates | Section goal | Evidence to produce |
|---|---|---|
| Sep 14–20, 2026 | 1. Understand one tool cycle — active | Trace request/execution/result, modify a harmless tool, explain failure/stop |
| Sep 21–Nov 8 | 2. Learn JS, Node and process basics | Task-file CLI and fake worker with output/error/cancellation handling |
| Nov 9–Dec 27 | 3. Learn TS and build a small agent | Typed/validated tools, bounded loop, real provider, saved history; explain and change it |
| Dec 28–Jan 17, 2027 | 4. Investigate real agents and extend Pi | Selected source traces and one narrow extension |
| Jan 18–Feb 14 | 5. Delegate to one real worker | One real harness adapter with reviewable edits, checks and failure handling |
| Feb 15–Mar 28 | 6. Coordinate and recover on Linux | Second adapter, two isolated workers, verified integration and Linux recovery demonstration |

Daily harness/Herdr use starts early; aim for one reviewed direct task in the opening three weeks, subject to setup/access. This is inside the weekly budget. Bash/Linux basics start with process work; system-design readings enter when the build presents a state, queue or recovery problem.

Default weekly mix: 6 hours practice, 3 hours reading/explanation, 1 hour review/evidence. Review on September 27, or after the opening block if later, using actual time and next-session recall. Adjust the remaining dates as needed. No Calendar events were created.

Includes full Boot.dev JS/TS and selected Node, Bash/Linux, source-reading and system-design work. Exhaustive books, all Linux/Claude teaching lessons, Effect and Rust internals are outside the estimate. The earlier April 11 forecast is historical. Detailed assumptions and workload totals are in repository ROADMAP.md.

### Material audit — 2026-09-09
- The unchecked video https://www.youtube.com/watch?v=iQyg-KypKAA&t=736s is **L8 Principal's Agentic Engineering Workflow**. Prioritize this for the existing agent-instructions/skills task; also relevant to delegated work.
- https://www.youtube.com/@mattpocockuk/videos is a channel backlog, not one finishable video. Pick a specific JS/TS lesson when tackling the existing learning task.
- The unchecked video https://www.youtube.com/watch?v=9tGrhrVKCrE is **Why I’m moving to Linux (for real)**. Optional environment background; its title does not establish relevance to agent instructions. Preserved under its original parent to retain task context.
- The supplied [Ghostty post](https://x.com/alin_zone/status/2033524177295274496) is already checked in [[Daily Notes/2026/03/03-16, Mon]]. Do not add it again as unfinished.
- Unchecked means no completion recorded in these notes, not verified YouTube watch history.

### Migration

Tasks moved from [[pi-agent]] and [[dev-setup]] on 2026-09-09. Original task wording, nesting, and completion states were retained. Workflow next steps are newly added.

Related projects: [[gui-human-in-the-loop]], [[multi-agent-human-review]].

## Done when:

- I can explain and modify the transcript, tool loop, provider boundary, events, and session behavior in the study agents.
- I can write a typed worker adapter with structured results, cancellation, failure handling, and process cleanup.
- Pi completes a real direct task and coordinates Claude Code/Codex on a bounded task with reviewable diffs and passing relevant checks.
- The workflow can be interrupted, resumed or recovered, and operated on a Linux lab host with understandable logs and permissions.
- Decisions and demonstrated progress are recorded here, with links to evidence.

## Tasks:

**Follow this queue, not every checkbox top-to-bottom.** Parent tasks describe study areas spanning several sections. Complete only the relevant child exercise; mark a parent complete only when its intended scope is demonstrated.

1. **Today, 30–45 minutes:** use the short explanation in our conversation, then read only `agent_loop()` in `/Users/seanmacbook/Self-learn/learn-claude-code/s01_agent_loop/code.py` (current lines 87–117). Trace a file-read request and answer: who executes the tool, what changes in the messages, and what makes this example stop? No API call or installation. Record the explanation before checking the first-session task.
2. **Next agent session:** after feedback on that explanation, implement/change a tiny Python fixture-reading tool and dispatcher. Then locate the mechanism in selected Tau source; introduce async before following its event stream.
3. **Next language session:** start Boot.dev JavaScript with Variables; continue its sequence in later sessions. Do not start TS, Node subprocesses or YDKJS depth simultaneously.
4. **Early practical session:** reattach Herdr 0.9.0 and recheck pane/detach controls; then choose one direct harness task. Pi setup/direct use can happen early; its worker-adapter and second-harness children wait for Sections 5–6. Bash basics fit alongside this work.
5. **Section 2 onward:** add Node CLI/files once JS functions, objects, errors and modules are understood; learn promises before async labs. Follow with Boot.dev TS and the small typed agent in Section 3. Use YDKJS for specific questions.
6. **Sections 4–6:** deeper Tau/Pi reading and extension → one real worker adapter → second adapter and Linux recovery. Introduce design questions and Linux fundamentals as needed; defer advanced labs until their build step.

I will get short guided lessons for agent mechanisms and project bridges; Boot.dev supplies the language lessons, and official/source material supplies targeted readings. No bulk generated textbook. The separate skill-setup draft remains pending its existing review; it does not block today's lesson.

### 1. Current study — selected exercises, not whole parent tasks

- [ ] 之前搞的agent学习文件夹
    - [ ] Explain one tool-call cycle using a small trace, then implement/change a tiny fixture-reading dispatcher
        - [ ] Session 1: trace the cycle in s01 agent_loop and answer the three questions in my own words
        - [ ] Session 2: implement/change the fixture-reading tool and handle an unknown tool name
    - [ ] Trace selected Tau functions after learning the required async/process concepts
    - [ ] Build a small typed agent and compare its mechanisms with Pi; generated chapter completion is not required
- [ ] claude code 学习
    - [ ] Use selected current s01/s02 examples to compare loop/tools; add permissions/hooks when the build reaches them
    - [ ] Select later chapters by mechanism using the refreshed 17-chapter index: context/memory s08–s09, tasks/background s10–s11, teams s13, workflow/goal s16–s17
- [ ] 找个时间专门再学习下js/ts
    - [ ] Use selected You Don't Know JS chapters to explain scope, closures, modules, and relevant runtime behavior
    - [ ] Complete Boot.dev JavaScript; apply async, errors, and modules in a small CLI
    - [ ] Complete Boot.dev TypeScript; implement typed tasks/events and a local subprocess adapter
    - [ ] After a working adapter, compare a small Effect refactor and decide whether to adopt it

### 2. Early practical sessions — alongside study

- [ ] Validate Herdr as the terminal session layer for the Pi workflow
    - [ ] Practice named-session detach/reattach and pane controls using the existing HERDR.md guide
    - [ ] Run the first Pi task inside Herdr; verify session continuity after detach/reattach
    - [ ] Verify remote attachment alongside the Termius/Tailscale task and document daemon/host restart recovery separately
- [ ] bash course https://course.ysap.sh/
    - [ ] Practice quoting, pipes, exit codes, arguments, and traps in a launcher that handles spaces and interruption
- [ ] Validate Pi + DeepSeek V4.1 Flash on one real task
    - [ ] Install/configure Pi and verify the available DeepSeek model; current API name is `deepseek-flash`
    - [ ] Test tool use, interruption, and session resume; record result and review effort
    - [ ] Build one plain TypeScript adapter for a Claude Code or Codex worker; test failure and cancellation
    - [ ] Add the second harness, then two separate worktrees and integrated verification

### 3. After the relevant JavaScript basics

- [ ] Learn Node.js through the official Learn guides and a small task runner
    - [ ] After JS prerequisites, run a CLI with arguments/environment and read/write task JSON files
    - [ ] Explain async I/O and launch a fake worker, handling startup failure, stdout/stderr and exit/close
    - [ ] Read streamed JSONL across chunk boundaries, limit retained output and verify cancellation
    - [ ] Add meaningful failure/timeout checks, then reuse the runner for the TS agent and real worker adapter

### 4. Develop during later builds

- [ ] Apply focused system design to the personal agent workflow
    - [ ] Define component responsibilities, adapter contracts, and task/session state
    - [ ] Design bounded queues and demonstrate retry/duplicate-task handling
    - [ ] Explain logs, access boundaries, and recovery in a final architecture walkthrough
- [ ] Learn Linux for agent operations using LFS101 and focused labs
    - [ ] Complete command line, permissions, processes, user environment, networking, and security foundations
    - [ ] Demonstrate SSH, signals, services/logs, resource limits, and container/workspace boundaries in a designated lab environment

### 5. Optional setup backlog — not a prerequisite for today

- [ ] 手机通过termius + tailscale 连接
- [ ] cofig agent.md, claude.md, skills
	- [ ] https://www.youtube.com/watch?v=iQyg-KypKAA&t=736s
	- [ ] https://www.youtube.com/@mattpocockuk/videos
	- [ ] https://www.youtube.com/watch?v=9tGrhrVKCrE

### Completed — previous records

- [x] config herdr, claude code (remote access), cmux, t3 code ✅ 2026-09-09
- [x] change key bilnding for ghosty and cmux, also check if there is anyuse like super key for right three function keys ✅ 2026-09-09
- [x] 管理下ssh的instance，codex，vscode ✅ 2026-08-22
- [x] herdr 和 claude code，彻底摆脱cc desktop这个大屎坑 ✅ 2026-09-09

## Decisions and blockers:

- **User clarification, 2026-09-10:** include Herdr explicitly. Terminal stack: cmux or Ghostty → Herdr → Pi. Herdr manages persistent terminals; Pi coordinates workers. Visible worker panes are an interface choice, not automatic orchestration.
- **User direction, 2026-09-10:** Pi + DeepSeek V4.1 Flash is the initial workflow hypothesis. Keep Claude Code and Codex as worker harnesses. Actual fit must be demonstrated on personal tasks.
- **Current sequence:** tool-cycle trace → JS/Node process runner → small typed agent → selected Tau/Pi investigation and extension → one worker → bounded coordination/Linux recovery. Daily use in Herdr and OS basics start early.
- Pi's bundled subagent example launches Pi processes. Claude Code/Codex orchestration requires an adapter or evaluated extension; choosing their model names alone does not launch their harnesses.
- Keep one writer per checkout and one owner per session. Use separate worktrees for simultaneous edits and test the integrated result.
- Effect is optional later. LFS101 is the recommended Linux foundation; add practical labs because one introductory course is not complete operational coverage.
- Weekly capacity is confirmed at 10 focused hours. Current provisional estimate is 230–330 hours, working finish March 28, 2027; calibrate September 27. Model credentials, Linux lab host and API budget are resolved when their exercises begin.
- After each session, update the relevant task, add dated evidence, and choose one next action. Do not duplicate completion tracking in repository documents.

### Progress log

- 2026-09-10: Added an explicit today/next/later study queue, grouped existing task areas by when they apply, and split the opening exercise into two session checkpoints. Today is a short source trace; no lesson completion recorded.

- 2026-09-10: User confirmed 10 focused hours/week. Consolidated six-section roadmap with goals/checkpoints, 230–330-hour range and 280-hour working schedule (Sep 14–Mar 28). Included Node/Bash/Linux/design practice within section budgets; no learning completion recorded.

- 2026-09-10: Added official Node.js Learn and API references with a selected CLI/files/async/process/streams/cancellation practice sequence. Fills Step 2 and supports later adapters; active Step 1 unchanged. No new completion or runtime installation recorded.

- 2026-09-10: Updated five material checkouts; System Design 101 was already current. Verified all six upstream heads and preserved local files. Corrected current Claude teaching track to 17 chapters. Restarted terminal-practice to Herdr 0.9.0 with explicit approval; verified matching client/server protocols. No learning task marked complete.

- 2026-09-10: Redesigned from capabilities and prerequisites after confirming the old generated course was unclear and ineffective. Confirmed Python baseline: small scripts, unfamiliar async/subprocesses/larger codebases. Superseded the assistant-added 01–05 / 06–08 / 09–18 chapter tasks with behavior-based tasks; no task marked complete. Archived the old roadmap and retired its date forecast. Current work is Step 1's three-session pilot.

- 2026-09-10: Audited the four additional resources and integrated focused system design plus selected YDKJS reading. Revised working estimate: 300 hours at provisional 10 hours/week; core Jan 17, coordination Feb 14, final Apr 11, 2027. Original dates below are historical forecasts. No learning completion recorded.
- 2026-09-10: Added provisional dated milestones at 10 hours/week: core learning Jan 3, orchestration Jan 31, full-project working target Mar 14, 2027. Pace review Sep 27; no learning completion recorded.
- 2026-09-10: Expanded the roadmap into six stages with readiness checks and the first five study sessions. Session 1 is prepared; user completion remains pending.
- 2026-09-10: Audited existing materials and project context; recorded the five goals, early-stage study baseline, recommended sequence, and acceptance criteria. No learning exercise or live model integration marked complete.

## Resources:

- Repository: `/Users/seanmacbook/Projects/agent-workflow-research`; design and milestones in `ROADMAP.md`, cited course research in `learning-resources-research.md`.
- Legacy generated material (not required): `/Users/seanmacbook/Self-learn/agent-learning/README.md`. Tau and Pi source remain selected references.
- Claude teaching course: `/Users/seanmacbook/Self-learn/learn-claude-code/README.md` (current root-level s01–s17).
- [Herdr persistence/remote access](https://herdr.dev/docs/persistence-remote/) · [Pi](https://pi.dev/) · [Tau](https://github.com/huggingface/tau) · [Claude Code programmatic usage](https://code.claude.com/docs/en/headless).
- [DeepSeek model identifier and API](https://api-docs.deepseek.com/).
- [Boot.dev JavaScript](https://www.boot.dev/courses/learn-javascript) · [Boot.dev TypeScript](https://www.boot.dev/courses/learn-typescript).
- [Node.js Learn](https://nodejs.org/learn/getting-started/introduction-to-nodejs) · [Node subprocess API](https://nodejs.org/api/child_process.html) — required runtime material.
- [Effect](https://effect.website/) — optional later; use documentation matching the chosen release.
- [YSAP Bash](https://course.ysap.sh/) · [Linux Foundation LFS101](https://training.linuxfoundation.org/training/introduction-to-linux/).
