# Project context

This file preserves the working decisions from the Codex task **Design terminal agent workflows** (`01a0886a-08d4-7c70-9f4d-a62bc3494115`). Read this first when continuing in a new task. A readable conversation snapshot is in CHAT-HISTORY.md; it is not a native Codex history import.

## Location and user preference

Project root: `/Users/seanmacbook/Projects/agent-workflow-research`.
The user reserves Documents for personal information. Keep this project and its new artifacts in Projects. The directory was moved from Documents on 2026-09-09; five files were verified byte-for-byte before updating embedded paths.

## Objective

### TypeScript plugin lab — 2026-09-28

The user asked to learn TypeScript by improving their own Obsidian plugin, Daily Task Panel (`/Users/seanmacbook/Projects/obsidian-taskflow`), and said this study is part of the course and must respect its schedule and project method. [typescript-plugin-lab.md](typescript-plugin-lab.md) owns the design: an optional follow-on on the Coding Agent Course roadmap (sequence 12), entry gate Boot.dev TypeScript through unions and narrowing, hours taken from the shared 10 hours/week only when activated, and a route of stages 01–08 where only stage 01 has a project. Obsidian project: `Projects/Active/ts-panel-01-strict-flags.md`, status `later` with no dates. A separate roadmap note created earlier the same session was moved to the vault's `.trash` because the course keeps a single roadmap. Activation date and which planned hours it replaces remain the user's decision. No study, code change or learning completion occurred. The session's output style was switched to Learning at the user's request.

### Long-term study expansion — 2026-09-28

The user explicitly set aside the certification deadline for learning and requested three additions: official Claude courses; Codex CLI source plus recommended open-source agents and their local Claude Code snapshot; and model inference from KV cache through vLLM. [expanded-research-plan.md](expanded-research-plan.md) owns the detailed additions and connects them to the foundation roadmap.

The core source route is mini-swe-agent → Pi → Codex, with a Rust reading bridge, short nanocode/Tau comparisons and optional OpenCode. Inference progresses from tensor/attention foundations through generation, KV memory, kernels, scheduling, serving, quantization, speculative decoding, parallelism and operational benchmarks. The shared capstone connects the existing agent to a model server and measures both layers.

The original 160 hours and dates describe the earlier foundation forecast only. New scope is self-paced with no new calendar commitment or inferred completion. Last recorded JS/Node status remains unchanged; check current Obsidian evidence before assigning later foundation work. Student notes and task states were not rewritten by this repository update.

Located `/Users/seanmacbook/Projects/claude-code/src`; root has no Git history, README or package manifest. Treat it as a user-supplied unverified snapshot, with provenance/hash capture at the first source lesson. Located nanochat at `/Users/seanmacbook/Projects/nanochat`, revision `d5759400f96789d7649e040e5f444790101baa21`; model and engine files are proposed inference readings. No repository update, installation or compute job occurred. Next sessions: the official subagent course using the monitoring skill as an example, and an inference prerequisite/one-token walkthrough.

### Parallel autonomous pipeline plan — 2026-09-24

The user confirmed both coding jobs and research reports as target workloads, with an additional 3–5 focused hours/week alongside the existing learning/terminal workflow. See [autonomous-job-pipeline-plan.md](autonomous-job-pipeline-plan.md) for the draft: one bounded job at a time, explicit acceptance checks, limited repair, durable recovery and human decisions for meaningful ambiguity or consequential actions. This allows a small existing-tool pilot before the later multi-agent course capstone. The user selected `phicil-itate/listen-phirst` dashboard work; [the pilot brief](listen-phirst-dashboard-pilot.md) maps live issues #23–27 and the `test` branch instructions. The user chose patient-first using the existing patient session. Exact patient-visible fields in scope issue #23 remain unresolved; a research decision packet precedes one approved patient coding slice. Execution budgets remain open. Existing course dates and Obsidian task states were not changed by drafting; no unattended job was launched.

