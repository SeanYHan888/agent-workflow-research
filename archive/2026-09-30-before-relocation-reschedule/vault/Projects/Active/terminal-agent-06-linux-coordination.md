---
type: project
status: later
area: tools
start: 2026-11-23
deadline: 2026-12-13
outcome: Operate the workflow with both worker harnesses, bounded parallelism, explicit task state and recoverable Linux execution.
created: 2026-09-10
tags:
  - project-file
related:
  - "[[terminal-human-in-the-loop]]"
order: 14
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 7
---
# 06 — Coordination and Linux recovery

**Planned start:** 2026-11-23 · **Target finish / deadline:** 2026-12-13

[[Notes/Coding Agent Course/00 Start Here|Course overview]] · [[terminal-human-in-the-loop|Terminal workflow]] · [[terminal-agent-05-worker-adapter|Previous section]] · [[multi-agent-human-review|Next — team capstone]]

Dates are study targets, not actual start/completion records. Planned allocation: **30 hours** within the shared **10 hours/week** course budget. This compact target has limited slack; reforecast if the preceding checkpoint takes longer.

## Project goal:

Operate the workflow with both worker harnesses, bounded parallelism, explicit task state and recoverable Linux execution.

## Required scope update — September 30, 2026

The approved [systems module](</Users/seanmacbook/Projects/agent-workflow-research/course/modules/systems-foundations.md>) adds explicit F0/O1–O3/N1–N3/S1 criteria for M5 and D1–D3 storage criteria for M7. These deepen the existing requirements beyond command practice. This note retains the original task/evidence ownership; split the expanded backlog into independently finishable projects before activation. The old 30h allocation and dates are historical planning fields, not capacity for all new requirements. The shared current budget is 15h/week (10 core/labs, 3 project, 2 exploration). No date, checkbox or learning credit changes in this update.

## Done when:

This is the supervised two-worker foundation. The later [[multi-agent-human-review]] project reuses it to test coordinator-led execution and final human review; it does not repeat the language or Linux course.

I can integrate and verify two isolated changes, diagnose an interrupted run, reconcile uncertain outcomes before retrying, and demonstrate Linux recovery using logs.

## Start here:

**Compact pace:** attempt the checkpoint first, read only what you cannot yet explain, and reuse the existing runner/agent. Keep the recorded completion criteria and Boot.dev tasks; a skipped explanation is not a completed course exercise. Dates are ambitious targets with limited slack at 10 hours/week. Review the pace on September 26; move dependent dates if needed.

First operate one worker on a designated Linux lab host. Then add the second adapter, separate worktrees and bounded concurrency. Apply the design readings to observed failure cases.

## Agent runtime build:

Extend the existing runner/agent on one Linux lab host:

```text
FastAPI → Redis + RQ → trusted worker adapter → per-task Docker container
                                             ↓
                              logs + result + timeout + resource limits
```

Use a thin Python API/queue wrapper to invoke the existing agent. Begin with one fixture task and one worker, then a bounded agent task, then the planned second worker. RQ is the initial queue; Celery is an optional later comparison. The trusted adapter owns container launch/cleanup; task containers never receive the host Docker socket. Start with networking disabled for the fixture; verify a restricted egress policy before a provider-backed task.

The additions below expand required scope. Keep the recorded dates and 30-hour allocation provisional; reassess at entry and adjust dependent dates if needed. Distributed deployment and Kubernetes follow only after a working single-host runtime and measured need.

## Tasks:

### VPS 落地 — 2026-09-24

- [ ] 评估并确定 Linux VPS（含 OVHcloud）：用途、预算、配置和访问方式
- [ ] 获取并配置选定的 VPS，验证 SSH 连接和基础运行环境
- [ ] 将下方 Agent Runtime 部署到 VPS，完成一项真实任务并记录人工介入与失败恢复

2026-09-24 用户澄清：OVHcloud VPS 尚未完成；日记勾选只是因为项目里已有重复任务。选购、配置和部署均在此跟踪为未完成。

### 已有学习与建设任务


- [ ] Add the second harness, then two separate worktrees and integrated verification
- [ ] Apply focused system design to the personal agent workflow
    - [ ] Design bounded queues and demonstrate retry/duplicate-task handling
    - [ ] Explain logs, access boundaries, and recovery in a final architecture walkthrough
