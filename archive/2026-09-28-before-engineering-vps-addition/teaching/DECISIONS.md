# Course decision record

## Current agreement — September 28, 2026

The student confirmed all three grill-with-docs rounds and authorized the repository structure. They emphasized that milestones and organization must remain adaptable, and added renting a VPS as a small idea that needs a place in the course. Shared understanding was reached; the interview is complete for this revision.

- Destination: design, build, evaluate and operate distributed AI agent systems, including operating systems/Linux, networks/VPS, Docker/Kubernetes and model inference.
- Structure: foundations → reliable single-host systems → distributed systems → integrated capstone; the ten proposed milestones were accepted as curriculum v1, subject to deliberate future change.
- Workload: 15 hours/week total, normally 10 core/labs, 3 project and 2 exploration; one primary module and one active project. This supersedes the earlier separate learning/build lanes.
- Mastery: artifact/experiment, student explanation and unfamiliar modification/diagnosis; applied graduate-level source/research depth, pass/revise with focused reassessment.
- Authority: teacher handles materials, idea classification, equivalent exercises and routine weekly ordering; student agreement governs changed required milestones, core outcomes and agreed milestone deadlines.
- Intake: an idea can become an example, exercise, project option, elective, proposed milestone or deferred/out-of-scope idea. Capture does not promise implementation. Existing pilot/plugin/tool ideas were accepted in the proposed roles.
- Ownership: repository holds curriculum/materials/research/teaching; Obsidian keeps schedule, tasks, hours, annotations and evidence. Preserve old links, source repositories and learner work.
- Adaptability: stable milestone/idea IDs, impact proposals for major changes, dated decisions, old-to-new evidence mapping and historical snapshots. The core is protected from accidental drift, not from agreed revisions.

Current rules live in the [charter](../course/CHARTER.md), [roadmap](../ROADMAP.md), [assessment](../course/ASSESSMENT.md), [projects](../course/PROJECTS.md) and [idea intake](../course/IDEAS.md). The [accepted review proposal](COURSE-STRUCTURE-PROPOSAL.md) is historical design evidence, not another authority to maintain.

### Implementation record

Reorganized research/material/project documents into explicit homes, retaining root forwarding pages and original section destinations. Added a course-work pointer to AGENTS.md. Replaced conflicting current roadmap/context/navigation with the accepted program. Original Markdown files were preserved byte-for-byte in the [pre-change snapshot](../archive/2026-09-28-before-program-structure/README.md); its manifest records hashes.

I001 (VPS) now has a two-hour exploration brief and an optional bounded service-operation project. No rental, paid host, provider choice, model run, external publication, exercise completion or Obsidian task-state change resulted from this reorganization. Existing milestone deadlines remain unchanged. A concrete evidence-based calendar reforecast remains to be reviewed separately under the accepted authority boundary.

### Verification

Checked 366 local Markdown destinations and current section anchors across 49 non-archival current Markdown files; all resolved. Verified all 32 pre-change snapshot hashes. The historical CHAT-HISTORY bytes are unchanged; HERDR practice changed only its material-version link. Existing copied upstream whitespace was preserved. This was a document/link check, not a live Obsidian rendering or runtime test.

### Deferred choices

Provider, region, monthly spend and first VPS workload are resolved when the lab brief is ready. Later cluster/GPU topology follows its workload and prerequisites. Detailed future lessons and tool choices remain deferred until their entry evidence exists. Those deferred operational choices do not block the adopted course organization.

## Historical decisions

Earlier agreements below preserve rationale. Current charter/roadmap rules take precedence wherever scope, capacity, dates, ownership or sequence differs.

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