### Source additions — 2026-09-15

Added user-requested nanocode (Section 3, 60 minutes) and mini-swe-agent v2 (Section 4, 90 minutes) as focused source comparisons inside existing review/source-study hours. Pinned revisions and exact symbols are in learning-resources-research.md. Updated classroom materials and the corresponding Obsidian reading/project notes. JS/Node remains active; all dates, 160 total planned hours and prior task states are preserved. No agents installed or run, and no learning completion inferred.

### Teaching progress and reforecast — 2026-09-13

Section 1 completed through guided explanation and verified real-file dispatcher outputs in self-practice/tool_dispatch.py. Obsidian section status is done; JavaScript is now (September 13–26), TypeScript next (September 27–October 14). Following stages shifted four days earlier; course finish December 30, pace review September 26. Hour allocations unchanged; actual study hours unknown. Uncompleted s01/s02 comparison moved to the TypeScript task list. This supersedes earlier active-section and schedule statements below.

### Material refresh — September 11, 2026

Pulled all seven linked repositories with fast-forward-only Git pulls and verified HEAD against each remote default branch. Pi advanced 7 commits to `71dca871bc80`; Grokking advanced 25 to `ba7927f641f2`; the other five were already current. Current readings and the opening s01 anchor are unchanged. Grokking now includes newer implementations/tests, so do not repeat the earlier blanket non-executable description. Its unrelated Java example has a case-only README/readme collision on this Mac; both originals are preserved in the classroom. See [material-versions.md](material-versions.md) and its JSON evidence. No tools were installed or learning tasks completed.

### Classroom and student reading room — 2026-09-11

Follow-up: the user explicitly requested complete removal of `Self-learn/agent-learning` after extracting Tau and Pi. Both repositories now live directly at `/Users/seanmacbook/Self-learn/tau` and `/Users/seanmacbook/Self-learn/pi`; all file/symlink manifests and Git HEADs were verified across the move. The remaining generated chapters, README and mini-agent were deleted. Current course links were repaired; archived records describe their historical locations.

The reading room now also includes `04 Tools and Progress`. YSAP Bash and LFS101 were reaffirmed and their official pages rechecked. Grokking OOD is an optional, narrowly selected design reference for foundation Sections 3 and 5; see [ood-material-assessment.md](ood-material-assessment.md). No additional phase or study hours were added. The user reaffirmed that Obsidian project notes track current progress and next phases; preserve their tasks and metadata.

The user explicitly designated this repository as the teacher's classroom/office. Start at [README.md](README.md); teaching preparation and original handouts live in `teaching/`. The student reading room is Obsidian `Notes/Coding Agent Course/`, with Start Here, a material shelf, the study route and the first tool-cycle handout. The user chose links to the six existing Self-learn repositories; `materials/` contains those links. Their local revisions and the s01 lines 87–117 anchor were checked again.

This organizes the settled September 10 curriculum. The existing roadmap remains the course design; existing Obsidian project notes retain tasks, status and evidence. Preserve student annotations when revising published handouts. See [teaching/DECISIONS.md](teaching/DECISIONS.md) for the recovered agreement and later evidence-dependent decisions, and [CONTEXT.md](CONTEXT.md) for course vocabulary. No learning completion is inferred from the organization.

### Current course redesign — 2026-09-10

The user wants to redesign the course from outcomes and the purpose of each resource. They explicitly report that the generated `agent-learning` chapters are poorly designed, unclear, and did not help them learn. Do not use those chapters or the existing mini-agent as the syllabus or assume their correctness. Keep Tau and Pi source as valuable references.

Confirmed baseline: the user can write small Python scripts, but async, subprocesses and larger codebases are unfamiliar. No lesson completion has been demonstrated. Teach small mechanisms before introducing full async agent implementations. Use a few Python exercises for orientation, then TypeScript for the main build.

