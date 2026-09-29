# VPS lab — imported concepts and roadmap

Imported September 28, 2026 at the student's request from the Oracle VPS work. This workspace now owns the learning concepts and curricular roadmap. The original `/Users/seanmacbook/Peronsal/oracle-vps` workspace remains in place. Its sole status file is now preserved in this repository, while its old Codex chat and paused monitor still reference the original working directory. See the [retirement assessment](../../research/oracle-folder-retirement.md); no folder deletion or cloud change occurred.

## Purpose and evidence boundary

The established direction is a remote Linux environment for agent work, with Tailscale/Herdr considered for remote access and terminal continuity. Relate it to M2 processes, M5 OS/network/container operation and later M7 distributed work. Model inference remains a separate workload/hardware decision, not an assumed capability of the first low-cost host.

The related chat **Plan Oracle Cloud Free VPS setup** records an approximately **$5/month** budget on September 24. Retain that as the previous planning preference, not purchase authorization or proof that a suitable current plan exists. Provider offers, billing/renewal terms and workload fit need fresh verification when selecting a plan.

The inspected [preserved STATUS.md](../../archive/2026-09-28-oracle-project-source/STATUS.md) records a September 24, 2026 capacity report for Oracle A1 2 OCPUs / 12 GB in San Jose returning `OUT_OF_HOST_CAPACITY`; it records no successful launch. Later accessible chat turns report sign-in/network blockers. **Current host availability and account state were not checked during this import.** Keep provisioning paused unless the student explicitly resumes it. No monitor or automation was changed.

## Concepts to learn from the project

| Concept | Course connection | Evidence the learner should produce |
|---|---|---|
| Quota/eligibility versus actual host capacity | M5 resource allocation and operational evidence | Explain why a selectable/free-eligible shape or an old capacity report does not guarantee a VM now |
| CPU architecture and workload fit | M2/M5 processes, packaging and containers | Identify ARM/x86 requirements for the proposed binaries/images and separate host RAM from a model-serving requirement |
| SSH identity and access paths | M5 authentication, networking and permissions | Draw who connects to which host/service and explain key ownership and permitted access |
| Public/private connectivity | M5 addressing, routing, firewalls and overlay networks | Trace an intended request and diagnose which layer prevents it |
| Terminal persistence versus application recovery | M4/M5 state ownership | Demonstrate reconnecting to a terminal separately from resuming a conversation or recovering durable job state |
| Lifecycle, storage and cost | M5 operations | Explain stop, reboot, resize, migration and deletion effects; account for retained storage and recurring charges using current provider evidence |
| Observation and bounded automation | M5/M7 | Distinguish reporting capacity from provisioning; report unknown state honestly and define when human action is needed |
| Acceptance and rollback | M11 engineering practice | Produce a concrete service acceptance packet and an understood recovery procedure |

## Staged roadmap

V1–V6 are lab slices mapped to existing milestones, not six new required graduation milestones. Estimates are provisional. Each activated execution project stays within 21 days at its actual allocation; unscheduled slices keep dates blank.

| Slice | Entry and course fit | Deliverable / acceptance | Initial effort and time source |
|---|---|---|---|
| V1. Reuse context and decide requirements | Eligible now as I001 exploration | One workload/topology brief using prior Oracle work and recorded budget; identify remaining provider/cost/access questions. No duplicate vendor search unless needed. | Up to 2h exploration |
| V2. Select and obtain an understood host | Basic Linux/SSH readiness; explicit current rental/provisioning instruction | Fresh authorized capacity/plan evidence and a scoped host choice; if obtained, record OS/architecture, access and recovery boundary. If unavailable, defer or compare a fallback. | 2–3h project work, excluding unpredictable provider waiting |
| V3. Demonstrate remote access and continuity | Host/access established; relevant M5 networking lesson | Verify intended SSH/private-access path; demonstrate terminal disconnect/reconnect with the chosen tool and explain what did and did not persist. | 3–6h project work |
| V4. Run one bounded agent task | M3/M4 worker prerequisites | One read-only task then an authorized bounded change, isolated workspace, logs, interruption and evidence-based acceptance | 3–6h project work |
| V5. Operate and recover one service | M5 services/state/resource limits | Demonstrate startup, logs, limits and controlled restart/recovery; distinguish process, job and conversation state | 3–6h project work |
| V6. Containerize and extend only as justified | Single-host behavior understood | One container/service comparison, then reuse evidence in M7 coordination; Kubernetes and distributed serving follow M8/M9 gates | Estimate one contained slice at entry |

At three project hours/week, a six-hour slice spans two weeks. Waiting for capacity consumes elapsed calendar time but is not study effort; use local/disposable exercises while waiting and review the project scope rather than indefinitely extending its deadline. Do not claim the entire roadmap fits one execution project.

## Ownership and import scope

The existing [Linux coordination note](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-06-linux-coordination.md>) owns three unfinished VPS actions. Use that owner or explicitly split/link its tasks during the approved reforecast, preserving history and one owner per action. The former generic [I001 brief](../ideas/I001-vps.md) now routes to this roadmap.

This import includes purpose, concepts, sequence, prior decisions, evidence limits and source pointers. It excludes SSH key contents, credentials, cloud identifiers/configuration, operational scripts, monitoring relocation and account actions. The old operational record remains authoritative for its dated observations; this page is authoritative for course placement. New live checks belong with operational evidence and are linked, not silently copied into curriculum as timeless facts.

## Sources and access limitations

- Local [preserved STATUS.md](../../archive/2026-09-28-oracle-project-source/STATUS.md), read September 28; source SHA-256 `d4158bc919e47e8950ea046cf95aa0b87dccd111650fbe2b11e3f09002dc08a8`.
- Related accessible Codex chat **Plan Oracle Cloud Free VPS setup**, thread `01a0c09c-e6df-7391-9bad-1fd159c7d752`; read-only retrieval verified the September 24 budget request and later capacity-check blockers.
- User-supplied [shared chat](https://chatgpt.com/s/cx_6abaf4fdeccc8191a39006875189ebc2): direct web retrieval failed; after a browser retry, the in-app page explicitly displayed “Shared chat not found.” Retained as a reference; this import does not claim its full content was read or that it is identical to the related local chat.

The original folder currently contains only STATUS.md in the inspected file inventory. The staged teaching route above is our synthesis from the available sources, not a recovered pre-existing roadmap document.
