# Course history

Earlier plans, migration snapshots and compatibility pages were removed on October 27, 2026 when the repository became a shareable course. On the same day the published Git history was rewritten to remove the learner's personal material, so **these snapshots are not in this repository's history**. The learner keeps a full pre-rewrite backup privately. They are historical records: their dates, schedules and links describe the course at that time, not current requirements.

The [changelog](course/CHANGELOG.md) summarizes each curriculum change; this page only records what the old snapshots were and where things moved.

## Archive snapshots

Each snapshot preserved the affected files immediately before a curriculum change, usually with a `manifest.json` of SHA-256 hashes. They are listed here for provenance only.

### 2026-09-10-before-compact-schedule

Plan before the compact 160-hour/16-week schedule; six terminal-agent project notes. 14 files (formerly `archive/2026-09-10-before-compact-schedule/`).

### 2026-09-10-before-course-redesign

Plan and resource research before the September 10 redesign retired the generated agent-learning chapters. 3 files (formerly `archive/2026-09-10-before-course-redesign/`).

### 2026-09-10-project-split

Task migration map from splitting the original terminal project. 2 files (formerly `archive/2026-09-10-project-split/`).

### 2026-09-10-three-workflows

The nine original Obsidian project notes and three course documents for the terminal, GUI and team workflows. 14 files (formerly `archive/2026-09-10-three-workflows/`).

### 2026-09-28-before-brokers-vps-migration

Course files before RabbitMQ/Kafka were added to M7 and VPS operations moved out of the course. 13 files (formerly `archive/2026-09-28-before-brokers-vps-migration/`).

### 2026-09-28-before-engineering-vps-addition

Course files before M11 engineering practice and the VPS idea were added. 15 files (formerly `archive/2026-09-28-before-engineering-vps-addition/`).

### 2026-09-28-before-program-structure

Original documents and migration map before the four-stage program reorganization, including the first 160-hour foundation roadmap. 46 files (formerly `archive/2026-09-28-before-program-structure/`).

### 2026-09-28-before-university-course-integration

Course files before selected MIT 6.5840 and Stanford CS329Z material was embedded. 12 files (formerly `archive/2026-09-28-before-university-course-integration/`).

### 2026-09-28-course-cleanup

September 28 audit, removed navigation leftovers, a retired terminal setup script and pre-edit vault snapshots. 30 files (formerly `archive/2026-09-28-course-cleanup/`).

### 2026-09-30-before-core-foundations

Curriculum v1.4 before M13–M15 (computer organization, algorithms, discrete mathematics). 35 files (formerly `archive/2026-09-30-before-core-foundations/`).

### 2026-09-30-before-programming-paradigms

Curriculum v1.5 before M16 programming paradigms and design. 34 files (formerly `archive/2026-09-30-before-programming-paradigms/`).

### 2026-09-30-before-relocation-reschedule

All dated project notes before a schedule postponement. 34 files (formerly `archive/2026-09-30-before-relocation-reschedule/`).

### 2026-09-30-before-systems-foundations

Curriculum before M12 Rust/compiler construction and the M5/M7 depth changes. 37 files (formerly `archive/2026-09-30-before-systems-foundations/`).

### 2026-10-04-before-agentic-linux

Curriculum v1.6 before M17 T3 Code/Omarchy Quattro and the distribution capstone. 27 files (formerly `archive/2026-10-04-before-agentic-linux/`).

### 2026-10-06-before-project-first

Course files before project-first teaching was adopted. 27 files (formerly `archive/2026-10-06-before-project-first/`).

### 2026-10-16-before-agent-skills

Curriculum v1.8 before M18 Agent Skills. 14 files (formerly `archive/2026-10-16-before-agent-skills/`).

### 2026-10-17-before-mcp

Curriculum v1.9 before M19 Model Context Protocol. 16 files (formerly `archive/2026-10-17-before-mcp/`).

The Oracle project source (`archive/2026-09-28-oracle-project-source/`) was personal operational evidence; it moved to the learner's gitignored `private/` folder.

<a id="removed-documents"></a>
## Removed documents

| Former path | Replacement |
|---|---|
| `learning-resources-research.md` | [materials/resource-catalog.md](materials/resource-catalog.md) |
| `material-versions.md` | [materials/versions.md](materials/versions.md) |
| `omp-orca.md` | [research/omp-orca.md](research/omp-orca.md) |
| `ood-material-assessment.md` | [materials/ood-assessment.md](materials/ood-assessment.md) |
| `typescript-plugin-lab.md` | Personal project; moved to `private/` |
| `workflow-design.md` | [research/workflow-design.md](research/workflow-design.md) |
| `teaching/COURSE-STRUCTURE-PROPOSAL.md` | Superseded September 28 by the four-stage [roadmap](ROADMAP.md); history only |
| `archive/README.md` | This page |

The six root pages were compatibility stubs headed "Moved"; their anchors match headings in the replacement documents.

## Moved in the October 27 reorganization

| Former path | Now |
|---|---|
| `CONTEXT.md` | [GLOSSARY.md](GLOSSARY.md) |
| `teaching/DECISIONS.md` | Learner agreements in `private/`; version-level changes in [course/CHANGELOG.md](course/CHANGELOG.md) |
| `materials/<repo>` symlinks to `~/Self-learn` | Pinned Git submodules under [materials/sources/](materials/README.md#source-repositories) |
| `materials/refresh-2026-09-11.json`, `materials/grokking-ood-case-collision/` | `materials/provenance/` |
| Personal context, chat history, schedule reviews, restart diagnostic, reading-room handouts, ideas, personal projects, VPS operations, practice work, progress-owner links | The learner's gitignored `private/` folder; not published |
| One external-project pilot note under `research/` | Removed; the workload was withdrawn |