Read [ROADMAP.md](ROADMAP.md) for the redesigned sequence: one tool cycle → JS/Node process runner → small typed agent → selected Tau/Pi investigation and Pi extension → one real worker → bounded coordination and Linux recovery. Only Step 1 is active. The opening block traces a scripted file-read request, modifies a tiny tool dispatcher, then locates that mechanism in actual source. Expand lessons interactively; do not generate the entire course or implement the learner's exercises upfront.

The five goals remain: a useful terminal workflow; agent construction through Tau/Pi/Claude Code; Obsidian progress tracking; Boot.dev JS/TS; Bash/Linux. Initial workflow hypothesis: cmux or Ghostty → Herdr → Pi with DeepSeek V4.1 Flash → Claude Code/Codex workers. Actual daily harness use can begin alongside learning. DeepSeek fit and delegation remain unverified. Herdr terminal persistence is distinct from conversation/task recovery. Pi source exists; its executable was not on the inspected PATH earlier September 10.

Resource roles: Boot.dev teaches languages; YDKJS supplies selected depth; Node docs/labs bridge languages to processes; YSAP teaches Bash; LFS101 supplies Linux foundations with focused operational labs. System Design Primer supplies tradeoffs, System Design 101 visual reinforcement, and the SDE interview roadmap optional references. Effect is a later comparison after an understood plain-TS adapter. The third-party learn-claude-code repo is not Anthropic's internal source; select chapters by mechanism rather than requiring all seventeen current chapters.

The user confirmed **10 focused hours/week** and now wants all three workflow projects in the course. They explicitly chose **a working team using existing tools first**, not a new coordination framework. Current compact target: **160 hours / 16 weeks**, September 14, 2026–January 3, 2027, with limited slack. The user reports being a fast learner and explicitly requested shorter dates for every course project. Review actual pace September 30 after the two-week JS/Node sprint. This supersedes the earlier 360-hour forecast without marking work complete or increasing weekly hours.

### Three-workflow Obsidian course — 2026-09-10

Navigation: `/Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/coding-agent-course.md`. It is outside Taskflow's Active folder so it does not consume a project slot or duplicate task checklists. The three original workflow identities remain terminal-human-in-the-loop, gui-human-in-the-loop, and multi-agent-human-review.

Ordered execution projects under Projects/Active:

1. terminal-agent-01-agent-loop: 2026-09-14–2026-09-16, 4h.
2. terminal-agent-02-javascript-node: 2026-09-17–2026-09-30, 20h.
3. terminal-agent-03-typescript-agent: 2026-10-01–2026-10-18, 26h.
4. terminal-agent-04-pi-extension: 2026-10-19–2026-11-01, 20h.
5. gui-human-in-the-loop: 2026-11-02–2026-11-08, 10h.
6. terminal-agent-05-worker-adapter: 2026-11-09–2026-11-22, 20h.
7. terminal-agent-06-linux-coordination: 2026-11-23–2026-12-13, 30h.
8. multi-agent-human-review: 2026-12-14–2027-01-03, 30h.
The terminal workflow note owns shared early practice, optional setup, and completed historical records; its target is December 13, 2026. Only the first learning section is active. Preserve exact `## Tasks:` punctuation, original Chinese wording and all completion dates. The existing 53 tasks across nine Active notes were retained exactly once; new GUI/team checkpoints were added. Backup and task audit: archive/2026-09-10-three-workflows/.

Taskflow 0.5.6 installed/running was checked. Its reader consumes `start`, `deadline`, `status` and `order`; old course `start_date` keys were migrated to `start`. Future starts affect hybrid pacing, while `now` overrides them. No parent/dependency engine was found; use explicit prerequisite links and evidence gates. Global settings/templates were not changed. Dates are forecasts, never actual completion.

GUI: compare Paseo/T3, trace one client/server/provider path after JS/TS and Pi architecture. T3's React/Effect require only a narrow reading bridge; optional early 1–2h preview replaces practice and counts inside its 10h budget. Full React training and Effect adoption remain outside the main build.

