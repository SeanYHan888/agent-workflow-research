# Lesson 3: persistent terminals with Herdr

Original exercises verified on 2026-09-09 with Herdr 0.8.0 inside cmux.

**Update, 2026-09-10:** client and named `terminal-practice` server are now 0.9.0. The user approved stopping the old pane processes for the restart. The server is running headlessly; attach with `herdr --session terminal-practice`. Layout/UI and these key exercises need a fresh check; the old shell PID and in-memory marker are no longer live. See [version evidence](../material-versions.md).

## Previously verified setup

Select **Herdr Practice** in cmux. This workspace contains one outer terminal running `herdr --session terminal-practice`. Herdr contains two inner shell panes, both in this directory. The left pane is for the future agent; the right is for checks. No coding agent has been launched.

The separate **Terminal Practice** workspace retains its original two cmux panes. The research workspace was preserved.

## Which keys control which layer?

| Action | Outer app: cmux or Ghostty | Inner runtime: Herdr |
|---|---|---|
| Split right | Cmd+D | Ctrl+B, release, then V |
| Move left/right | Cmd+Option+Left/Right | Ctrl+B, release, then H/L |
| Zoom/restore | Cmd+Shift+Enter | Ctrl+B, release, then Z |
| New tab | Cmd+T | Ctrl+B, release, then C |
| Detach, keeping shells alive | — | Ctrl+B, release, then Q |
| Show Herdr bindings | — | Ctrl+B, release, then ? |

The action letters are lowercase unless Shift is explicitly listed. Ctrl+B is a prefix: release it before pressing the next key. For this workspace use Herdr's inner controls. Cmd+D creates an additional outer cmux pane.

## Repeat the persistence test

1. In the left Herdr pane, run:

   ```sh
   printf 'pid=%s marker=%s\n' "$$" "$WORKFLOW_PROBE"
   ```

2. Press Ctrl+B, release, then Q. You return to the outer shell.
3. Run:

   ```sh
   herdr --session terminal-practice
   ```

4. Repeat the print command. Both values should match. The marker exists in the running shell, not a saved file.

Our test returned `pid=85637 marker=still-here` before and after detachment. This proves live shell continuity for that test; it does not prove restart, reboot, or agent-conversation recovery. A later restarted shell will have a different PID and no marker.

## Use the same session from Ghostty

Detach from cmux first with Ctrl+B then Q. Open Ghostty manually and run:

```sh
cd /Users/seanmacbook/Projects/agent-workflow-research/terminal-practice
herdr --session terminal-practice
```

This is the documented named-session attach route; Ghostty UI attachment has not been tested here because earlier computer-control access was denied. Detach there before returning to cmux. Always include the session name: plain `herdr` opens the default session.

Detaching keeps processes alive while the host is running. It does not make the Mac execute while asleep or powered off. Do not use `exit` or close an inner pane when you intend to preserve its shell.

## Next checkpoint

Practice navigation and detachment yourself. Then select one harness for the left pane and verify multiline input, interruption, notifications, and conversation resume. Keep the right pane for checks. No global hooks or Herdr configuration changes were needed for this lesson.

References: [Herdr quick start](https://herdr.dev/docs/quick-start/), [named sessions and persistence](https://herdr.dev/docs/persistence-remote/). Keybindings were also checked against installed `herdr --default-config` and the local config, which has no key overrides.