- [ ] Learn Linux for agent operations using LFS101 and focused labs
    - [ ] Complete command line, permissions, processes, user environment, networking, and security foundations
    - [ ] Demonstrate SSH, signals, services/logs, resource limits, and container/workspace boundaries in a designated lab environment
- [ ] Complete explicit Linux command and scheduling checkpoints
    - [ ] Practice users/groups, sudo, chmod/chown, ps/top/kill, signals and jobs/fg/bg on harmless fixtures
    - [ ] Explain IP, ports, localhost, DNS and HTTP; use curl, ss or lsof, and getent hosts to diagnose listener, DNS and HTTP failures
    - [ ] Run a harmless cron status check with explicit paths/environment and logs; prevent overlap, observe execution and remove the lab entry
- [ ] Demonstrate Docker isolation and least privilege
    - [ ] Explain images/containers, bind mounts/named volumes, networks and published ports
    - [ ] Explain namespaces and cgroups; demonstrate a non-root task, narrow mounts, read-only root filesystem and CPU/memory/PID limits
    - [ ] Verify denied writes and blocked outbound access for an offline fixture; demonstrate an enforced egress policy for a provider-backed task
- [ ] Build the small Agent Runtime around the existing agent
    - [ ] Connect FastAPI POST /tasks and GET /tasks/{id} to Redis + RQ and a fixed, validated task handler; keep the initial API and Redis local/private
    - [ ] Start with one worker, then two with separate workspaces; bound queue admission/concurrency and demonstrate capped retries and duplicate handling
    - [ ] Run each task in a container through the trusted adapter; correlate job ID, logs, result, deadline and resource limits
    - [ ] Demonstrate success, nonzero exit, timeout and a resource-limit failure; verify container and descendant cleanup
    - [ ] Interrupt the worker; recover orphaned containers and reconcile uncertain results before retrying; explain Redis persistence and result retention
    - [ ] Supervise API and worker with systemd; use journalctl to diagnose failure and verify restart recovery
- [ ] Verify remote attachment alongside the Termius/Tailscale task and document daemon/host restart recovery separately
- [ ] 手机通过termius + tailscale 连接

## Decisions and blockers:

- Tasks were moved from the overview on 2026-09-10; no learning completion was inferred.
- Earlier/later parts of broad original task categories now live in the linked section projects. Complete this section from its stated evidence, not the wording of a category label alone.
- Keep examples small and source-grounded; generated agent-learning prose is not required material.

## Progress log:

- 2026-09-30: Curriculum scope expanded at the student’s request: OS/network depth, required storage and security are mapped in the systems module above. Existing tasks and dates preserved; no lab, assessment or implementation completed. Bounded subdivision precedes activation.

- 2026-09-26: At the user’s request, shifted the planned start and target finish / deadline four days later (2026-11-19–2026-12-09 → 2026-11-23–2026-12-13) while they work on another project. Duration, effort allocation, task states and completion records are unchanged.

- 2026-09-24: Added explicit Linux commands, cron, isolation/network restrictions and FastAPI → Redis + RQ → container runtime checkpoints at the user's request. Reuse the existing agent; dates/status and earlier task states are preserved. Reassess the 30-hour allocation at entry. No study or implementation marked complete.

- 2026-09-13: Reforecast after Section 1 completion: JavaScript starts September 13; remaining stages shifted four days earlier with allocations unchanged at 10 focused hours/week. Pace review September 26. Dates remain forecasts.

- 2026-09-10: Compressed at the user’s request to 2026-11-23–2026-12-13, 30 hours. Prior allocations below are historical; tasks and completion states retained.

- 2026-09-10: Section project created from the agreed roadmap; study checkpoint not yet demonstrated.

## Resources:

- [LFS101](https://training.linuxfoundation.org/training/introduction-to-linux/) — selected relevant topics; Bash/process basics began earlier.
- `/Users/seanmacbook/Self-learn/system-design-primer` and `/Users/seanmacbook/Self-learn/system-design-101`.
- Official Git, Linux service/network and container references linked in the repository resource guide.
- [Linux runtime checkpoints and verified source links](/Users/seanmacbook/Projects/agent-workflow-research/learning-resources-research.md#small-agent-runtime--added-september-24-2026) — cron, namespaces/cgroups, Docker network restrictions, FastAPI and Redis + RQ.

Full course design: `/Users/seanmacbook/Projects/agent-workflow-research/ROADMAP.md`. Selected readings: `learning-resources-research.md` in the same repository.