Team: existing tools first, reuse the bounded two-worker/Linux work. Start with two writers, one coordination/integration owner and a separate review pass; compare two trials and justify any scaling. OMP/Orca remain candidates. The Orca orchestration page could not be fetched in this update; recheck interfaces when beginning the lab. No tool deployment, live integration or learning completion resulted from planning.

The separate setup-matt-pocock-skills draft remains pending its own final review; default triage labels were confirmed. Do not duplicate Obsidian progress in an additional repo issue backlog.

Fast pacing: attempt checkpoints first, shorten familiar explanations, reuse one implementation and limit source tours. Retain Boot.dev completion tasks and actual evidence gates. All 62 task lines/states were preserved when updating the ten notes. Prior schedule snapshot: archive/2026-09-10-before-compact-schedule/.

### Immediate study workflow — 2026-09-10

The user asked what to do now and how to follow Obsidian tasks. Teach through short guided sessions plus narrow source readings, not bulk generated chapters. Today's 30–45-minute assignment: explain model request vs harness execution, read only current learn-claude-code s01 `agent_loop()` (lines 87–117), trace the message/result flow, and answer who executes, what changes, and what stops this example. No API call/install is needed. Review the learner's answers before the tiny Python dispatcher exercise. A separate Boot.dev JS session starts at Variables. Obsidian now has an explicit task queue and ordered task groups; parent tasks span stages and are not meant to be completed wholesale in sequence. No learning completion is recorded.

### Node.js material added — 2026-09-10

The user explicitly requested Node.js material. Required sources are official Node.js Learn (short explanations) and API docs (implementation details); the resource catalog contains selected readings and project checkpoints. Step 2 covers CLI/environment, files, async I/O and a fake-worker subprocess runner; streaming/cancellation are revisited for Step 5's real adapter and Step 6's Linux process-tree cleanup. Begin after the relevant JS prerequisites, not after completing all TS. The active Step 1, provisional schedule and existing runtime/package-manager setup remain unchanged. No Node exercise has been completed by this addition.

### Material and Herdr refresh — 2026-09-10

All six local material repositories now match their fetched upstream default branches; full before/after evidence is in [material-versions.md](material-versions.md). Tau source package 0.4.2, Pi coding-agent source package 0.85.1. learn-claude-code now has 17 current chapters, not the previously inspected 20. Recheck source details and chapter numbering before lessons; dependencies/executables were not installed by these Git updates.

Herdr client was already 0.9.0. The named terminal-practice server was 0.8.0; user explicitly approved stopping its processes and restarting it. It now runs 0.9.0 with compatible protocol 22 and no restart required. State/config backup: /tmp/herdr-terminal-practice-before-0.9.0. Started headlessly; attach with `herdr --session terminal-practice`. Earlier 0.8.0 shell markers/PIDs below are historical and no longer live. Other sessions/remote hosts were not restarted. UI/layout restoration remains unverified.

### Previous scope — retained for context

Develop two personal coding-agent workflows:
1. Human-in-the-loop, single active harness per task: Ghostty or cmux, Herdr, Claude Code/Codex/Pi, optional Paseo GUI/mobile.
2. Later: larger delegated work with human review, evaluating OMP and Orca.

The user wants concrete app boundaries, use cases, and hands-on instruction, not vague recommendations. Current priority is workflow 1, specifically learning and configuring Ghostty and cmux before proceeding to Herdr and harness integration.

## Agreed working model

- Ghostty and cmux are alternative terminal interfaces. cmux additionally supplies a project sidebar, browser, and notifications.
- Herdr manages persistent CLI terminals; the harness manages its conversation and tools.
- One writer and one session owner per task. Switching harnesses uses code plus explicit task notes.
- Paseo is an alternative GUI/mobile session owner; seamless takeover of Herdr sessions is unverified.
- OMP is a separate Pi-derived harness, so keeping it with Claude Code, Codex, and Pi means four harnesses. Defer that choice.

