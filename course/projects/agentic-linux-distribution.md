# Final project — publish an agent-first Linux distribution

Selected by the student on October 4, 2026. This is the product direction for **M10**, with dedicated [M17 T3 Code and Omarchy Quattro study](../modules/agentic-linux.md). It is a long-term project family. Each execution slice will have one Obsidian owner and a deliverable that fits within 21 days.

The [project folder](agentic-linux-distribution/README.md) records the student's six goals: **Rust, easy remote SSH, distributed system, agentic first, safety and lightweight operation on multiple remote VPS nodes**. This is the course's main practical goal. Modules develop its components and evidence; M10 integrates and publishes them. The final architecture remains open.

## First release boundary

Plan a small derivative of an existing Linux base for one declared architecture and one supported VPS profile, tested on at least two remote VPS instances. Select the base after M17; studying Omarchy does not require an Omarchy fork. The distribution should make an agent workflow a normal part of using the system. Nodes must support headless use over SSH without a desktop, GPU or local model weights.

For version 0.1, a user must be able to obtain a versioned deployable system image, boot it through the supported VPS installation path, connect over SSH, configure their own provider access, run a bounded task, inspect and interrupt it, review its changes, and recover from a documented failure. Select the image format from the target's requirements; a desktop ISO is not assumed. A setup script can be an intermediate artifact. The final publication target includes the image, build recipe and release documentation.

The first design decision must identify the intended user, one important workflow and one improvement over the existing tools. Compare that workflow with a plain upstream setup. Packaging alone does not prove that the integration is useful.

## Acceptance evidence

| Area | Required demonstration |
|---|---|
| Rust systems component | Use Rust for a suitable component owned by the project; select its boundary through a small experiment. Explain and test errors, cancellation, concurrency and resource use. Reuse R1 and existing service work; no full rewrite is required. |
| Remote SSH workflow | Show first connection with host identity verification, node inspection, disconnect/reconnect, access revocation and recovery from bad configuration. Record user steps and human time. |
| Lightweight VPS target | Declare CPU/RAM/disk limits and workload before measurement. Report base OS cost separately from added services, at idle and under bounded load. Test memory/disk pressure and bounded logs/queues. Numerical targets remain open until the first target experiment. |
| Build and installation | Record upstream versions, package inputs and build commands. Build from a clean environment and install on a fresh test target. Publish checksums and build logs. Repeatable installation is required; claim byte-identical builds only if tested. |
| Agent workflow | Show task entry, visible execution state, review, cancellation and resume. Explain which component owns each process, session, checkout and result. |
| Safety and access boundaries | Use ordinary user permissions for normal agent work. Test a denied action, cross-workspace access, untrusted instructions that request more authority, and an explicit elevation path. Keep personal credentials out of the image and logs. Record actions and demonstrate recovery. |
| Updates and recovery | Demonstrate one update and one failed-update recovery path. State what rollback restores and what needs backup. Record supported versions and known failures. |
| Distributed system | Retain M10's durable jobs, isolated workers and model-serving boundary. Demonstrate operation across at least two real remote VPS nodes, duplicate delivery, link failure, worker/server loss, cancellation and overload. Place larger services or model execution separately when needed; each small node need not contain every course component. |
| Evaluation | Compare a fixed workload with a baseline. Report correctness, latency, resource use, failures and human intervention. Separate measured results from assumptions and simulation. |
| Public release | Provide source/build instructions, component notices, installation and recovery guides, supported-target limits, release notes and an issue-reporting route. Verify the uploaded version and a fresh download when publication is authorized. |
| Learner defense | Explain design choices and diagnose an unfamiliar failure under the shared rubric. Agent-generated artifacts alone do not establish mastery. |

Kernel development, broad hardware support, a new package manager and a replacement agent harness are outside version 0.1. M12 compiler and M13–M16 evidence remain graduation requirements; those teaching artifacts do not need to ship in the image.

## Sequence of bounded work

1. **Design brief and upstream comparison:** reuse M17 C1 and M5/M6 resource evidence. Decide the user, workflow, base, Rust component and supported VPS profile. Set measurable resource limits.
2. **Bootable VPS baseline:** one minimal image, the supported deployment path, a first SSH connection and a resource baseline; initially 6–9h.
3. **Agent integration:** connect the selected interface to the existing worker/service; use the original M10 integration allowance and prior M4/M5 components. Split into 6–9h slices at entry.
4. **Update and recovery:** one controlled change and a recovery drill; initially 6–9h of distribution-specific work.
5. **Distributed evaluation and defense:** reuse the original M10 workload and failure tests, split into 6–9h execution slices.
6. **Release preparation:** source/build packet, notices, guides and clean-download check; initially 6–9h, with up to 3h of review in a separate primary lesson if needed.

The distribution adds a provisional **18–30h** to M10's existing **35–55h**, giving **53–85h** for M10. M17 adds separate study time. These estimates assume a narrow derivative and reuse of working course components, including the Rust and distributed-service work. They have not yet been validated against the VPS target or image delivery method. The first target experiment and C1 must test these assumptions before build work begins. An unsuitable build host, difficult image tooling or wider scope requires a revised estimate, not unpaid extra work.

## Ownership and current state

The live course overview links this direction. The existing GUI note owns T1. The existing team project remains a bounded M7/M10 contributor; its older “final capstone” wording is historical. It does not own this entire distribution backlog.

Before each slice starts, select or create its one owning project, record the entry evidence and allocated hours, and set dates within the 21-day limit. No new project is active and no release date is promised by this plan. The student's publication goal is recorded; uploading an actual release follows review of the concrete artifact and task-specific publication authorization under the charter.
