# VPS operational status

**OVH remote CLI setup verified, October 1, 2026.** The student authorized an OVH Oregon VPS for remote Codex CLI and Claude Code work and completed payment in the browser. Oracle provisioning remains discontinued; its capacity automation remains deleted.

## Current OVH order

- Order **9004697**: authenticated order history shows **Payment validated** and **Order accepted**. The VPS dashboard subsequently showed **Active** (the earlier account homepage had still shown preparation).
- One VPS-1 2027: **US-WEST-OR (Hillsboro), 2 vCPU, 4 GB RAM, 40 GB local NVMe, Ubuntu 24.04**.
- Monthly, no long-term commitment: **$5.35 total at checkout**, including $0.00 tax; default PayPal and automatic renewal. Standard automatic backup is offered at no added cost on this order. No premium backup, snapshot or additional disk purchased.
- Host: `vps-1c9379da.vps.ovh.us`; IPv4 `51.81.222.110`; OS, Oregon location and resources verified on its dashboard. Standard backup is enabled; next payment date is November 1, 2026.
- A dedicated local Ed25519 key was generated at `/Users/seanmacbook/.ssh/ovh_oregon_ed25519`; its public-key fingerprint is `SHA256:/yOcc8piPStfsg2C9Fws1JZsGDTlSLXtNrXQlBWiAp0`. Its public key is installed; passwordless SSH and non-interactive sudo were verified on October 1. The student reports saving the new Ubuntu password in Apple Passwords; its contents were not accessed.
- Official native installers installed **Codex CLI 0.159.3**, **Claude Code 2.1.285 (stable)** and **Herdr 0.9.3** under `/home/ubuntu/.local/bin`; all version commands and login-shell PATH were verified. Git 2.43.0 was already present.
- **Herdr + Tailscale** is the selected workflow. The OS already included tmux 3.4; no tmux sessions were created. Herdr named session `work` survived a full SSH disconnect and reattach; the live shell retained a test variable (`REATTACH_OK=herdr-survived`). Reboot survival and agent-task recovery have not been tested.
- **Tailscale 1.102.4** installed from its official Ubuntu Noble repository; `tailscaled` is active. The student authorized device `ovh-oregon` into their tailnet. VPS private IPv4: `100.86.36.8`; SSH over it returned `TAILSCALE_SSH_OK` with the expected hostname. The Mac's existing Tailscale installation was reconnected, preserving its accept-routes setting.
- Local SSH alias `ovh-oregon` uses that private IP, dedicated key, strict host-key checking against the already trusted public-IP entry, no agent forwarding, and keepalives. Public SSH settings were not changed. The Mac Herdr 0.9.1 client successfully attached over this alias to VPS Herdr 0.9.3 using `herdr --remote ovh-oregon --session work`, displayed the preserved shell, and detached cleanly.
- Both CLI auth checks now report **logged in**: Codex through ChatGPT and Claude through Claude.ai. Minimal live prompts returned `CODEX_OK` and `CLAUDE_OK` from the VPS. These were connectivity tests without tool use or project work. Ubuntu bubblewrap 0.9.0 was installed after Codex reported the missing host prerequisite; the subsequent AppArmor sandbox fix and boundary checks are recorded below. No Mac credential caches were copied.
- Remote CLI provisioning is complete. No project repositories have been deployed by this setup; phone SSH access and reboot recovery remain untested.
- October 1 phone-access follow-up: `codex remote-control start --json` successfully bootstrapped a separate managed Codex 0.159.3 daemon (PID backend, auto-update enabled) and reported `status: connected`, host `vps-1c9379da`, remote control enabled. A short-lived manual pairing code was generated and shown only in chat. The student supplied iPhone screenshots showing the CLI host connected, followed by a phone-originated task reporting hostname `vps-1c9379da`, user `ubuntu`, and a workspace under `/home/ubuntu/Documents/Codex/2026-10-01/`. **Mobile pairing and remote command execution are verified by those user-provided results.** That first task required approved execution outside the sandbox; its startup failure was fixed as described below. Reboot autostart has not been configured or tested.

