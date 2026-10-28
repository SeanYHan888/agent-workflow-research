# Course history

Earlier plans, migration snapshots and compatibility pages were removed from the working tree on October 27, 2026 when the repository was reorganized into a shareable course. Every file is still in Git. They are historical records: their dates, schedules and relative links describe the course at that time, not current requirements.

The last commit containing all of them is `24fa53c`. To read or restore any of them:

```bash
git show 24fa53c:archive/2026-10-17-before-mcp/README.md
```

```bash
git restore --source=24fa53c -- archive/2026-10-17-before-mcp
```

The [decision record](course/DECISIONS.md) explains each curriculum change; this page only says where the before-and-after copies went.

## Archive snapshots

Each snapshot preserves the affected files immediately before a curriculum change. Most include a `manifest.json` with SHA-256 hashes and, where navigation notes changed, copies of the Obsidian notes as they were.

### 2026-09-10-before-compact-schedule

Plan before the compact 160-hour/16-week schedule; six terminal-agent project notes. 14 files under `archive/2026-09-10-before-compact-schedule/`.

### 2026-09-10-before-course-redesign

Plan and resource research before the September 10 redesign retired the generated agent-learning chapters. 3 files under `archive/2026-09-10-before-course-redesign/`.

### 2026-09-10-project-split

Task migration map from splitting the original terminal project. 2 files under `archive/2026-09-10-project-split/`.

### 2026-09-10-three-workflows

The nine original Obsidian project notes and three course documents for the terminal, GUI and team workflows. 14 files under `archive/2026-09-10-three-workflows/`.

### 2026-09-28-before-brokers-vps-migration

Course files before RabbitMQ/Kafka were added to M7 and VPS operations moved out of the course. 13 files under `archive/2026-09-28-before-brokers-vps-migration/`.

### 2026-09-28-before-engineering-vps-addition

Course files before M11 engineering practice and the VPS idea were added. 15 files under `archive/2026-09-28-before-engineering-vps-addition/`.

### 2026-09-28-before-program-structure

Original documents and migration map before the four-stage program reorganization, including the first 160-hour foundation roadmap. 46 files under `archive/2026-09-28-before-program-structure/`.

### 2026-09-28-before-university-course-integration

Course files before selected MIT 6.5840 and Stanford CS329Z material was embedded. 12 files under `archive/2026-09-28-before-university-course-integration/`.

### 2026-09-28-course-cleanup

September 28 audit, removed navigation leftovers, a retired terminal setup script and pre-edit vault snapshots. 30 files under `archive/2026-09-28-course-cleanup/`.

### 2026-09-30-before-core-foundations

Curriculum v1.4 before M13–M15 (computer organization, algorithms, discrete mathematics). 35 files under `archive/2026-09-30-before-core-foundations/`.

### 2026-09-30-before-programming-paradigms

Curriculum v1.5 before M16 programming paradigms and design. 34 files under `archive/2026-09-30-before-programming-paradigms/`.

### 2026-09-30-before-relocation-reschedule

All dated project notes before the relocation/conference postponement. 34 files under `archive/2026-09-30-before-relocation-reschedule/`.

### 2026-09-30-before-systems-foundations

Curriculum before M12 Rust/compiler construction and the M5/M7 depth changes. 37 files under `archive/2026-09-30-before-systems-foundations/`.

### 2026-10-04-before-agentic-linux

Curriculum v1.6 before M17 T3 Code/Omarchy Quattro and the distribution capstone. 27 files under `archive/2026-10-04-before-agentic-linux/`.

### 2026-10-06-before-project-first

Course files before project-first teaching was adopted. 27 files under `archive/2026-10-06-before-project-first/`.

### 2026-10-16-before-agent-skills

Curriculum v1.8 before M18 Agent Skills. 14 files under `archive/2026-10-16-before-agent-skills/`.

### 2026-10-17-before-mcp

Curriculum v1.9 before M19 Model Context Protocol. 16 files under `archive/2026-10-17-before-mcp/`.

The Oracle project source (`archive/2026-09-28-oracle-project-source/`) was not removed. It is the only copy of that operational evidence and now lives in [my-progress/operations/vps/oracle-source](my-progress/operations/vps/oracle-source/README.md).

<a id="removed-documents"></a>
## Removed documents

| Former path | Replacement |
|---|---|
| `learning-resources-research.md` | [materials/resource-catalog.md](materials/resource-catalog.md) |
| `material-versions.md` | [materials/versions.md](materials/versions.md) |
| `omp-orca.md` | [research/omp-orca.md](research/omp-orca.md) |
| `ood-material-assessment.md` | [materials/ood-assessment.md](materials/ood-assessment.md) |
| `typescript-plugin-lab.md` | [my-progress/projects/typescript-plugin-lab.md](my-progress/projects/typescript-plugin-lab.md) |
| `workflow-design.md` | [research/workflow-design.md](research/workflow-design.md) |
| `teaching/COURSE-STRUCTURE-PROPOSAL.md` | Superseded September 28 by the four-stage [roadmap](ROADMAP.md); history only |
| `archive/README.md` | This page |

The six root pages were compatibility stubs headed "Moved"; their anchors match headings in the replacement documents.

## Moved in the October 27 reorganization

| Former path | Now |
|---|---|
| `CONTEXT.md` | [GLOSSARY.md](GLOSSARY.md) |
| `teaching/DECISIONS.md` | [course/DECISIONS.md](course/DECISIONS.md) |
| `PROJECT-CONTEXT.md`, `CHAT-HISTORY.md` | [my-progress/](my-progress/README.md) |
| `teaching/RESTART-DIAGNOSTIC.md`, `teaching/2026-09-*-*.md` schedule reviews | [my-progress/](my-progress/README.md) and `my-progress/schedule/` |
| `teaching/handouts/` | [my-progress/reading-room/](my-progress/README.md#reading-room) |
| `course/ideas/`, `operations/vps/`, `research/oracle-folder-retirement.md` | `my-progress/ideas/`, `my-progress/operations/` |
| `self-practice/`, `terminal-practice/` | `my-progress/work/self-practice/`, `my-progress/terminal-practice/` |
| `materials/<repo>` symlinks to `~/Self-learn` | Pinned Git submodules under [materials/sources/](materials/README.md#source-repositories) |
| `materials/refresh-2026-09-11.json`, `materials/grokking-ood-case-collision/` | `materials/provenance/` |
| `course/projects/typescript-plugin-lab.md`, `course/projects/vps-lab-roadmap.md` | [my-progress/projects/](my-progress/README.md) (personal projects) |
| Idea index in `course/IDEAS.md` | [my-progress/ideas/README.md](my-progress/ideas/README.md); the intake process stays in the course |
| Progress-owner links and owner status in course pages | [my-progress/OWNERS.md](my-progress/OWNERS.md) |
