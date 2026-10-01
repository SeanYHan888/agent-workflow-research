# VPS operations home

**OVH setup resumed October 1, 2026.** Order 9004697 has validated payment and its VPS is active. SSH, Herdr and Tailscale connectivity are verified; Codex CLI and Claude Code are signed in and have each returned a live test response. See [current status](STATUS.md) for the verified configuration and remaining setup. Oracle provisioning remains discontinued and its capacity automation remains deleted.

Oracle/VPS continuity moved into this workspace September 28, 2026 at the student's request to retire the old folder. Use this directory for operational evidence; course tasks and learning progress remain in the existing Obsidian Linux project.

- [Current status and next action](STATUS.md): what was verified, what remains unknown, and monitoring ownership.
- [Provider comparison and recommendation](provider-options.md): prior options, budget and purchase conditions.
- [Course lab roadmap](../../course/projects/vps-lab-roadmap.md): learning stages and bounded projects.
- [Original Oracle status](../../archive/2026-09-28-oracle-project-source/STATUS.md) and [recommendation excerpts](../../archive/2026-09-28-oracle-project-source/vps-recommendation-excerpts.md): preserved dated sources.
- [Folder migration record](../../research/oracle-folder-retirement.md): preservation and app-dependency checks.

The prior Oracle method is historical reference only. Current authorization covers the purchased OVH host, SSH setup, Codex CLI and Claude Code for remote work; it does not mark course exercises complete.

## Daily connection

On the Mac, with Tailscale connected:

```bash
herdr --remote ovh-oregon --session work
```

In a VPS shell pane, enter the desired project directory and run `codex` or `claude`. Detach with Ctrl+B, then Q; the VPS owns the running processes. Reconnect with the same command. This preserves sessions through client disconnects, not arbitrary processes through a VPS reboot. Use `ssh ovh-oregon` for an ordinary SSH shell. Other devices need their own Tailscale connection and SSH access; the Mac alias is local configuration.
