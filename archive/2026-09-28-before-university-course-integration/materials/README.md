# Course materials

Select readings for a learning question, then demonstrate the related mechanism. The [roadmap](../ROADMAP.md) owns scope; this shelf owns resource roles. Existing version/source checks below retain their dates and must be rechecked before version-dependent lessons.

## Required selections and supporting depth

| Milestone | Main materials and role | Boundary |
|---|---|---|
| M1 | Selected learn-claude-code s01/s02 and tiny Python orientation; [catalog](resource-catalog.md) | Preserve credited tool-cycle evidence; use for gaps or comparison |
| M11 | [Engineering reading map](engineering-practice.md): Git/GitHub docs, review guidance, ADR/TDD sources and installed workflow skills | Explain the workflow and inspect its evidence; skill execution alone is not acceptance |
| M2/M3 | Boot.dev JS/TS ordered curriculum; official Node Learn/API; selected YDKJS; YSAP Bash | Language goals plus runner/agent capability checks; no full API-reference reading assignment |
| M4 | Mini-swe-agent → Pi → Codex; scoped Rust bridge; selected official Claude courses/API/MCP material | [Advanced selections](advanced-study.md); short Tau/nanocode comparisons and optional OpenCode |
| M5 | Selected LFS101/YSAP for Linux practice; [OS, network and container readings](systems-reading-map.md) for mechanisms | Dedicated OS/network lessons and VPS/service failure labs, not only command memorization |
| M6 | Python/tensor/attention bridge, nanochat inference path, cache/generation/accounting selections | [C1–C4 and serving introduction](advanced-study.md); teach shapes and assumptions before optimization |
| M7 | Selected distributed-systems readings and source cases; existing System Design Primer/101 as supporting reference | [Systems reading map](systems-reading-map.md) and required [RabbitMQ/Kafka readings](message-brokers.md); durable work, retained events and partial-failure reasoning |
| M8 | Official Kubernetes concepts/tasks after Linux, networking and containers | [Systems reading map](systems-reading-map.md); scoped service deployment/recovery |
| M9 | Selected CS336, FlashAttention/PagedAttention papers, vLLM documentation/source; C5–C11 | [Advanced selections](advanced-study.md); controlled experiments, hardware constraints stated |
| M10 | C12 reliable serving plus prior coordination/runtime/evaluation materials | Integrate and defend measured behavior; no new catalog to finish |

Optional OOD selections live in [ood-assessment.md](ood-assessment.md); optional backend specializations remain C13. A course badge, downloaded source or public syllabus is not mastery evidence. Record a precise revision/section when assigning a reading.

## Source ledgers

- [Foundation catalog and Linux runtime readings](resource-catalog.md)
- [Agent and inference selections](advanced-study.md)
- [OS/network/container/distributed selections](systems-reading-map.md)
- [Historical repository versions](versions.md)

## Preserved local source shelf


The user chose links to the existing repositories on September 11, 2026. These seven directory shortcuts point to the maintained copies under Self-learn; opening or editing a shortcut operates on that original repository.

| Shortcut | Source location | Upstream HEAD verified September 11 |
|---|---|---|
| [tau](tau/README.md) | `/Users/seanmacbook/Self-learn/tau` | `55df51608b8b` |
| [pi](pi/README.md) | `/Users/seanmacbook/Self-learn/pi` | `71dca871bc80` |
| [learn-claude-code](learn-claude-code/README.md) | `/Users/seanmacbook/Self-learn/learn-claude-code` | `0dcafa2ae053` |
| [you-dont-know-js](you-dont-know-js/README.md) | `/Users/seanmacbook/Self-learn/You-Dont-Know-JS` | `044120ef5556` |
| [system-design-primer](system-design-primer/README.md) | `/Users/seanmacbook/Self-learn/system-design-primer` | `ae9bbd7b02d9` |
| [system-design-101](system-design-101/README.md) | `/Users/seanmacbook/Self-learn/system-design-101` | `b28380a4710c` |
| [grokking-ood](grokking-ood/readme.md) | `/Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview` | `ba7927f641f2` |

All seven were refreshed with `git pull --ff-only` and compared with upstream on September 11. The links are specific to this Mac. [Material versions](versions.md) records the results and the Grokking case-only filename collision; [both colliding originals](grokking-ood-case-collision/README.md) are preserved separately.

On September 11, Tau and Pi were moved directly into Self-learn at the user's request. Their complete file/symlink manifests matched before and after (Tau: 493 entries; Pi: 1,789), their Git HEADs were unchanged, and both worktrees remained clean. The generated agent-learning parent was then deleted. The shortcuts above now point to the new locations.

Additional optional shelf entry: [Grokking OOD](grokking-ood/readme.md), at `/Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview`. Use only the [selected design readings](ood-assessment.md) when needed for the TypeScript or worker-adapter stages.

For all online courses, documentation and selected reading assignments, open the [student material shelf](../teaching/handouts/01%20Material%20Shelf.md). Boot.dev, Node, YSAP and LFS101 remain web resources. Course-authored handouts live in [teaching/handouts](../teaching/README.md).

## Online agent sources — added September 15, 2026

- [nanocode](https://github.com/1rgs/nanocode/blob/b009d3dbedf14795a5c10804a5455386563f4b5b/nanocode.py): Section 3 tool/dispatch comparison; inspected master `b009d3dbedf14`.
- [mini-swe-agent v2](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/src/minisweagent/agents/default.py): Section 4 loop/model/environment comparison; inspected main `04d809ceab9d`.

These are pinned online readings, not additional local checkouts. See [assigned symbols, timeboxes and checkpoints](resource-catalog.md#nanocode-and-mini-swe-agent--added-september-15-2026). The seven local shortcuts above retain their existing locations.

## Extended source shelf — September 28, 2026

See [the expanded research plan](advanced-study.md) for Codex, OpenCode, official Claude courses, inference references and their assigned roles. New web repositories remain reading references; this update does not clone or install them.

Existing local additions discovered for future study:

- [nanochat model](</Users/seanmacbook/Projects/nanochat/nanochat/gpt.py>) and [engine](</Users/seanmacbook/Projects/nanochat/nanochat/engine.py>): local revision and proposed reading role recorded in the plan.
- [Claude Code source snapshot](</Users/seanmacbook/Projects/claude-code/src>): user-supplied source with unverified provenance; separate from the open-source references and the third-party learn-claude-code teaching project.
