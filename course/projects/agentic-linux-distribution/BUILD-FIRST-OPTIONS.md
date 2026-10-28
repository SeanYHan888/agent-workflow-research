# Build while learning — course revision options

Prepared October 4, 2026 after the student asked to start the distribution sooner, learn while building, and focus on essential knowledge. This is a concrete revision proposal. No route has been selected, required milestone retired, or existing deadline moved.

## Status after the October 6 teaching update

Project-first, hands-on teaching is now adopted through [I018 and the current project route](../../../ROADMAP.md#project-route). That decision retains the existing 10 core/lab + 3 project + 2 exploration allocation, M1–M17 graduation requirements and dates. The alternative routes, 8+5+2 split and elective conversions below remain October 4 proposals; they are not the current course agreement.

## Review finding

The current course is broader than the first product needs. Its 584–907h estimate covers the full program, not the minimum knowledge needed to start. Linking every subject to the project did not change the actual sequence enough: the live Linux project still has a December 28–January 17 window after JS, TS and harness work. M10 also requires advanced foundations, compiler, Kubernetes and inference evidence before program completion.

Existing JS/Node, Linux and GUI owners may contain plans and unchecked work; that is not new mastery evidence. Preserve credited M1 work. Begin with a short programming/Linux diagnostic and teach the missing basics inside the first build. Do not assume that the student must restart programming or can already operate a remote service independently.

**Recommendation: choose route A, and introduce a small Rust component in its second slice.** Build a useful node first, extend it to two nodes, then package the proven system as a distribution. A configuration recipe is an early product artifact; it is not the final distribution release.

## Three routes

| Route | First useful artifact | Teaching order | Main tradeoff |
|---|---|---|---|
| **A. Working VPS first — recommended** | A repeatable headless Linux setup with SSH, one supervised fixture worker, logs and limits | Linux/SSH/Git → service/process control → small Rust tool → existing agent integration → two-node work → image/release | Prioritizes early feedback. Start from a supported upstream cloud image; custom image packaging comes after useful behavior. |
| **B. Rust component first** | A Rust worker or management CLI, first tested locally and then supervised on Linux | Rust ownership/errors/tests/processes → Linux service/SSH → agent adapter → two nodes → image/release | More early Rust practice, but language learning delays the first integrated VPS system if R1 is unfamiliar. Use this if writing the core component is the strongest motivation. |
| **C. Declarative OS first** | A version-controlled NixOS configuration and a VM image with SSH and one service | Nix configuration/modules/builds → boot/network/service operation → Rust/agent integration → remote nodes | Makes OS configuration central from day one. Adds Nix/NixOS learning and target-image compatibility work before testing the agent workflow. Measure disk and runtime cost; do not assume it meets the lightweight goal. |

Debian is a candidate base for A/B, subject to the chosen host and agent support. NixOS is a candidate for C. These are route recommendations, not an adopted base or provider. T3 Code/Omarchy remain comparative sources in all routes, without requiring their full environments on every VPS.

## Recommended lineup for route A

These are relative teaching blocks, not calendar assignments. The first block includes the diagnostic and host suitability check. Hours include learning, implementation, debugging and review. Re-estimate after that block; do not compress gaps to meet the table.

| Slice | Learn only what this build requires | Observable result | Initial directed effort |
|---|---|---|---:|
| 1. One controlled Linux node | Basic shell, Git inspection/recovery, SSH identity/keys, users/permissions, processes, services/logs, simple first-boot configuration | Recreate a disposable node, connect, start/stop a fixed harmless task, disconnect/reconnect, inspect logs and recover after restart | 12–18h |
| 2. One useful Rust component | Cargo, ownership/borrowing, enums/Result, config parsing, tests and process/file I/O; add concurrency only when required | Small status/management CLI or worker component with failure behavior and bounded output; reuse rather than translate every earlier artifact | 18–30h |
| 3. One bounded agent job | Existing harness interface, provider access, task validation, workspace isolation, cancellation, resource limits and secret handling | One reviewed agent result on the node, plus denied access, timeout and cleanup evidence | 12–18h |
| 4. Two remote nodes | Job identity/state, one durable state owner, timeouts, leases when needed, retry limits, deduplication and reconciliation | Dispatch bounded jobs to two VPS nodes; recover from disconnect and worker loss without claiming exactly-once external effects | 18–30h |
| 5. Installable alpha | Packages/dependencies, boot/image basics, clean first boot, versioned inputs, updates, recovery, release checks and resource measurement | A supported VPS image, fresh-install instructions, measured limits and recovery evidence | 18–30h |

Total: **78–126 directed hours**, a provisional estimate for a narrow alpha with integrated study. At 15h/week this is roughly **6–9 active weeks** when rounded to full weeks. It is not a release promise or a replacement full-course forecast. Missing programming/Linux foundations, provider setup, image import limits or failed safety/recovery tests can extend it. A useful node is the first deliverable; the student does not wait for the alpha to start building.

Each slice must be independently useful and fit within 21 days. Proposed weekly allocation: **8h guided building, 5h focused explanation/readings, 2h testing/review**. This replaces the old 10+3+2 split within the same 15h total. One primary project supplies the lesson and practical work; there is no separate build lane. The 2h review is part of these effort estimates, not an added charge. Exploration occurs only when it resolves the current design question.

## What must be known, and when

| Gate | Essential knowledge | Adequate entry evidence |
|---|---|---|
| Before the first lab edits | Basic files/commands, Git status/diff/revert, shell exit codes, SSH identity and the selected disposable target | Explain a small change, connect to the intended host, and recover a deliberate harmless mistake |
| Before autonomous agent execution | Process lifetime/cancellation, least privilege, paths/workspaces, credential boundaries, enforced resource/network limits | A fixed fixture demonstrates stop/cleanup and denied access; no unrestricted agent is used to discover these boundaries |
| Before multiple nodes | Persistent job state, authentication, timeouts, uncertain outcomes, bounded retries/concurrency and idempotency limits | Explain a failure history and demonstrate recovery from an interrupted single-node task |
| Before publishing an image | Boot/service/network startup, first-boot initialization, package inputs, identity cleanup, update/restore procedure, checksums and release documentation | Fresh install on the supported target, distinct host identities, no baked credentials, repeatable workload and tested recovery |

Rust foundations are needed before owning the Rust component, not before configuring the first Linux node. Deep compiler knowledge is not needed to use Rust. Local model inference is not required for a small node that calls a separate model endpoint.

## Important gaps to make explicit

The old plan already covers Rust, SSH, networking, security and distributed state broadly. Its main missing practical sequence is **how software becomes an installable, maintainable VPS system**:

1. **Provisioning and repeatable configuration:** first-boot inputs, repeat-safe setup, machine identity and per-host secrets. Use a selected tool such as cloud-init; learn another configuration tool only if repeated updates need it.
2. **Boot and service lifecycle:** the path from boot to network access and the worker service, plus a rescue method if SSH is unavailable. Selected mechanisms are sufficient; a kernel course is not a prerequisite.
3. **Packaging and image construction:** application binary versus OS package versus system image, dependencies, target architecture/libc compatibility and provider image import. Choose one supported target.
4. **Updates and persistent state:** versioned artifacts, package/image updates, data/config compatibility, failed-update recovery, backup and restore. A rollback of binaries does not necessarily restore changed data.
5. **Release trust and maintenance:** upstream package verification, component/license records, separation of build/runtime secrets, artifact verification and a bounded supported-version policy. Apply proportionate release checks to the chosen delivery method.
6. **Resource accounting:** CPU/RAM/disk budgets, bounded queues/logs, pressure tests and base-OS versus agent overhead. “Lightweight” must have a workload and measurements.

These are proposed practical parts of M5/M10/M11/M17, taught during the relevant build slices. They are not six new full courses or hours to add again to the alpha estimate.

## Proposed reduction of prerequisites

| Existing scope | Proposed placement for a project-focused course |
|---|---|
| M2/M3 full JS/TS completion before systems work | Use a diagnostic and only the language needed for the chosen harness/adapter. Preserve existing language-course goals as separate deferred commitments unless the student explicitly retires them. They would not gate the first release. |
| M4 full mini-swe-agent → Pi → Codex source sequence and GUI comparison | Study one actual request/process path when integrating a harness. Defer the full comparison sequence. |
| M12 compiler K1–K5 | Keep R1 Rust foundations early; propose compiler construction as later elective depth for this product-focused course. |
| M13–M16 complete foundation assessments | Teach relevant memory, data structures, state invariants and design concepts as needed. Propose the remaining full milestone depth as later electives; retain valid prior evidence. |
| M7 full storage/MIT/RabbitMQ/Kafka sequence | Keep job-state, transactions, partial failure, retry/reconciliation and bounded queues before distribution. Use an existing store/queue first; full broker comparison, replication theory and toy database construction can be later depth. Do not implement a new consensus protocol for the alpha. |
| M8 Kubernetes | Later elective unless the measured deployment problem requires it. A two-node system can first use a simpler service deployment. |
| M6/M9 local and distributed inference internals | Keep provider boundary, latency/cost, rate limits and model/agent resource separation. Defer kernels, GPU parallelism and inference-engine implementation. |
| M17 T3 Code/Quattro | Early short architecture comparison and selected traces during the build; full desktop extension study later if it contributes to the product. T3OS remains pending public material. |
| M10 all-M1–M17 graduation dependency | Propose a release gate based on the six product goals and relevant safety/reliability evidence. Keep full-program completion distinct if the student retains the broader program. |

This is a material scope change. It should not be recorded as a completed milestone, or as cancellation of the student's earlier completion goals. Selecting the route also requires confirming which broader requirements become elective versus retained for later study.

## First session and calendar impact

The first session would check shell/process/Git/SSH readiness, review the actual available host, then begin a fixed fixture service on a disposable target. It can use familiar Python or shell while the Rust component is introduced in slice 2. The teacher should ask for learner predictions and attempts, then review them; this proposal is not a completed exercise.

The last confirmed return date is **October 12**, after the September 28–October 11 break. “As soon as possible” is recorded as a priority, not assumed to cancel that break. Route selection would bring a bounded Linux project ahead of the existing JS → TS → Pi → GUI → worker → Linux sequence. The current project windows would need review under the charter. No calendar field changes in this proposal.

Existing Linux-note choices (FastAPI, Redis/RQ and per-task containers) remain a reference implementation for evaluation. The student has not selected their removal or a full Rust rewrite. Compare their fit with the resource budget before choosing components. No host provisioning, paid service or deployment is started by this document.

## Primary references checked October 4, 2026

- [cloud-init documentation](https://docs.cloud-init.io/en/latest/) describes first-boot configuration of networking, storage, SSH keys and packages. This supports the provisioning lesson; it is not a full lifecycle configuration solution by itself.
- [Debian cloud documentation](https://wiki.debian.org/Cloud/) is an entry point for supported cloud images and their use. Check the chosen provider and architecture before adopting a base.
- [Rust Book CLI project](https://doc.rust-lang.org/book/ch12-00-an-io-project.html) combines input/output, error handling, organization and tests. It supports a narrow R1 bridge; the learner's product component needs its own behavior and assessment.
- [NixOS manual](https://nixos.org/manual/nixos/stable/) documents system configuration, upgrades, service management and image construction. Route C adds these mechanisms to the early learning load.

The route ranking and effort ranges are teaching judgments, not claims from these sources or measured student pace.
