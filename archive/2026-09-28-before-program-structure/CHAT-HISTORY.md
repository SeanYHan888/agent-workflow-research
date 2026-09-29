# Conversation history

Snapshot of the user and assistant messages from Codex task `01a0886a-08d4-7c70-9f4d-a62bc3494115`, captured during the project move on 2026-09-09. Includes progress messages. Excludes system/developer instructions, tool payloads, and internal reasoning. Original historical paths are retained; the current project path is `/Users/seanmacbook/Projects/agent-workflow-research`. This is a readable archive, not an import into Codex native history.


## 1. User

i want to start building a terimal agent cli workflow with herdr and claude code, codex, pi, etc. im thinking cmux or ghosty as terminal client. here are some resources you might find useful: [https://x.com/alin\_zone/status/2033524177295274496](https://x.com/alin_zone/status/2033524177295274496). this wokrflow is mostly for signal thread, single model harness. i would use 3 different harness: claude code, codex, and pi, at most. and maybe [https://paseo.sh/](https://paseo.sh/) for gui case.my human in the loop workflow.&#x20;

and i have another multi agent setup in mind using omp.sh and onorca.dev. this is mostly for large but human as reviewer only workflow

i dont know how the two workflow would be so lets dive deep into it and see what could be the best practice for me



## 2. Assistant

I’ll investigate the tools and how they fit your two modes: hands-on work in a single agent session, and larger delegated work where you mainly review results. I’ll also check where terminal management, agent harnesses, and orchestration overlap so the setup stays manageable.


## 3. Assistant

I’m using the research skill and official OpenAI documentation for this comparison. One early distinction matters: Herdr manages persistent terminal sessions, while a harness manages the agent’s conversation and tools. Keeping those responsibilities separate will make it easier to switch between Claude Code, Codex, and Pi.


## 4. Assistant

Paseo currently lists all three of your preferred harnesses, plus OMP. That makes it a possible shared GUI for both workflows. I’m checking the session handoff details, though: supporting the same harness doesn’t necessarily mean Paseo can attach to the exact terminal session Herdr is already running.


## 5. Assistant

The OMP–Orca combination is supported, but OMP is a separate Pi-derived harness, so it would add a fourth harness if you keep Pi. Orca’s structured orchestration is also marked experimental and still needs a coordinator to dispatch and supervise work.

I found one consequential default for your reviewer-only mode: Orca pre-fills permission-bypass launch flags. A disposable Git worktree protects the separation of code changes; it doesn’t contain what shell commands can access. I’ll account for that in the proposed setup.


## 6. Assistant

My recommendation is taking shape: use Ghostty + Herdr for the terminal-first workflow if Herdr is central to what you want. Trial Orca with Claude Code or Codex before introducing OMP, so you can judge orchestration separately from a new harness.

I’ve saved the detailed design and a separate OMP–Orca comparison, including a small trial plan for measuring review effort and recovery behavior.


## 7. Assistant

**I would build two working modes that share the same task records and review standards.** Start with the interactive mode, then add delegation once you know what a good completed task looks like.

My initial recommendation:

- **Hands-on:** Ghostty + Herdr + one selected harness per task.
- **GUI/mobile:** Paseo-managed sessions when you want that interface.
- **Delegated work:** Orca + your existing Claude Code/Codex first; evaluate OMP afterward.

I’m interpreting “signal thread” as **single thread**, and “ghosty” as **Ghostty**.

The tools occupy different layers:

| Layer | Tools | Responsibility |
|---|---|---|
| Terminal interface | Ghostty, cmux | Display terminals, navigation, keyboard interaction |
| Persistent terminal runtime | Herdr | Keep agent terminals running and reconnect to them |
| Agent harness | Claude Code, Codex, Pi, OMP | Conversation, model calls, tools, agent behavior |
| Workspace and supervision | Paseo, Orca | Launch/manage sessions, worktrees, review and coordination |

Herdr’s server owns running terminals; cmux adds desktop workspaces, notifications, and a browser. These capabilities overlap in navigation, but their responsibilities differ. [Herdr persistence](https://herdr.dev/docs/persistence-remote/), [cmux](https://cmux.com/)

**For your first workflow, choose the terminal around how you want to interact.**

| Starting setup | Best fit | Main tradeoff |
|---|---|---|
| **Ghostty + Herdr** | Herdr is central; you want a consistent terminal workflow locally and over SSH | Learn Herdr’s navigation |
| **cmux + native harnesses** | You value a Mac sidebar, notifications, and browser beside the agent | Process recovery depends on the relevant integration |
| **cmux + Herdr** | You specifically need cmux’s desktop features and Herdr’s persistent terminals | Two overlapping navigation layers |

Given your stated interest in Herdr, **I’d start with Ghostty + Herdr**. If you choose cmux, initially let cmux own project/browser organization and Herdr own agent terminals. Avoid mirroring every pane and notification between them.

One meaningful distinction: cmux documents restoring layouts and resuming supported agent conversations, but **does not checkpoint arbitrary live processes**. Herdr can keep processes alive across client detachment. Neither makes a sleeping or powered-off execution machine keep computing. [cmux session restore](https://cmux.com/docs/session-restore)

Your interactive loop could be:

```text
You clarify the task
        ↓
One harness implements a small coherent change
        ↓
You inspect behavior and the diff
        ↓
Continue, correct, or accept
```

Keep Claude Code, Codex, and Pi available, but choose **one default** based on your own tasks. I would avoid assigning permanent “planner” and “coder” roles before comparing actual results.

Also distinguish **model choice from harness choice**: using an OpenAI model through Pi still gives you Pi’s tools, session handling, and extensions. Pi deliberately leaves several workflow features to extensions rather than building them into its core. [Pi documentation](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)

For switching harnesses, transfer **code and a short handoff record**: decisions, checks performed, unresolved problems, and the next action. Don’t depend on conversations being interchangeable.

**Paseo is promising, but choose session ownership deliberately.**

It supports Claude Code, Codex, Pi, and OMP. However, its structured interfaces use provider integrations—for example, Codex app-server and the Claude Agent SDK. That does not establish automatic attachment to an arbitrary native TUI already running inside Herdr. [Supported providers](https://paseo.sh/agents), [Codex integration](https://paseo.sh/docs/codex), [Claude integration](https://paseo.sh/docs/claude-code)

My starting rule would be:

- A terminal-first task starts under Herdr.
- A task needing desktop/mobile continuity starts under Paseo.
- Changing owners requires a tested handoff or an explicit artifact transfer.

Paseo also supports delegation and worktrees, so it may eventually cover both modes well enough for you. Orca should earn its place through a better review experience or coordination workflow. [Paseo orchestration](https://paseo.sh/docs/orchestration)

**For your second workflow, the critical design is ownership and acceptance.**

Use this proposed structure:

```text
You approve a bounded brief
             ↓
       One coordinator
        ↙           ↘
 Worker A         Worker B
 Worktree A       Worktree B
        ↘           ↙
   Integration and verification
             ↓
     Fresh agent review
             ↓
 You review evidence and approve
```

The coordinator handles routine questions, retries, and integration. You receive a reviewable result containing:

- The candidate diff and revision.
- Acceptance checks with actual results.
- Remaining concerns and unresolved findings.
- A concise demonstration of the resulting behavior.

Start with **two writers**, scoped to separable work. Parallelism helps when ownership and interfaces are clear. Tightly coupled changes may be easier to complete sequentially even when the overall project is large.

**OMP + Orca is supported, but OMP is another harness.** Keeping Claude Code, Codex, Pi, and OMP means maintaining four. If your three-harness limit applies globally, OMP would replace Pi rather than simply extend it. [OMP repository](https://github.com/can1357/oh-my-pi), [Orca agent support](https://www.onorca.dev/docs/agents/supported)

If you adopt both, give them distinct scopes: Orca manages feature worktrees; OMP manages bounded subtasks inside an assigned feature. Avoid having both independently schedule, retry, and integrate the same work.

Orca’s structured orchestration is currently labeled **experimental** and still requires a coordinator. Also, its documented defaults include permission-bypass launch arguments. For unattended execution, establish an appropriate runtime boundary: a Git worktree separates code changes but does not sandbox shell access. [Orca orchestration](https://www.onorca.dev/docs/cli/orchestration), [Launch defaults](https://www.onorca.dev/docs/agents/supported)

**I would adopt this in four steps:**

1. Complete three real tasks with Ghostty + Herdr and one familiar harness.
2. Try one Paseo task, including desktop/mobile continuity.
3. Run a small delegated feature in Orca using the familiar harness.
4. Compare a similar task using OMP, measuring human intervention, review time, repair turns, and accepted correctness.

This separates the value of each tool from the novelty of changing everything simultaneously.

I saved the [detailed workflow design](/Users/seanmacbook/Documents/agent-workflow-research/workflow-design.md) and [OMP–Orca investigation](/Users/seanmacbook/Documents/agent-workflow-research/omp-orca.md). This was documentation research; no tools were installed or integrations tested. The original X post did not return readable content, so I used official Ghostty documentation for the terminal comparison.


## 8. User

good lets work on first workflow first, give me some recommandtions of how to set it up



## 9. Assistant

I’ll focus on a minimal Ghostty + Herdr setup for hands-on work. I’ll check what’s already installed and recommend clear defaults for panes, sessions, and switching harnesses.


## 10. Assistant

**You already have most of the foundation installed.** I verified Ghostty 1.3.1, Herdr 0.8.0, Claude Code, and Codex CLI. Pi wasn’t found on the current shell’s `PATH`. I haven’t changed anything.

I recommend starting with **Ghostty → Herdr → one Claude Code or Codex session**, with the following setup.

**1. Give each layer one job.**

- **Ghostty:** font, colors, clipboard, and the terminal window.
- **Herdr:** projects, tabs, panes, and persistent agent terminals.
- **Harness:** conversation, tools, and implementation.
- **You:** direction, feedback, and acceptance.

Use one main Ghostty window initially. Create your working splits inside Herdr so there’s only one pane-navigation system to learn.

**2. Organize by project and task—not by model.**

My suggested layout:

```text
Herdr
└── Project workspace
    ├── Task: authentication
    │   ├── Agent                 ~70% width
    │   └── Shell / tests / diff  ~30% width
    └── Server / logs            optional tab
```

The task remains “authentication” whether you use Claude Code or Codex. This makes returning to work easier than navigating a collection of model names.

Herdr recommends project-level workspaces and supports tabs and splits inside them. [Herdr quick start](https://herdr.dev/docs/quick-start/)

**3. Keep the initial launch process explicit.**

From Ghostty:

```sh
cd /path/to/project
herdr
```

Inside the intended Herdr pane, confirm the directory and start **one** harness:

```sh
pwd
git status --short
claude
```

Or use `codex` instead.

For now, launch Herdr manually. Once the workflow feels right, add a small project launcher. That avoids committing early to shell startup behavior or complicated automation.

Learn just these Herdr shortcuts first:

| Action | Keys |
|---|---|
| Split right | `Ctrl+B`, then `V` |
| Split below | `Ctrl+B`, then `-` |
| New tab | `Ctrl+B`, then `C` |
| Workspace navigation | `Ctrl+B`, then `W` |
| Detach | `Ctrl+B`, then `Q` |
| Show active bindings | `Ctrl+B`, then `?` |

Run `herdr` again to reconnect. Detaching leaves its agents running while the execution machine remains available. [Herdr controls](https://herdr.dev/docs/quick-start/)

**4. Configure Ghostty for reading and reliable input.**

My suggested starting preferences:

- Font size around **14–16**, adjusted to your screen.
- Opaque background for long code and diff reviews.
- A clearly visible cursor and restrained theme.
- Keep close confirmation enabled.
- Test multiline input and image paste in each harness.

Your Ghostty configuration already contains a **Shift+Enter mapping**. I would test that before adding or replacing shortcuts.

Use your existing [Ghostty configuration](</Users/seanmacbook/Library/Application Support/com.mitchellh.ghostty/config>) as the single configuration source. Ghostty documents the available appearance and input settings in its [configuration reference](https://ghostty.org/docs/config/reference).

**5. Establish a small task contract.**

At the start of a meaningful task, give the agent something like:

```text
Goal:
What should work when this task is complete?

Acceptance:
Concrete examples or checks that demonstrate success.

Constraints:
Existing behavior to preserve; relevant files and conventions.

Working mode:
One agent session. Implement a small coherent change, verify it,
then show me the result. Ask when a product decision is ambiguous.
```

For work spanning multiple sessions, maintain one short task note with decisions, checks performed, unresolved issues, and the next action. That becomes your handoff when switching harnesses.

Use your normal checkout for one active task. Introduce a separate worktree when another task needs to edit the same repository concurrently.

**6. Add integrations only after the basic loop passes.**

Before adding Pi, Paseo handoffs, or plugins, verify:

- Detach and reconnect to the same running terminal.
- Interrupt the agent and provide a correction.
- Exit and resume the harness conversation.
- Paste multiline text and an image where supported.
- Run tests and inspect the diff from the companion shell.

Then add Herdr’s harness integrations where they improve session identification and restoration. [Herdr integrations](https://herdr.dev/docs/integrations/)

**My recommended first milestone is one real task completed comfortably with this two-pane layout.** Keep Claude Code and Codex available, choose whichever you already prefer for that task, and add Pi once you can identify a specific customization you want from it.


## 11. User

this is a bit too vague, give me a clear map of what is the boundary for each app, and what is the usecase for each app, and when should i use them i what setting.



## 12. Assistant

**For your first workflow, you have three choices to make: where you interact, who keeps the session running, and which harness does the work.** You do not need every app in the path.

Here is the concrete map:

```text
TERMINAL MODE                         GUI MODE

You                                  You
 ↓                                    ↓
Ghostty OR cmux                       Paseo
 ↓                                    ↓
Herdr                                Paseo-managed agent session
 ↓                                    ↓
Claude Code OR Codex OR Pi            Claude Code OR Codex OR Pi
 ↓                                    ↓
Project files + shell commands       Project files + shell commands
```

In terminal mode, **Herdr owns the running terminal**. In GUI mode, **Paseo manages the agent session**. Treat these as two entry points into your work, with one owner per active session.

**The boundary of each app**

| App | Its responsibility | What you use it for | Where its responsibility ends |
|---|---|---|---|
| **Ghostty** | Terminal display and input | Typing, rendering agent output, fonts, clipboard, keyboard shortcuts | Does not own the agent’s reasoning, task plan, or conversation history |
| **cmux** | Terminal display plus a desktop workspace | Project sidebar, terminal/browser splits, notifications, browser interaction | Does not replace the underlying agent harness; restoring a session is not preserving arbitrary process memory |
| **Herdr** | Persistent terminal processes and agent navigation | Keeping a CLI running after you detach, reconnecting, switching agent panes, seeing attention states | Does not decide whether the implementation is correct or provide a common conversation across harnesses |
| **Claude Code** | Agent execution and conversation | Discussing a task, inspecting files, editing, running commands, checking results | Does not manage the overall Ghostty/Herdr environment unless you explicitly ask it to |
| **Codex CLI** | Agent execution and conversation | The same category of work, using Codex’s tools, controls, and session behavior | Does not automatically inherit a Claude Code or Pi conversation |
| **Pi** | Extensible agent execution and conversation | Working through a customizable harness with your chosen models and extensions | Custom workflow features may require extensions or configuration |
| **Paseo** | GUI/mobile access and management of agent sessions | Chatting with an agent, reviewing changes, returning from another client | Do not assume it automatically takes over a native terminal session already running under Herdr |

These boundaries follow the documented [Herdr runtime](https://herdr.dev/docs/persistence-remote/), [cmux workspace and restore behavior](https://cmux.com/docs/session-restore), [Pi harness](https://github.com/earendil-works/pi/tree/main/packages/coding-agent), and [Paseo provider integrations](https://paseo.sh/agents).

**Ghostty versus cmux: choose the kind of desk you want.**

Both can be the terminal application at the top of your stack.

| Your setting | Use | Why |
|---|---|---|
| Primarily chatting with an agent, running tests, and reading terminal output | **Ghostty + Herdr** | Herdr provides the project/pane organization; Ghostty supplies the terminal |
| Building web interfaces and frequently checking the browser beside the agent | **cmux + Herdr** | cmux adds a browser and desktop workspace around persistent agent terminals |
| Mostly local work, happy with native agent resume, and prefer cmux’s navigation | **cmux + harness directly** | Herdr may add little for that particular session |
| Connecting to a remote machine and keeping work alive after disconnecting | **Ghostty or cmux → remote Herdr → harness** | The remote machine owns execution; your Mac displays it |

cmux’s browser and notification features are documented in its [product guide](https://cmux.com/). Herdr supports [remote attachment over SSH](https://herdr.dev/docs/persistence-remote/).

**My recommendation for you:** make **Ghostty + Herdr** the default. Use **cmux instead of Ghostty** when its browser workspace materially helps the task. You do not need to run Ghostty inside cmux.

If using cmux + Herdr, divide navigation like this:

```text
cmux owns:
  outer window
  browser pane
  desktop workspace

Herdr owns:
  agent terminal
  test terminal
  logs terminal
  detach / reconnect
```

**Claude Code versus Codex versus Pi: select the worker interface for the task.**

For your single-thread workflow, these are alternatives—not three roles that must run together.

| Situation | My recommended choice |
|---|---|
| Starting ordinary implementation or debugging | Your most familiar **Claude Code or Codex** |
| Wanting another assessment of a finished change | A fresh session in the other harness, with the exact diff and acceptance criteria |
| Wanting to design custom commands, extensions, or model-selection behavior | **Pi** |
| Continuing unfinished work | Resume the **same harness session** |
| Switching because the current approach is failing | Save a handoff, stop the current writer, then start the other harness |

I would not prescribe “Claude plans, Codex codes, Pi researches.” Those assignments would add switching without establishing that they help your work.

The important boundary is:

> **The harness owns the conversation. The repository owns the code. Your task note owns the portable decisions.**

Changing harnesses can preserve code and recorded decisions; it does not automatically preserve the same conversation.

**Paseo: use it when the interaction should be GUI-first or accessible from your phone.**

For example:

```text
At your desk:
Paseo desktop → Codex session

Later, away from your desk:
Paseo mobile → that Paseo-managed session
```

Paseo supports desktop/mobile access and runs the underlying providers on the execution machine. [Paseo](https://paseo.sh/)

That is different from:

```text
Ghostty → Herdr → Codex TUI
```

Both use Codex, but their session-management paths differ. I have not verified seamless live transfer between them.

**Decide at task creation:**

- “I want the native CLI experience” → **Herdr**.
- “I want to follow this through desktop/mobile GUI” → **Paseo**.

Paseo is therefore an alternative session entry point, rather than another mandatory layer beneath Herdr.

**What this looks like during actual work**

| What you are doing | Open this | What stays responsible |
|---|---|---|
| Implementing a backend feature at your Mac | Ghostty → Herdr → Codex or Claude | Herdr keeps terminals; harness does the task |
| Testing a web page while changing it | cmux → Herdr → harness, with browser alongside | cmux owns browser; Herdr owns CLI terminals |
| Leaving a terminal task and returning later | Detach Herdr, then reconnect | Same Herdr process and harness session, while host remains running |
| Working on a remote repository | Terminal → Herdr on remote host → harness | Remote host executes everything |
| Starting a task you want to check from your phone | Paseo → selected harness | Paseo manages access to that session |
| Experimenting with your own agent workflow | Ghostty → Herdr → Pi | Pi extensions define the custom behavior |
| Reviewing the result | Diff/browser/test output in your chosen interface | You judge acceptance; an “idle” indicator is not acceptance |

For now, I would assign **Ghostty as your daily terminal, Herdr as your CLI session manager, Claude Code/Codex as interchangeable task harnesses, Pi as your customization environment, and Paseo as your GUI/mobile route**. cmux becomes useful when you want its browser-centered desktop workspace.


## 13. User

good, teach me how to start using them, lets set up the terminal workflow with Ghostty and cmux first



## 14. Assistant

I’ll inspect the Ghostty and cmux settings, then set up a consistent terminal appearance and walk you through opening a workspace, splitting panes, and starting an agent.


## 15. User

good, teach me how to start using them, lets set up the terminal workflow with Ghostty and cmux first. also check if there are some extra configs i need to do


## 16. Assistant

I’ll check your Ghostty and cmux settings, then set up a consistent starting workflow and walk you through using it. I’ll preserve your existing preferences and focus on input, navigation, session recovery, and agent integrations.


## 17. Assistant

Both apps are installed, and their config files are mostly defaults. cmux reads the same Ghostty settings file, so one set of font and input settings can serve both.

I’ll add a small baseline and create a separate practice workspace. There’s an existing research terminal in cmux; I’ll leave that session intact.


## 18. Assistant

The config changes pass validation. They set 15-point text, comfortable padding, saved Ghostty layouts, and a stable cmux sidebar order. Your shell setup and existing Shift+Enter binding are unchanged.

I’m checking the practice workspace now. One useful detail surfaced: the new cmux split inherited the old project directory, so I’m correcting that and will include a `pwd` check in the walkthrough.


## 19. Assistant

cmux now has a separate **Terminal Practice** workspace with **Agent** and **Checks** panes, both in the practice directory. The original research workspace is still present.

Ghostty’s config validates, but the computer-control tool refuses access to the Ghostty app. I can verify its settings here; you’ll need to open Ghostty yourself for the visual check.


## 20. Assistant

**The terminal baseline is configured, and cmux is ready for a hands-on lesson.** Your existing research workspace is untouched.

I changed:

| Setting | Result |
|---|---|
| Shared Ghostty settings | 15-point text, opaque background, comfortable padding |
| Ghostty recovery | Save window/tab/split layout |
| Working directories | New terminals inherit the current directory |
| cmux sidebar | Projects stay in a stable order |
| cmux input | Native terminal input; routine agent hibernation off |
| Protection | Close/quit confirmation enabled |

Both config files were backed up and validated. cmux successfully reloaded them. Your shell and Shift+Enter mapping were preserved.

**Start in cmux now.**

Select **Terminal Practice** in its sidebar. I created:

```text
Terminal Practice workspace
┌───────────────────┬───────────────────┐
│ Agent             │ Checks            │
│                   │                   │
│ Conversation with │ Your commands,    │
│ the agent later   │ tests, and output │
└───────────────────┴───────────────────┘
```

Both panes are currently ordinary shells. No agent is running.

1. **Click Checks**, then run these individually:

   ```sh
   pwd
   ls
   cat hello.txt
   ```

   `pwd` should show `/Users/seanmacbook/Documents/agent-workflow-research/terminal-practice`.

2. **Move between panes:** press `⌘⌥←` and `⌘⌥→`.

3. **Enlarge one pane:** press `⌘⇧Enter`. Press it again to restore both panes. I verified this works.

4. **Create a terminal tab:** press `⌘T`. Run `pwd` to check its directory. Close that new idle tab with `⌘W`.

Use **workspaces for projects**, **panes for simultaneous views**, and **tabs for views you switch between**.

**Then try the same controls in Ghostty.**

Open Ghostty yourself, press `⌘⇧,` to reload, and run:

```sh
cd /Users/seanmacbook/Documents/agent-workflow-research/terminal-practice
```

Press `⌘D` to split right. In the new pane, run `pwd`, then `cat hello.txt`. Practice the same pane navigation and zoom controls.

| Action | Ghostty and cmux |
|---|---|
| Split right | `⌘D` |
| Split below | `⌘⇧D` |
| Move between panes | `⌘⌥Arrow` |
| Zoom/restore pane | `⌘⇧Enter` |
| Copy / paste | `⌘C` / `⌘V` |
| Interrupt a running command | `Ctrl+C` |
| Reload configuration | `⌘⇧,` |

**Two differences to remember:** `⌘N` creates a **window in Ghostty**, but a **workspace in cmux**. `⌘T` creates a **window tab in Ghostty**, but a **tab within the focused cmux pane**. [cmux shortcuts](https://cmux.com/docs/keyboard-shortcuts)

**Extra configuration you need now: none for basic terminal use.** The next configuration step is connecting your chosen harness and testing multiline input, notifications, and resume. I haven’t installed global agent hooks yet. Saved terminal layouts alone do not keep arbitrary commands running; Herdr will handle that part later.

The [saved walkthrough](/Users/seanmacbook/Documents/agent-workflow-research/terminal-practice/START-HERE.md) includes configuration paths, backups, and these exercises.

Ghostty’s configuration passed validation, but the computer-control tool denied access to its UI, so its visual check remains yours to complete.

<oai-mem-citation>
<citation_entries>
MEMORY.md:1805-1805|note=[Preserved existing shell setup and avoided unrelated keybinding changes]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>


## 21. User

this project looks cool but doesnt belong to docment folder, which i use to store personal info. move this project to project folder and create a new codex project with current session history and chat memory



## 22. Assistant

I’ll move the workflow project into `~/Projects`, then check how to attach this conversation to it while preserving its history.


## 23. Assistant

The files can be moved, and I’ll save the conversation and decisions inside the project for continuity.

Creating the saved Codex project is blocked from here: there’s no project-creation tool available, and computer control denied access to the Codex app. I’ll finish the move and context files, then give you the remaining app step.
