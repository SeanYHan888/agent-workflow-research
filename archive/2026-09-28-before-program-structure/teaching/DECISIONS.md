# Course decision record

## Course governance interview — September 28, 2026

The student requested a coherent course with master's-level rigor, explicit subsection boundaries, a schedule, selected materials, course projects and assessments. The teacher maintains the essential topics and defines milestones. The student can explore between milestones and request additional milestones. New ideas should be evaluated for a place in the course and their scheduling consequences made explicit while preserving the essential topics.

This records the requested teaching relationship, not a completed redesign. The existing foundation, September 28 study expansion and parallel automation pilot must be reconciled before implementing a new structure or schedule. Existing progress evidence remains authoritative in Obsidian.

The grill-with-docs interview is in progress. Folder moves, syllabus replacement and rescheduling await a shared understanding; drafting vocabulary and recording interview decisions can proceed during the interview.

### Round 1 — confirmed by the student

- **Destination:** design, build, evaluate and operate reliable distributed AI agent systems, and explain the model-serving layer they depend on. The student explicitly includes Linux, operating systems, VPS administration, computer networks, Docker/Kubernetes and model inference as important core subjects. Their placement and depth must serve this destination.
- **Capacity:** 15 focused hours/week total across study, projects, assessments and exploration. This supersedes the separate 10-hour learning and additional 3–5-hour build commitments. The expanded scope has no agreed finish date; prior foundation estimates do not describe its total workload.
- **Mastery:** each milestone requires a working artifact or experiment, an explanation in the student's own words, and an unfamiliar modification or debugging task. AI assistance is welcome in practice; assessment must reveal the student's understanding. Unmet criteria lead to targeted practice and reassessment.

### Round 2 — confirmed by the student

- **Program structure:** foundations → reliable single-host systems → distributed systems → integrated capstone. Each stage has useful intermediate outcomes and its own milestones. Near-term work gets a detailed schedule; later work remains a forecast.
- **Weekly allocation:** 10 hours core study and labs, 3 hours course-project work, 2 hours exploration. Assessments are included in these hours. Keep one primary learning module and one active project. Unused exploration time returns to core work. An exploration may replace an equivalent exercise; a larger unrelated idea waits for an appropriate slot.
- **Teacher authority:** classify ideas, select materials, substitute equivalent exercises and adjust weekly ordering within the agreed budget, explaining changes. Adding a required milestone, changing a core outcome or moving an agreed milestone deadline requires student agreement. These rules do not authorize paid infrastructure or external deployment.

### Final structure review — pending

The concrete [course structure proposal](COURSE-STRUCTURE-PROPOSAL.md) maps the agreed destination to stages, milestones, document ownership and existing material. The remaining decisions concern depth, placement of existing additions and the file migration. Once the student confirms this proposal, implement the organization without reopening settled decisions. Exact lab providers and cluster sizes remain deferred until the relevant lab requirements are known.

## Settled course — recovered September 11, 2026

Historical baseline: the September 28 Round 1 decisions above supersede this section's overall scope and weekly capacity. Preserve earlier learning evidence; a new course schedule has not yet been adopted.

Evidence: [project context](../PROJECT-CONTEXT.md), [roadmap](../ROADMAP.md) and existing Obsidian course projects, read on September 11.

- Outcomes: terminal human collaboration, GUI human collaboration, and a working team with final human review.
- Capacity: 10 focused hours/week; compact 160-hour, 16-week forecast. Reassess actual pace September 30.
- Sequence: one tool cycle → JS/Node → small TS agent → Tau/Pi and extension → GUI → one worker → Linux/two workers → team capstone.
- Teaching: small Python orientation, then one evolving TypeScript build; attempt first, teach gaps, require explanation and failure evidence.
- Materials: Boot.dev JS/TS, official Node documentation, selected Tau/Pi and learn-claude-code, YSAP, selected LFS101, selected system-design references. See the [material shelf](handouts/01%20Material%20Shelf.md).
- Existing tools first for the team. Generated agent-learning chapters and the existing mini-agent do not determine the syllabus or count as learner work.
- First assignment: read s01 `agent_loop()`, explain execution, message changes and stopping, then review before implementing the tiny dispatcher.

## Organization — explicitly selected September 11

The user requested this repository as the teacher's classroom/office and a new folder under Obsidian Notes for study materials. Created the reading room at `Notes/Coding Agent Course`.

The user selected **link the six existing source repositories** rather than moving them. `materials/` is their local shelf. New plans, teaching preparation and original handouts are saved here; student reading copies are in Obsidian. Existing project notes retain progress ownership.

These storage choices are reversible, so this record is sufficient; no architecture decision record is needed.

## Decision tree and next eligible decisions

September 11 follow-up: the user requested extracting Tau/Pi and deleting the entire generated agent-learning project. Completed after verifying the preserved repositories. YSAP and LFS101 remain selected core resources. Added an explicit tools/progress handout and optional Grokking OOD selections for foundation Sections 3 and 5, within existing hours. Existing Obsidian projects retain their task/state ownership and all completion states.

```text
Course outcomes, time and sequence [settled]
├── Resource roles [settled]
│   └── Source repository storage [settled: links]
├── Classroom / reading room / progress ownership [settled]
└── First assignment [settled]
    ├── Next teaching hint [depends on learner's answer]
    ├── Provider / first worker [depends on adapter stage and access]
    ├── GUI choice [depends on comparison trial]
    ├── Linux lab host [depends on operations lab requirements]
    └── Team tool [depends on two-worker evidence and candidate trials]
```

There is no remaining decision required to organize the classroom. Later tool choices stay open until their evidence exists. Pi/DeepSeek suitability and cross-harness delegation are hypotheses to test. The separate Matt Pocock skill-setup proposal remains outside this organization work.
