# Distributed AI Agent Systems

A project-first course on agentic workflows and Linux systems. You learn how coding agents work (the tool loop, harnesses, skills, MCP), how to build and evaluate one, and the Linux, networking, distributed-systems and inference foundations needed to run agents safely across machines. One project carries the whole course: a controllable runner grows into a typed agent, a supervised Linux worker, durable work across remote nodes and finally a published, lightweight **agent-first Linux distribution** for small VPS nodes.

Every session is a small build, debugging task or experiment: the learner attempts it first, the missing concept is taught at the point of need, and the session ends with observed behavior and the learner's own explanation.

## Get started

```bash
git clone --recursive <this-repository-url>
```

The `--recursive` flag fetches the pinned source repositories the course reads (Pi, mini-swe-agent, learn-claude-code, the MCP SDK, the skills collections, nanochat and others). See [materials](materials/README.md#get-the-materials) for the optional large ones and for adding them to an existing clone.

Then:

1. Read the [charter](course/CHARTER.md) for how the course adapts and the 15-hour weekly budget.
2. Skim the [roadmap](ROADMAP.md): four stages, nineteen milestones and the project route.
3. Start with [M1 — the agent tool cycle](course/modules/agent-tool-cycle.md) and [M2 — programs and processes](course/modules/programs-and-processes.md).
4. Keep your own progress record (tasks, dates, evidence) outside the course files; [my-progress](my-progress/README.md) shows one learner's.

No formal prerequisites beyond a computer and a terminal. The course teaches JavaScript/TypeScript, Node, Bash, Python where needed, Rust, and the mathematics and systems theory as it goes; short diagnostics decide where each learner enters and credit what they already know.

## What's here

| Folder | Contents |
|---|---|
| [ROADMAP.md](ROADMAP.md) | Milestones, project route, dependencies, subject boundaries |
| [course/](course/CHARTER.md) | Charter, [assessment rubric](course/ASSESSMENT.md), [workload forecast](course/WORKLOAD.md), [project catalog](course/PROJECTS.md), [idea intake](course/IDEAS.md), [decision record](course/DECISIONS.md) |
| [course/modules/](course/modules/README.md) | One guide per milestone: checkpoints, labs, failure experiments, materials |
| [course/projects/](course/projects/agentic-linux-distribution.md) | The distribution capstone brief and bounded course projects |
| [materials/](materials/README.md) | Reading maps per milestone, [pinned source repositories](materials/README.md#source-repositories), [online resource index](materials/online-resources.md), version records |
| [teaching/](teaching/README.md) | Session workflow for the teacher (human or agent) and a worked session |
| [research/](research/README.md) | Tool investigations behind course choices: harness edit tools, skills repositories, MCP, Cua, university course fit |
| [my-progress/](my-progress/README.md) | One learner's schedule, ideas, VPS operations and practice work — not part of the course |
| [GLOSSARY.md](GLOSSARY.md) · [HISTORY.md](HISTORY.md) | Course vocabulary · where earlier plans and snapshots went |

## The milestones

| Stage | Milestones |
|---|---|
| I. Foundations | M1 agent tool cycle · M2 programs and processes · M3 typed agent · M11 engineering practice · M13 computer organization · M14 algorithms · M15 discrete mathematics · M16 programming paradigms |
| I–II. Agent workflows | M18 agent skills · M19 Model Context Protocol |
| II. Reliable single-host systems | M4 agent harnesses · M5 Linux, OS, networks and security · M6 model inference · M12 Rust and a small compiler |
| III. Distributed systems | M7 durable distributed work and message brokers · M8 Kubernetes · M9 efficient and distributed inference |
| II–IV. Agentic Linux and capstone | M17 T3 Code and Omarchy Quattro · M10 publish and defend an agent-first Linux distribution |

Estimated total: 609–943 directed hours at about 15 hours a week ([forecast](course/WORKLOAD.md)). Milestones are learning destinations, not calendar dates; each is assessed by a working artifact, the learner's explanation and an unfamiliar change ([rubric](course/ASSESSMENT.md)).

## For agents teaching this course

[AGENTS.md](AGENTS.md) holds the standing instructions: teach through learner attempts, keep milestone changes under the charter's change process, and never complete the learner's exercises.