This is operational evidence, not completion of a course exercise or Linux milestone. No passwords, payment credentials or model tokens are stored here.

## Verified historical state

The [original record](../../archive/2026-09-28-oracle-project-source/STATUS.md) preserves the September 24 authenticated San Jose A1 2-OCPU/12-GB capacity result (`OUT_OF_HOST_CAPACITY`), capacity-report command, prior resize/storage observations and local preparation. It records no successful launch. Subsequent September 25/27 chat checks encountered network/sign-in blockers. Current capacity, free-tier allowances, billing and resource inventory remain unverified.

The established purpose is remote agent work using Tailscale/Herdr, with an approximately $5/month planning budget. No VPS-side installation was completed in the preserved record. [Provider choices](provider-options.md) are candidates, not an order.

## Monitoring and ownership

Automation `oracle-free-vps-capacity` was deleted successfully on September 28 after the student stopped this work. No future capacity checks are scheduled by it. Oracle provisioning is discontinued for this plan.

The old chat **Plan Oracle Cloud Free VPS setup** is archived and remains historical evidence; use this workspace for future work. The original folder has been moved to Trash. The [migration record](../../research/oracle-folder-retirement.md) records verification and the remaining stale sidebar entry.

## Access and next action

The preserved source references `/Users/seanmacbook/.ssh/oracle_vps_ed25519` and its `.pub` companion outside the retired folder. Key contents were not read, copied or changed. No credential belongs in this repository.

The replacement is the OVH host above. Continue only with that host; do not resume Oracle sign-in or capacity checks. The dedicated OVH key is installed and verified; the historical Oracle key was not changed or installed on OVH.

## Ubuntu 24.04 sandbox repair — October 1, 2026

- Reproduced `bwrap` user-namespace / loopback permission failures. Kernel audit logs showed the `unprivileged_userns` AppArmor profile and a denied UID-map write; the bubblewrap-specific profile was missing.
- Followed [official Codex prerequisites](https://learn.chatgpt.com/docs/sandboxing): installed `apparmor-profiles` and `apparmor-utils`, copied Ubuntu's `/usr/share/apparmor/extra-profiles/bwrap-userns-restrict` to `/etc/apparmor.d/bwrap-userns-restrict`, and loaded it with `apparmor_parser -r`. Package dependencies updated AppArmor/libapparmor to `4.0.1really4.0.1-0ubuntu0.24.04.8`.
- `kernel.apparmor_restrict_unprivileged_userns` remains **1**. No global AppArmor or Codex sandbox disablement was applied.
- Both the normal Codex binary and the separately managed remote-control binary successfully ran `hostname`, `whoami`, and `pwd` inside `codex sandbox` as `ubuntu`. A managed-binary probe attempting to create a file under `~/.cache/agent-setup` from a temporary workspace was blocked with `Read-only file system`; no probe file was created.
- The fix was loaded without reboot. The student subsequently reported that all three commands succeeded from the iPhone in the default sandbox, each with exit code 0: hostname `vps-1c9379da`, user `ubuntu`, cwd `/home/ubuntu/Documents/Codex/2026-10-01/hostname-whoami-pwd-2`. **The post-fix phone-to-VPS sandbox execution path is verified by that user-provided result.** Reboot autostart/recovery remains unconfigured and untested.

## Mac remote-control pairing — October 1, 2026

The student completed a separate Mac-to-VPS pairing. The Mac app tool inventory now lists remote host `remote-control:env_e_6abdf5d4d5188322adfce71ce8739b24` and both phone-created VPS chats, with no unavailable hosts. Reading the remote chat `重新运行 hostname whoami pwd` through the app succeeded and independently confirmed its three command outputs and exit codes of 0. Mac and iPhone can access the same VPS chat history; this does not migrate the current Mac-local course chat or copy local project files. Pairing codes were not saved to this repository.
