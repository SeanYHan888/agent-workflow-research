# Ghostty and cmux: first terminal lesson

Configured 2026-09-09. No agent was launched and no project source was edited.

## What was configured

Both applications read the existing Ghostty file at `/Users/seanmacbook/Library/Application Support/com.mitchellh.ghostty/config`. Added 15-point text, an opaque background, 8-point padding, saved Ghostty window layout, inherited working directories, and close confirmation. The existing Shift+Enter mapping and shell configuration were preserved.

cmux preferences are in `/Users/seanmacbook/.config/cmux/cmux.json`. Set stable sidebar order, directory inheritance, quit confirmation, native terminal input, supported-agent resume, and disabled routine agent hibernation. Existing unrelated settings were retained. The legacy settings file is a fallback; edit the canonical cmux.json going forward.

Backups are next to the two files, with suffix `.20260909-194452.bak`. Restoring those exact backups and reloading undoes this configuration change.

Validation: Ghostty's installed config validator passed; cmux's JSONC check passed; cmux reloaded successfully and displayed the practice panes. Full quit/relaunch recovery and agent input were not tested. Ghostty UI access was denied by the computer-control tool, so open it manually to verify appearance.

## Lesson 1: use cmux

Open cmux and select **Terminal Practice** in the sidebar. The two panes are **Agent** on the left and **Checks** on the right. Both are ordinary shells today; the names describe their intended purpose.

In Checks, run these one at a time:

```sh
pwd
ls
cat hello.txt
```

The working directory should be `/Users/seanmacbook/Projects/agent-workflow-research/terminal-practice`.

Press Cmd+Option+Left to focus Agent. Press Cmd+Option+Right to return to Checks. Press Cmd+Shift+Enter to enlarge the current pane, then again to restore the split.

Press Cmd+T to add a terminal tab inside the current pane. Run `pwd` to verify where it started. Close only that newly created, idle tab with Cmd+W. Do not close the existing research workspace.

Cmd+N creates a new sidebar workspace. Use a workspace for a project or independent task; use panes for simultaneous views inside it; use tabs for views you switch between.

For a real project, from a local terminal use `cmux /absolute/path/to/project` to create its workspace. Always verify `pwd` before starting an agent, especially after switching directories and immediately creating a split.

## Lesson 2: use Ghostty

Open Ghostty manually, reload settings with Cmd+Shift+Comma, and run:

```sh
cd /Users/seanmacbook/Projects/agent-workflow-research/terminal-practice
pwd
```

Press Cmd+D for a right split. Run `pwd` in that split, followed by `cat hello.txt`. Practice moving between panes with Cmd+Option+Left/Right and zooming with Cmd+Shift+Enter.

Ghostty's Cmd+N opens a window, while cmux's Cmd+N creates a sidebar workspace. Ghostty's Cmd+T opens a window tab, while cmux's creates a tab in the focused pane. Neither split automatically creates a separate Git checkout.

## Shared controls to learn first

| Task | Shortcut |
|---|---|
| Split right | Cmd+D |
| Split below | Cmd+Shift+D |
| Move between panes | Cmd+Option+Arrow |
| Zoom/restore focused pane | Cmd+Shift+Enter |
| Copy/paste | Cmd+C / Cmd+V |
| Interrupt a foreground command | Ctrl+C |
| Reload settings | Cmd+Shift+Comma |
| Open settings/config | Cmd+Comma |

Use the directional pane keys in both apps. Cmd+[ and Cmd+] have different navigation meanings between Ghostty and cmux.

## Extra configuration decisions

- No extra font, theme, shell framework, or plugins are required for this lesson.
- Keep the existing Shift+Enter mapping until we test it in the chosen harness. Terminal config parsing alone does not prove the agent receives the expected input.
- cmux's Claude integration is enabled by default. Codex has separate hook integration; hook setup can modify Codex configuration, so it belongs in the next harness setup step. No global hooks were installed here.
- Sidebar attention indicators and macOS notification banners are different. If you want banners, check System Settings > Notifications > cmux. Banner delivery was not verified here.
- Keep cmux's current socket access restriction. Commands from its own terminals work; an unrelated external process may be denied. No access settings were widened.
- Saved layout and native agent resume do not preserve arbitrary running processes. Add Herdr for persistent terminal execution in the next lesson.
- Once Herdr is inside a pane, use its controls for inner splits. Cmd+D still splits the outer terminal app.

## Continue with Herdr

The next lesson is [persistent terminals with Herdr](HERDR.md). A separate **Herdr Practice** cmux workspace is ready with two inner shells; detach/reconnect was verified on 2026-09-09. No agent is running.

## Primary references

- [Ghostty configuration](https://ghostty.org/docs/config)
- [cmux configuration](https://cmux.com/docs/configuration)
- [cmux shortcuts](https://cmux.com/docs/keyboard-shortcuts)
- [cmux agent hooks](https://raw.githubusercontent.com/manaflow-ai/cmux/main/docs/agent-hooks.md)

The one-time `configure-practice.sh` file was used to name the current cmux panes. Its surface references are temporary; do not reuse it as a general launcher.
