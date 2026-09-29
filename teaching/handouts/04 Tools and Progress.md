---
title: Coding Agent Course — Tools and Progress
created: 2026-09-11
tags:
  - learning/coding-agents
---
# Tools we will use

[[Notes/Coding Agent Course/00 Start Here|Start Here]] · [[Notes/Coding Agent Course/01 Material Shelf|Material shelf]] · [[Notes/Coding Agent Course/00 Start Here|Project roadmap]]

The course separates tools for daily work, tools we learn to extend, and candidates that must earn a place through trials. This is the agreed working plan; an installed command alone does not establish a working integration.

| Tool | Job in the course | When and current evidence |
|---|---|---|
| Ghostty or cmux | Terminal/workspace for the human; cmux also provides a browser workspace | Early daily practice. Both commands found on PATH September 11 |
| Herdr | Keep terminal panes and reconnect to a named session | Early terminal practice. Command found; repeat the practical persistence checkpoint with the actual harness |
| Claude Code and Codex | Direct coding harnesses, then real workers behind adapters | Use directly early; integrate one first, then the second. Both commands found |
| Pi | Main TypeScript agent/extension reference and proposed coordinator | Source reading and extension stage. Source preserved at `Self-learn/pi`; executable not on PATH in this check |
| DeepSeek | Proposed model behind Pi | Fit, access and exact model selection require a real task trial; not yet accepted as a working integration |
| Tau | Python agent source for comparison | Narrow source readings; a teaching reference rather than another required daily harness |
| Node.js and npm | Run JS/TS exercises and manage project dependencies | JS/Node stage onward. Both commands found; choose version-matched documentation when implementing |
| TypeScript | Express tool, event and worker contracts | TS stage onward; project-local setup belongs to its lesson |
| Git and worktrees | Inspect changes, isolate worker edits and review integration | Diff/review early; worktrees when delegation begins. Git command found |
| Bash | Small launchers and process/environment exercises | YSAP and Node labs; explicitly run Bash scripts with Bash. Interactive zsh and Bash exercises are distinct |
| Linux lab environment | Observe Linux processes, permissions, services, logs and recovery | Foundations early; designated lab host/VM selected before operations work |
| Obsidian and Taskflow | Current phase, next phases, tasks, evidence and actual study time | Existing project notes remain the progress system |
| Paseo / T3 | Candidates for the GUI workflow | Compare during the GUI phase; no winner assumed |
| OMP / Orca | Candidates for an existing-tool team | Compare during the team phase; no new orchestration framework is required |
| Effect | Optional comparison for an understood plain-TS adapter | Later reading/experiment only; not a dependency for starting |

## Working model to test

```text
You → Ghostty or cmux → Herdr → direct Claude Code / Codex
                          └→ Pi + chosen model → adapter → worker harness
```

The direct workflow can begin before the extension/coordination build. Herdr owns terminal continuity; a harness owns its conversation; the coordinator/adapter needs explicit task state and recovery. Each boundary gets its own checkpoint.

## Where current progress and next phases live

Use [[Notes/Coding Agent Course/00 Start Here|the existing course overview]] to navigate and the linked `Projects/Active` notes to track execution. The tool-cycle project is archived as completed; verify current evidence in [[Projects/Active/terminal-agent-02-javascript-node|JavaScript and Node]] before assigning work. Shared tool practice belongs to [[Projects/Active/terminal-human-in-the-loop|Terminal workflow]]. Later phase order is in [[Notes/Coding Agent Course/02 Study Route|Study route]].

The project notes own `status`, `start`, `deadline`, `order`, their `Tasks:` lists and progress logs. The reading room supplies study material and personal annotations. The classroom supplies planning and teaching preparation. At a checkpoint, record your explanation or working evidence and focused time, then update the owning project's status and the next phase when warranted. No parallel checkbox list is maintained here.

## Hands-on starting references

- [Terminal controls and exercises](file:///Users/seanmacbook/Projects/agent-workflow-research/terminal-practice/START-HERE.md).
- [Herdr practice](file:///Users/seanmacbook/Projects/agent-workflow-research/terminal-practice/HERDR.md).
- [Pi source README](file:///Users/seanmacbook/Self-learn/pi/README.md) and [Tau source README](file:///Users/seanmacbook/Self-learn/tau/README.md).
- [YSAP Bash](https://course.ysap.sh/) and [LFS101](https://training.linuxfoundation.org/training/introduction-to-linux/).

The September 11 availability check only looked up commands on PATH; it did not install tools, start sessions, make paid calls or validate integrations.