## Verified local setup

Historical initial versions (Herdr superseded by the refresh above): Ghostty 1.3.1, cmux 0.64.22, Herdr 0.8.0, Claude Code 2.1.237, Codex CLI 0.147.0. Pi was not found on the shell PATH. Recheck before version-dependent changes.

Shared terminal config: `/Users/seanmacbook/Library/Application Support/com.mitchellh.ghostty/config`.
cmux config: `/Users/seanmacbook/.config/cmux/cmux.json`.
Herdr config: `/Users/seanmacbook/.config/herdr/config.toml` (not changed).

Changes already made:
- Ghostty: font-size 15, opaque background, padding 8, window-save-state always, inherited working directories, close confirmation.
- cmux: stable sidebar order, inherited working directories, quit confirmation, native terminal input, supported-agent auto-resume, routine hibernation off.
- Original Shift+Enter mapping and shell configuration preserved.
- Both edited configs have sibling backups ending `.20260909-194452.bak`.
- Ghostty config validation and cmux JSONC validation passed; cmux reloaded successfully.

## UI and verification boundaries

cmux has an existing research workspace that must be preserved. We added **Terminal Practice** with **Agent** and **Checks** panes. Neither contains a running coding agent. Pane navigation, zoom/restore, and reading hello.txt were visually verified. Directory references must use the new Projects path after the move.

cmux socket mode permits processes started inside cmux. External socket access was denied; no access settings were weakened. For UI operations use approved computer-use tools. Computer control explicitly denied access to Ghostty and Codex apps. Do not work around those denials with another UI automation mechanism.

No global agent hooks installed; no full quit/relaunch recovery test; no agent multiline/image input test; no macOS banner-delivery test. Ghostty UI appearance remains a manual user check.

## Continuation verification (2026-09-09)

- Saved Codex project registration is now verified by `list_projects`: `agent-workflow-research`, path `/Users/seanmacbook/Projects/agent-workflow-research`, project ID `ee9512c7-c4be-46d3-bc59-7afd0afc4489`. This task read both continuity files. CHAT-HISTORY.md remains an archive, not native imported history.
- Verified cmux Checks directory and a new tab's inherited directory use the Projects path; closed only the new idle test tab.
- Created a separate cmux **Herdr Practice** workspace with one outer terminal running `herdr --session terminal-practice`. The existing research and Terminal Practice workspaces remain present.
- Herdr 0.8.0 has two inner shells. Verified split right, H/L navigation to left, zoom/restore, right-pane directory inheritance, detach, and reattach. The left shell printed PID 85637 and in-memory marker `still-here` before and after detachment. Session is left attached for hands-on practice.
- No harness launched, hooks installed, or global config modified in this continuation. Ghostty UI and full app/server restart remain untested.
- Hands-on continuation: `terminal-practice/HERDR.md`.

## Next work (supersedes the original list below)

1. User practices the inner/outer controls in HERDR.md; manual Ghostty visual check and named-session attachment remain outstanding.
2. Configure one chosen harness and test input, interruption, notifications, and native conversation resume.
3. Test full recovery separately when existing work can be safely interrupted.

## Original next-work list (historical)

1. Register this folder as a saved Codex project in the app. Tooling could list projects but did not expose project creation or reassignment of the current task, and Codex UI control was denied. This app step is not yet complete.
2. Keep the original task history if the app supports moving this task to the saved project. Otherwise create a task there and explicitly read PROJECT-CONTEXT.md and CHAT-HISTORY.md; do not claim the archive is native imported history.
3. Finish the terminal exercises in terminal-practice/START-HERE.md.
4. Add Herdr deliberately and teach inner versus outer pane controls.
5. Configure one harness and test its actual input, notifications, and resume before adding more integrations.

No global Codex memory files were modified. This is project-local continuity context requested by the user.
