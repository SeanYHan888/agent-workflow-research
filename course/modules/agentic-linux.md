# M17 — T3 Code and Omarchy Quattro

Dedicated course accepted October 4, 2026. The student selected an agent-first Linux distribution as the final project and requested dedicated study of T3 Code and Omarchy Quattro. This course connects their mechanisms to the [M10 distribution capstone](../projects/agentic-linux-distribution.md). It uses the same 15-hour weekly budget.

## Outcome

Explain how an agent interface and its execution service connect to Linux hosts, including a desktop case study and headless remote VPS use. Use source traces and controlled experiments to choose the design of the student's distribution. Define “agent-first” through observable behavior: the user can start work, inspect its state, set access limits, interrupt execution, review changes and recover after failure.

T3 Code and Omarchy are required case studies. The distribution's base, interface and package choices remain open until the comparison. The [six project goals](../projects/agentic-linux-distribution/README.md) guide that comparison. Omarchy desktop study informs interface and extension design; the VPS node must also work without a graphical session. T3 Code and model serving need not run on every node. The student's view that these projects lead this area is a reason to study them, not a verified ranking. T3OS is teased, according to the student's clarification; no published specification or release was supplied. Revisit it at course entry if official material is available. It is not a prerequisite.

## Course blocks and evidence

| Block | Learning question and required evidence | Entry and hours |
|---|---|---|
| T1. T3 Code request path | Trace input through client, server, provider and returned events. Explain session ownership, permissions, cancellation and reconnect. Record source revision and actual files. | Existing M4 GUI exercise; retain its owner and budget. Credit only demonstrated evidence. |
| T2. T3 Code on Linux | Explain service identity, startup, configuration, state and logs. In an isolated lab, test one service interruption and one access boundary. Separate a visible approval prompt from enforced OS access. | T1 and relevant M5 service/network/permission evidence; 6–9h of new depth. |
| Q1. Omarchy Quattro architecture | Trace one desktop action through shell/IPC to an OS operation. Map installation, packages, user settings and update ownership. Explain what shares a failure boundary. | M2 process/Bash and relevant M5 Linux evidence; 6–9h. |
| Q2. A reversible desktop extension | Make one small extension or configuration change in a disposable environment. Test its behavior, removal and recovery from a broken setting. Explain the boundary between upstream code and the user's changes. | Q1; learn only the QML/JavaScript needed for this path; 6–9h. |
| C1. Compare and select | Compare the same bounded workflow with and without the proposed integration. Record user steps, human minutes, failures, access limits and recovery. Measure the extra cost on a small VPS profile. Defend the base/interface choice, identify a suitable Rust component, and state which services belong on a headless node or a separate controller. Define the smallest useful release and its resource limits. | T2/Q2 and existing M11 review practice; 6–9h. |

New directed work totals **24–36h**. T1 stays inside the existing M4 GUI allocation. M5 instruction in services, permissions and networking stays in M5. The new hours pay for these products' mechanisms and the comparison. Full React, Effect, Qt/QML courses and complete product rewrites are outside this selection.

Use the [source map](../../materials/agentic-linux.md). At lesson entry, record an exact revision and check current interfaces. Prepare only the next eligible lesson: prediction, learner attempt, source reading, experiment and feedback. This outline does not supply completed learner exercises.

## Practical slices and assessment

T2, Q1, Q2 and C1 can each supply one independent 6–9h project, including preparation and review. At three project hours/week, each takes at most three weeks. Use one at a time. If setup exceeds the allowance, split the outcome before activation. The [project catalog](../PROJECTS.md) routes ownership; new execution notes and dates wait until activation.

Apply the [shared rubric](../ASSESSMENT.md): working evidence, learner explanation, an unfamiliar fault/change, and a statement of limits. A running desktop or installed application does not establish mastery. Reuse T1's GUI evidence instead of creating another source-reading checklist.

## Placement

M4 supplies T1. Relevant M5 checkpoints enable T2 and Q1. Q2 follows Q1; C1 follows both study paths. M17 need not wait for all distributed/inference work, and it does not block unrelated eligible lessons. Its design decision feeds M10. The existing mini-swe-agent → Pi → Codex route and M1–M16 outcomes remain required.

No required study is added to the September 28–October 11 break. Existing project dates remain; M17 has no assigned dates. The [workload forecast](../WORKLOAD.md) records the added scope and uncertainty.
