# Course materials

Everything the course assigns is either in this repository or linked from it with a pinned revision. Select readings for a learning question, then demonstrate the related mechanism. The [roadmap](../ROADMAP.md) owns scope; this shelf owns resource roles; each [module guide](../course/modules/README.md) orders the materials for its milestone.

## Get the materials

Third-party source repositories are Git submodules under `sources/`, pinned to the exact commits the course checked. Clone with them:

```bash
git clone --recursive <this-repository-url>
```

In an existing clone:

```bash
git submodule update --init
```

The eight largest optional repositories (Codex, OpenCode, Cua, vLLM, FlashAttention, llama.cpp, MLX LM, SGLang) are pinned but skipped by default. Fetch one when its lesson starts:

```bash
git submodule update --init --checkout materials/sources/agents/codex
```

Each submodule keeps its own license; read it before copying code into your project. Pins are deliberate: before a version-dependent lesson, compare the pin with upstream and record a precise revision and section when assigning a reading. Moving a pin is a material change, recorded in [versions.md](versions.md).

## Source repositories

| Path | Upstream | Pinned | License | Course role |
|---|---|---|---|---|
| [`agents/learn-claude-code`](sources/agents/learn-claude-code) | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | `0dcafa2ae053` | MIT | M1 tool cycle (s01/s02); later chapters for tasks, subagents, MCP, worktrees |
| [`agents/nanocode`](sources/agents/nanocode) | [1rgs/nanocode](https://github.com/1rgs/nanocode) | `b009d3dbedf1` | none stated | M1/M4 tool dispatch comparison (`nanocode.py`) |
| [`agents/mini-swe-agent`](sources/agents/mini-swe-agent) | [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) | `04d809ceab9d` | MIT | M4 first source trace: loop, model, environment |
| [`agents/pi`](sources/agents/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | `4a080252f06c` (v1.4.0) | MIT | M4 harness and extension study; M19 built-in MCP |
| [`agents/tau`](sources/agents/tau) | [huggingface/tau](https://github.com/huggingface/tau) | `55df51608b8b` | MIT | M4 short comparison |
| [`agents/claude-code`](sources/agents/claude-code) | [anthropics/claude-code](https://github.com/anthropics/claude-code) | `c017428c8c27` | Anthropic commercial terms | Official public repository (plugins, docs, changelog) for M4/M18 comparisons; not product source |
| [`agents/t3code`](sources/agents/t3code) | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | `c3b40b97f751` | MIT | M17 T3 Code case study |
| `agents/codex` *(on demand)* | [openai/codex](https://github.com/openai/codex) | `e16b631d08cd` | Apache-2.0 | M4 required source study after smaller traces and M12 R1 |
| `agents/opencode` *(on demand)* | [anomalyco/opencode](https://github.com/anomalyco/opencode) | `86ce19d96ecc` | MIT | Optional M4 comparison |
| `agents/cua` *(on demand)* | [trycua/cua](https://github.com/trycua/cua) | `1cb7b6fb2415` | MIT | Optional computer-use investigation ([fit review](../research/cua-course-fit.md)) |
| [`skills/mattpocock-skills`](sources/skills/mattpocock-skills) | [mattpocock/skills](https://github.com/mattpocock/skills) | `49dd158d1076` | MIT | M18 skill dissection and comparison |
| [`skills/addyosmani-agent-skills`](sources/skills/addyosmani-agent-skills) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `aeac41d4d005` | MIT | M18 comparison |
| [`skills/cursor-plugins`](sources/skills/cursor-plugins) | [cursor/plugins](https://github.com/cursor/plugins) | `cdb3c41c9f2f` | none stated | M18 comparison (plugin packaging) |
| [`skills/emilkowalski-skills`](sources/skills/emilkowalski-skills) | [emilkowalski/skills](https://github.com/emilkowalski/skills) | `2d228630ba14` | MIT | M18 comparison |
| [`skills/humanlayer-skills`](sources/skills/humanlayer-skills) | [humanlayer/skills](https://github.com/humanlayer/skills) | `653b6411c1f7` | MIT | M18 comparison |
| [`mcp/specification`](sources/mcp/specification) | [modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification) | `ccaf9102ec5e` | MIT | M19 specification and `schema/2026-07-28/schema.ts` |
| [`mcp/typescript-sdk`](sources/mcp/typescript-sdk) | [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | `39ae8e6192cf` | MIT | M19 learner-built server |
| [`mcp/inspector`](sources/mcp/inspector) | [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | `0cac110a809e` | MIT | M19 protocol tracing |
| [`javascript/you-dont-know-js`](sources/javascript/you-dont-know-js) | [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | `044120ef5556` | CC BY-NC-ND 4.0 | M2/M3 selected JavaScript depth |
| [`linux/bash-course`](sources/linux/bash-course) | [bahamas10/bash-course](https://github.com/bahamas10/bash-course) | `0fb288afb1a3` | none stated | M2/M5 YSAP Bash practice |
| [`linux/omarchy`](sources/linux/omarchy) | [omacom/omarchy](https://github.com/omacom/omarchy) | `f0020448ca87 (v4.0.0)` | MIT | M17 Omarchy Quattro case study |
| [`design/system-design-primer`](sources/design/system-design-primer) | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | `ae9bbd7b02d9` | CC BY 4.0 | M7 supporting system-design reference |
| [`design/system-design-101`](sources/design/system-design-101) | [ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101) | `b28380a4710c` | CC BY-NC-ND 4.0 | M7 supporting reference (retries, delivery semantics, idempotency) |
| [`design/grokking-ood`](sources/design/grokking-ood) | [tssovi/grokking-the-object-oriented-design-interview](https://github.com/tssovi/grokking-the-object-oriented-design-interview) | `ba7927f641f2` | none stated | Optional M16 OOD readings ([selection](ood-assessment.md)) |
| [`compilers/craftinginterpreters`](sources/compilers/craftinginterpreters) | [munificent/craftinginterpreters](https://github.com/munificent/craftinginterpreters) | `4a840f70f69c` | MIT code; book text CC BY-NC-ND | M12 compiler/VM reference |
| [`inference/nanochat`](sources/inference/nanochat) | [karpathy/nanochat](https://github.com/karpathy/nanochat) | `d5759400f967` | MIT | M6 inference path (`nanochat/gpt.py`, `nanochat/engine.py`) |
| [`inference/nano-vllm`](sources/inference/nano-vllm) | [GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm) | `bb823b3e0698` | MIT | M9 small serving-engine bridge before vLLM |
| `inference/vllm` *(on demand)* | [vllm-project/vllm](https://github.com/vllm-project/vllm) | `06e172b5cf88` | Apache-2.0 | M9/M10 serving source study; pair with matching docs |
| `inference/flash-attention` *(on demand)* | [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention) | `98c1cee0ed59` | BSD-3-Clause | M9 attention kernels |
| `inference/llama.cpp` *(on demand)* | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | `8ca4060b7e30` | MIT | M6 local inference lane (choose this or MLX LM) |
| `inference/mlx-lm` *(on demand)* | [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm) | `f39c4aa2af5d` | MIT | M6 local inference lane on Apple silicon |
| `inference/sglang` *(on demand)* | [sgl-project/sglang](https://github.com/sgl-project/sglang) | `610a74d64855` | Apache-2.0 | M9 later serving comparison |

Courses, documentation, papers and university lecture pages that are not Git repositories stay online; the [online resource index](online-resources.md) lists every one the course links, with the page that assigns it. Boot.dev, Node Learn/API, the TypeScript Handbook, the Rust Book, LFS101, Kubernetes documentation, MIT 6.5840, Stanford CS329Z/CS336 and the Claude courses are the main ones.

## Choose one reading path

For an active lesson, name one question, one primary source section, an attempt, its evidence and a timebox. Use the milestone row below to find that source. Supporting references answer a specific gap; comparison repositories and electives wait until they have a concrete purpose. Do not turn every link into a completion checklist.

The university selections, Claude materials and source-code studies overlap. Reuse the same runner/agent and one assessment artifact where it demonstrates the same outcome. Preserve explicitly assigned course-completion goals, but do not repeat an equivalent exercise merely because it appears in another syllabus.

[University integration map](university-course-integration.md): selected MIT 6.5840 and Stanford CS329Z blocks, prerequisites, overlap and assessment. These are embedded sources, not parallel full courses.

## Required selections and supporting depth

| Milestone | Main materials and role | Boundary |
|---|---|---|
| M1 | Selected learn-claude-code s01/s02 and tiny Python orientation; [catalog](resource-catalog.md) | Preserve credited tool-cycle evidence; use for gaps or comparison |
| M11 | [Engineering reading map](engineering-practice.md): Git/GitHub docs, review guidance, ADR/TDD sources and installed workflow skills | Explain the workflow and inspect its evidence; skill execution alone is not acceptance |
| M2/M3 | Boot.dev JS/TS ordered curriculum; official Node Learn/API; selected YDKJS; YSAP Bash; CS329Z components after readiness | Language goals plus runner/agent capability checks; no full API-reference reading assignment |
| M4 | Mini-swe-agent → Pi → Codex; M12 R1 Rust readiness; selected official Claude courses/API/MCP material and CS329Z harness design | [Advanced selections](advanced-study.md); short Tau/nanocode comparisons and optional OpenCode |
| M16 | [Paradigm/design source map](../course/modules/programming-paradigms.md): Python functional HOWTO, TS Handbook and Rust Book selections | Required FP/OOD and comparative design; reuse syntax lessons, full reference-course completion optional |
| M13–M15 | [Core-foundations source map](../course/modules/core-foundations.md): selected Nand2Tetris/CS:APP, MIT 6.006 and MIT 6.042J | Required machine, algorithm and proof/probability evidence; selected depth, not full university-course completion |
| M12 | Rust Book, selected compiler theory, Crafting Interpreters, LLVM and rustc guide; [systems reading map](systems-reading-map.md) | Learner-authored tiny typed compiler/VM and mechanism defense; selected references, not full-course completion |
| M5 | Selected LFS101/YSAP for Linux practice; [OS, network and container readings](systems-reading-map.md) for mechanisms | [F0/O/N/S criteria](../course/modules/systems-foundations.md): machine prerequisite credited through M13, OS mechanisms, socket/framing and packet/failure labs, security and service recovery |
| M6 | Python/tensor/attention bridge, nanochat inference path, cache/generation/accounting selections | [C1–C4 and serving introduction](advanced-study.md); teach shapes and assumptions before optimization |
| M7 | Selected MIT 6.5840 replication/consistency/ownership route and CS329Z agent comparison; existing System Design Primer/101 as supporting reference | [Systems reading map](systems-reading-map.md) and required [RabbitMQ/Kafka readings](message-brokers.md); required [D1–D3 local storage](../course/modules/systems-foundations.md) before durable distributed work, retained events and partial-failure reasoning |
| M8 | Official Kubernetes concepts/tasks after Linux, networking and containers | [Systems reading map](systems-reading-map.md); scoped service deployment/recovery |
| M9 | Selected CS336, FlashAttention/PagedAttention papers, vLLM documentation/source; C5–C11 | [Advanced selections](advanced-study.md); controlled experiments, hardware constraints stated |
| M17 | [T3 Code and Omarchy Quattro source map](agentic-linux.md) | Required case studies: request/service ownership, shell/IPC, reversible change and comparison; T1 reuses M4, T3OS waits for published sources |
| M19 | [MCP course/source map](../course/modules/mcp.md), 2026-07-28 specification and schema, official TypeScript SDK/Inspector, Pi built-in MCP sources; Claude Academy A7/A8 | Build and trace one narrow server; compare hosts and alternatives. Extensions are optional depth. |
| M18 | [Agent Skills course/source map](../course/modules/agent-skills.md), official format specification and [five-repository review](../research/agent-skills-review-2026-10-16.md) | Select one relevant workflow; author, evaluate and maintain it. Other collections are comparisons, not mandatory installations or completion lists. |
| M10 | [Distribution release brief](../course/projects/agentic-linux-distribution.md), C12 reliable serving, CS329Z data/evaluation/safety selections and prior coordination/runtime materials | Integrate and defend measured behavior; no new catalog to finish |

The [M16 module](../course/modules/programming-paradigms.md) now closes the previously recorded FP/OOD gaps. Practical system design remains a required thread through the existing agent/distributed milestones.

Optional OOD selections live in [ood-assessment.md](ood-assessment.md); optional backend specializations remain C13. A course badge, downloaded source or public syllabus is not mastery evidence. Record a precise revision/section when assigning a reading.

## Source ledgers

- [Foundation catalog and Linux runtime readings](resource-catalog.md)
- [Agent and inference selections](advanced-study.md)
- [OS/network/container/distributed selections](systems-reading-map.md)
- [Engineering practice readings](engineering-practice.md) · [Message brokers](message-brokers.md) · [T3 Code and Omarchy](agentic-linux.md) · [OOD selections](ood-assessment.md)
- [Repository versions and refresh history](versions.md); raw refresh data and the Grokking case-collision copies are in [provenance/](provenance/refresh-2026-09-11.json)

## Not included

- **Claude Code product source.** The course's earlier notes refer to a user-supplied local snapshot with unverified provenance. It is not redistributed here and is not required; use the official public repository above, official documentation and the open-source harnesses instead.
- **Paid or account-based courses** (Boot.dev, LFS101, Claude courses) cannot be copied. They are linked from the online index.
- **Learner work.** Each learner's own runner, agent and evidence belong in their project repository and progress record, not in `materials/`.
