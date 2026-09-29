# Project context

This file preserves the working decisions from the Codex task **Design terminal agent workflows** (`01a0886a-08d4-7c70-9f4d-a62bc3494115`). Read this first when continuing in a new task. A readable conversation snapshot is in CHAT-HISTORY.md; it is not a native Codex history import.

## Location and user preference

Project root: `/Users/seanmacbook/Projects/agent-workflow-research`.
The user reserves Documents for personal information. Keep this project and its new artifacts in Projects. The directory was moved from Documents on 2026-09-09; five files were verified byte-for-byte before updating embedded paths.

## Objective

### Current course redesign — 2026-09-10

The user wants to redesign the course from outcomes and the purpose of each resource. They explicitly report that the generated `agent-learning` chapters are poorly designed, unclear, and did not help them learn. Do not use those chapters or the existing mini-agent as the syllabus or assume their correctness. Keep Tau and Pi source as valuable references.

Confirmed baseline: the user can write small Python scripts, but async, subprocesses and larger codebases are unfamiliar. No lesson completion has been demonstrated. Teach small mechanisms before introducing full async agent implementations. Use a few Python exercises for orientation, then TypeScript for the main build.

Read [ROADMAP.md](ROADMAP.md) for the redesigned sequence: one tool cycle → JS/Node process runner → small typed agent → selected Tau/Pi investigation and Pi extension → one real worker → bounded coordination and Linux recovery. Only Step 1 is active. The opening block traces a scripted file-read request, modifies a tiny tool dispatcher, then locates that mechanism in actual source. Expand lessons interactively; do not generate the entire course or implement the learner's exercises upfront.

The five goals remain: a useful terminal workflow; agent construction through Tau/Pi/Claude Code; Obsidian progress tracking; Boot.dev JS/TS; Bash/Linux. Initial workflow hypothesis: cmux or Ghostty → Herdr → Pi with DeepSeek V4.1 Flash → Claude Code/Codex workers. Actual daily harness use can begin alongside learning. DeepSeek fit and delegation remain unverified. Herdr terminal persistence is distinct from conversation/task recovery. Pi source exists; its executable was not on the inspected PATH earlier September 10.

Resource roles: Boot.dev teaches languages; YDKJS supplies selected depth; Node docs/labs bridge languages to processes; YSAP teaches Bash; LFS101 supplies Linux foundations with focused operational labs. System Design Primer supplies tradeoffs, System Design 101 visual reinforcement, and the SDE interview roadmap optional references. Effect is a later comparison after an understood plain-TS adapter. The third-party learn-claude-code repo is not Anthropic's internal source; select chapters by mechanism rather than requiring all seventeen current chapters.

The user confirmed **10 focused hours/week** and now wants all three workflow projects in the course. They explicitly chose **a working team using existing tools first**, not a new coordination framework. Current working plan: **360 hours / 36 weeks**, September 14, 2026–May 23, 2027; estimated range **300–440 hours / 30–44 weeks**, April 11–July 18. Review actual pace September 27. Earlier estimates in historical notes are superseded for the expanded course.

### Three-workflow Obsidian course — 2026-09-10

Navigation: `/Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/coding-agent-course.md`. It is outside Taskflow's Active folder so it does not consume a project slot or duplicate task checklists. The three original workflow identities remain terminal-human-in-the-loop, gui-human-in-the-loop, and multi-agent-human-review.

Ordered execution projects under Projects/Active:
1. terminal-agent-01-agent-loop: Sep 14–20, 10h, now.
2. terminal-agent-02-javascript-node: Sep 21–Nov 8, 70h, next.
3. terminal-agent-03-typescript-agent: Nov 9–Dec 27, 70h, later.
4. terminal-agent-04-pi-extension: Dec 28–Jan 17, 2027, 30h, later.
5. gui-human-in-the-loop: Jan 18–Feb 7, 30h, later.
6. terminal-agent-05-worker-adapter: Feb 8–Mar 7, 40h, later.
7. terminal-agent-06-linux-coordination: Mar 8–Apr 18, 60h, later.
8. multi-agent-human-review: Apr 19–May 23, 50h, later.

The terminal workflow note owns shared early practice, optional setup, and completed historical records; its target is April 18. Only the first learning section is active. Preserve exact `## Tasks:` punctuation, original Chinese wording and all completion dates. The existing 53 tasks across nine Active notes were retained exactly once; new GUI/team checkpoints were added. Backup and task audit: archive/2026-09-10-three-workflows/.

Taskflow 0.5.6 installed/running was checked. Its reader consumes `start`, `deadline`, `status` and `order`; old course `start_date` keys were migrated to `start`. Future starts affect hybrid pacing, while `now` overrides them. No parent/dependency engine was found; use explicit prerequisite links and evidence gates. Global settings/templates were not changed. Dates are forecasts, never actual completion.

GUI: compare Paseo/T3, trace one client/server/provider path after JS/TS and Pi architecture. T3's React/Effect require only a narrow reading bridge; optional early 1–2h preview replaces practice and counts inside its 30h budget. Full React training and Effect adoption remain outside the main build.

Team: existing tools first, reuse the bounded two-worker/Linux work. Start with two writers, one coordination/integration owner and a separate review pass; compare two trials and justify any scaling. OMP/Orca remain candidates. The Orca orchestration page could not be fetched in this update; recheck interfaces when beginning the lab. No tool deployment, live integration or learning completion resulted from planning.

The separate setup-matt-pocock-skills draft remains pending its own final review; default triage labels were confirmed. Do not duplicate Obsidian progress in an additional repo issue backlog.

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
