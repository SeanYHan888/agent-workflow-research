# Agent skills: five repository review

Reviewed **October 16, 2026**. This is source research for an agent-skills course addition, not installation, execution, deployment or evidence of learner mastery. Recommendations below are this course's assessment of fit.

## What these are

These repositories package reusable instructions for coding agents. A skill normally has a `SKILL.md` entry point with a name, description/trigger and procedure or reference material; some also depend on scripts, agents, templates, tools or host-specific configuration. They influence how an agent works; their presence does not prove the resulting work is correct. The collections below show both lightweight guidance and full workflow/plugin systems.

## Quick comparison

| Collection | Main purpose | Most useful here |
|---|---|---|
| Matt Pocock | Requirements, design, implementation and review discipline | Strong starting point for the agent-first Linux/TypeScript project; `writing-for-agents` is central to learning skill authoring. |
| Cursor pstack | Task playbooks, parallel work, behavioral verification and durable corrections | Study verification skills, `correct`, `benchmark-checklist` and type/domain principles first; adopt orchestration selectively. |
| HumanLayer | Research/design/implementation handoffs and recurring improvement loops | Best connection to the runner/worker/service project and designing measurable agent loops. |
| Emil Kowalski | Interaction design, UI motion and visual quality | Useful for an Obsidian plugin, task panel or dashboard; secondary for Linux/backend foundations. |
| Addy Osmani | Broad engineering lifecycle and explicit quality practices | Use context, constraints, source verification and observability as complementary checklists. |

## Scope and revision pins

Fetched each repository's recursive Git tree and every scoped `SKILL.md` at the returned commit. None of the tree responses was truncated. Reviewed all skill entry-point descriptions and headings, with deeper body inspection of representative workflows and the recommended authoring/verification/loop skills. This is a purpose and fit review, **not a line-by-line audit of every supporting file, executable script or generated adapter**, and no runtime effectiveness experiment was performed. README contents were also inspected. The inventories below include every scoped `SKILL.md`, including draft or dormant entries explicitly labeled as such.

| Repository scope | Revision | Skill files |
|---|---|---:|
| mattpocock/skills | [`49dd158d1076`](https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336) | 38 |
| cursor/plugins/pstack | [`cdb3c41c9f2f`](https://github.com/cursor/plugins/tree/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack) | 57 |
| humanlayer/skills | [`653b6411c1f7`](https://github.com/humanlayer/skills/tree/653b6411c1f70c275a18e37673b042ff99f67ceb) | 7 |
| emilkowalski/skills | [`2d228630ba14`](https://github.com/emilkowalski/skills/tree/2d228630ba1446365f614a108cb8252f1feda202) | 15 |
| addyosmani/agent-skills | [`aeac41d4d005`](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d) | 25 |

Total: **142 entry-point files**. pstack contributes **54 normal skill files plus 3 dormant Benny automation files**; its playbooks are supporting documents, not additional `SKILL.md` entries. Matt contributes 20 engineering, 7 productivity, 4 miscellaneous and 7 explicitly in-progress skills.

## Inventory: purpose of every skill

Every skill-name link below points to the exact inspected entry point. Draft and automation-only entries are separated so presence is not mistaken for a normal installable command.

### Matt Pocock — engineering workflows

**Engineering**

| Skill | Purpose |
|---|---|
| [ask-matt](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/ask-matt/SKILL.md) | Choose a suitable Matt workflow for the current problem. |
| [code-review](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/code-review/SKILL.md) | Compare a scoped change against both repository standards and its specification. |
| [codebase-design](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md) | Reason about deep modules, narrow interfaces and testable seams. |
| [diagnosing-bugs](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/diagnosing-bugs/SKILL.md) | Reproduce a failure, test hypotheses, fix its cause and verify the regression. |
| [domain-modeling](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md) | Clarify domain terms in a glossary and record consequential design decisions. |
| [grill-with-docs](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/grill-with-docs/SKILL.md) | Challenge a design while capturing shared vocabulary and decisions. |
| [implement](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement/SKILL.md) | Build a scoped specification or ticket through testing and review. |
| [implement-spec](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement-spec/SKILL.md) | Coordinate ticket dependencies and parallel implementers on an integration branch. |
| [improve-codebase-architecture](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/improve-codebase-architecture/SKILL.md) | Survey architecture and discuss selected opportunities to simplify interfaces. |
| [pr](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/pr/SKILL.md) | Write a compact PR explanation with visual structure, evidence and merge risk. |
| [prototype](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/SKILL.md) | Build a disposable experiment to answer a design or interface question. |
| [research](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/research/SKILL.md) | Delegate primary-source investigation and preserve cited findings locally. |
| [retro](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/retro/SKILL.md) | Identify improvements to the agent environment from the completed session. |
| [setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/setup-matt-pocock-skills/SKILL.md) | Configure issue tracking, triage labels and document ownership for the pack. |
| [tdd](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/tdd/SKILL.md) | Build behavior through failing tests and small implementation steps. |
| [to-spec](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-spec/SKILL.md) | Turn settled discussion into a specification in the configured tracker. |
| [to-tickets](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md) | Split a plan into independently verifiable tickets with dependencies. |
| [triage](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/triage/SKILL.md) | Process incoming issues and PRs into categorized, verified, actionable work. |
| [wayfinder](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wayfinder/SKILL.md) | Resolve large uncertain work through a map of decision tickets. |
| [wizard](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wizard/SKILL.md) | Generate an interactive shell guide for steps requiring human participation. |

**Productivity**

| Skill | Purpose |
|---|---|
| [grill-me](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grill-me/SKILL.md) | Run an intensive interview to clarify a plan or design. |
| [grilling](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grilling/SKILL.md) | Provide reusable questioning discipline for other workflows. |
| [handoff](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/handoff/SKILL.md) | Write a continuation document for another agent or session. |
| [teach](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/teach/SKILL.md) | Organize instruction across sessions in a persistent learning workspace. |
| [to-questionnaire](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/to-questionnaire/SKILL.md) | Prepare a targeted questionnaire for a decision requiring another person's input. |
| [wait-what](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/wait-what/SKILL.md) | Explain the last response again with missing context and clearer language. |
| [writing-for-agents](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL.md) | Design precise triggers, ordered procedures, references and completion criteria. |

**Miscellaneous**

| Skill | Purpose |
|---|---|
| [git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/git-guardrails-claude-code/SKILL.md) | Install Claude Code hooks that block selected dangerous Git commands. |
| [migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/migrate-to-shoehorn/SKILL.md) | Replace unsafe test-fixture assertions with shoehorn helpers. |
| [scaffold-exercises](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/scaffold-exercises/SKILL.md) | Generate a course exercise directory structure and related scaffolding. |
| [setup-pre-commit](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/misc/setup-pre-commit/SKILL.md) | Configure Husky, lint-staged, formatting, types and commit-time checks. |

**In progress — evaluate as drafts**

| Skill | Purpose |
|---|---|
| [chief-of-staff](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/chief-of-staff/SKILL.md) | Coordinate subagents toward a long-running goal in one session. |
| [claude-handoff](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/claude-handoff/SKILL.md) | Transfer ongoing work directly to a fresh background agent. |
| [loop-me](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/loop-me/SKILL.md) | Interview the user about recurring workflows they want to build. |
| [setup-ts-deep-modules](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/setup-ts-deep-modules/SKILL.md) | Configure dependency-cruiser to enforce TypeScript package boundaries. |
| [writing-beats](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-beats/SKILL.md) | Arrange raw writing material into a sequence that builds understanding. |
| [writing-fragments](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-fragments/SKILL.md) | Collect and explore raw writing material before organizing it. |
| [writing-shape](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/in-progress/writing-shape/SKILL.md) | Develop raw material into a coherent article structure. |


### pstack — rigorous agent orchestration

**Normal skills**

| Skill | Purpose |
|---|---|
| [architect](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/architect/SKILL.md) | Settle caller usage, types and module boundaries before implementation. |
| [arena](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/arena/SKILL.md) | Compare independent attempts at the same task and combine their strongest parts. |
| [automate-me](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/automate-me/SKILL.md) | Turn the user's evidenced working preferences into a personal mode skill. |
| [benchmark-checklist](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/benchmark-checklist/SKILL.md) | Check what a benchmark actually measures before claiming an improvement. |
| [blast-radius](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/blast-radius/SKILL.md) | Investigate effects beyond the diff and execute the critical safety check. |
| [bro](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/bro/SKILL.md) | Restate the previous message in plain language. |
| [correct](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/correct/SKILL.md) | Turn recurring mistakes into structural, type, lint or test constraints. |
| [create-verification-skill](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/create-verification-skill/SKILL.md) | Build a project-local recipe for driving the real app and recording evidence. |
| [figure-it-out](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/figure-it-out/SKILL.md) | Create an auditable custom playbook for complex work lacking an existing route. |
| [how](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/how/SKILL.md) | Trace subsystem structure, runtime behavior and ownership from code. |
| [in-your-own-words](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/in-your-own-words/SKILL.md) | Restate the user's intended outcome before proceeding. |
| [interrogate](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/interrogate/SKILL.md) | Use multiple model perspectives to challenge a change. |
| [ketchup](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/ketchup/SKILL.md) | Summarize progress and decisions since the user's last message. |
| [maintain-verification-skill](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/maintain-verification-skill/SKILL.md) | Check verification documentation against source and live behavior, correcting drift. |
| [make-bot-ui](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/make-bot-ui/SKILL.md) | Build a UI that wakes a bot through a webhook and can be exposed on Tailscale. |
| [no-comments](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/no-comments/SKILL.md) | Review comments and replace avoidable explanations with clearer code or constraints. |
| [poteto-help](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/poteto-help/SKILL.md) | Explain pstack and route a question to its relevant entry point. |
| [poteto-mode](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/poteto-mode/SKILL.md) | Coordinate task-specific playbooks, verification, delegates and communication. |
| [recall](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/recall/SKILL.md) | Reconstruct current working context from relevant transcripts and shared evidence. |
| [reflect](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/reflect/SKILL.md) | Extract durable session lessons and update the appropriate existing skills. |
| [setup-pstack](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/setup-pstack/SKILL.md) | Configure available models and reasoning budgets for pstack roles. |
| [sharpen](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/sharpen/SKILL.md) | Reframe a task around the real objective and a strong expert approach. |
| [show-me-your-work](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/show-me-your-work/SKILL.md) | Keep a compact decision log linking choices to evidence and results. |
| [swarm](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/swarm/SKILL.md) | Distribute independent work and consolidate the findings. |
| [tdd](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/tdd/SKILL.md) | Add a focused failing regression check when the bug has a practical test path. |
| [teach](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/teach/SKILL.md) | Combine code behavior and historical rationale into a conversational explanation. |
| [technical-writing](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/technical-writing/SKILL.md) | Apply explicit documentation structure and clear technical prose rules. |
| [typescript-best-practices](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/typescript-best-practices/SKILL.md) | Apply discriminated unions, brands, schema ownership and related TypeScript practices. |
| [unslop](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/unslop/SKILL.md) | Edit stereotyped AI prose while preserving its meaning. |
| [why](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/why/SKILL.md) | Investigate historical rationale using code history and connected evidence sources. |

**Engineering principles — separate small skills**

| Skill | Purpose |
|---|---|
| [principle-attack-the-premise](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-attack-the-premise/SKILL.md) | Test the shared assumption behind repeatedly unsuccessful fixes. |
| [principle-boundary-discipline](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-boundary-discipline/SKILL.md) | Concentrate validation at external boundaries and simplify internal logic. |
| [principle-build-the-lever](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-build-the-lever/SKILL.md) | Create a repeatable tool instead of repeating manual work. |
| [principle-encode-lessons-in-structure](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-encode-lessons-in-structure/SKILL.md) | Convert repeated guidance into enforceable code or checks. |
| [principle-exhaust-the-design-space](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-exhaust-the-design-space/SKILL.md) | Compare competing prototypes before selecting an unfamiliar design. |
| [principle-experience-first](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-experience-first/SKILL.md) | Prioritize the user's experience when deciding product tradeoffs. |
| [principle-explain-the-number](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-explain-the-number/SKILL.md) | Establish why a measured metric has its observed value. |
| [principle-fix-root-causes](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-fix-root-causes/SKILL.md) | Repair the first incorrect state rather than hiding its downstream symptoms. |
| [principle-foundational-thinking](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-foundational-thinking/SKILL.md) | Choose data structures and shared-state models before adding behavior. |
| [principle-guard-the-context-window](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-guard-the-context-window/SKILL.md) | Keep bulk investigation out of the main conversation context. |
| [principle-laziness-protocol](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-laziness-protocol/SKILL.md) | Prefer deletion and a small solution over unnecessary abstraction. |
| [principle-make-operations-idempotent](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-make-operations-idempotent/SKILL.md) | Design retryable operations to converge after partial execution. |
| [principle-migrate-callers-then-delete-legacy-apis](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Move internal callers and remove superseded interfaces together. |
| [principle-minimize-reader-load](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-minimize-reader-load/SKILL.md) | Reduce indirection and hidden state required to understand code. |
| [principle-model-the-domain](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-model-the-domain/SKILL.md) | Represent domain states explicitly instead of spreading implicit assumptions. |
| [principle-never-block-on-the-human](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-never-block-on-the-human/SKILL.md) | Proceed with reversible authorized work while preserving human direction. |
| [principle-outcome-oriented-execution](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-outcome-oriented-execution/SKILL.md) | Keep phased migrations focused on the target design. |
| [principle-prove-it-works](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-prove-it-works/SKILL.md) | Check the actual result before declaring completion. |
| [principle-redesign-from-first-principles](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-redesign-from-first-principles/SKILL.md) | Reconsider the design when accommodating a new requirement. |
| [principle-separate-before-serializing-shared-state](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md) | Remove avoidable shared writes before introducing synchronization. |
| [principle-sequence-verifiable-units](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-sequence-verifiable-units/SKILL.md) | Order work into small changes that each end in a checkable state. |
| [principle-subtract-before-you-add](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-subtract-before-you-add/SKILL.md) | Remove unnecessary complexity before expanding a system. |
| [principle-test-behavior-not-implementation](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-test-behavior-not-implementation/SKILL.md) | Test observable contracts without coupling assertions to internal structure. |
| [principle-type-system-discipline](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/principle-type-system-discipline/SKILL.md) | Use types and boundary parsing to exclude invalid states. |

**Dormant Benny automation pack — not normal slash skills**

| Skill | Purpose |
|---|---|
| [reproduce-and-fix-issues](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md) | Reproduce a triaged bug and prepare a bounded draft fix with before/after proof. |
| [setup-benny](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/automations/benny/skills/setup-benny/SKILL.md) | Configure the dormant Slack triage and reproduction automation pack. |
| [triage-issue-reports](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/automations/benny/skills/triage-issue-reports/SKILL.md) | Classify Slack bug reports and create deduplicated tracker issues when warranted. |


### HumanLayer — document-driven work and recurring loops

| Skill | Purpose |
|---|---|
| [build-iterated-agentic-loop](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/plugins/build-iterated-agentic-loop/skills/build-iterated-agentic-loop/SKILL.md) | Generate a local skill, coding-agent CI workflow, memory and PR loop. |
| [design-control-loop](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/plugins/design-control-loop/skills/design-control-loop/SKILL.md) | Design a measurable sensor/controller/actuator loop and its implementation. |
| [improve-claude-md](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/plugins/improve-claude-md/skills/improve-claude-md/SKILL.md) | Restructure CLAUDE.md around conditional instructions and a project map. |
| [narrow-react-prop-types](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/plugins/narrow-react-prop-types/skills/narrow-react-prop-types/SKILL.md) | Narrow React props to states actually used in production paths. |
| [rpi](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/plugins/rpi/skills/rpi/SKILL.md) | Move through research, design documents and implementation with explicit phase handoffs. |
| [show-me](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/plugins/show-me/skills/show-me/SKILL.md) | Explain a topic using compact diagrams, code sketches or focused HTML. |
| [visual-pr](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/plugins/visual-pr/skills/visual-pr/SKILL.md) | Create or update a PR with a visual outline of the change. |


### Emil Kowalski — UI design and motion

| Skill | Purpose |
|---|---|
| [animate](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/animate/SKILL.md) | Implement motion by deciding its purpose, properties, timing and interruption behavior. |
| [animate-expo](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/animate-expo/SKILL.md) | Build React Native/Expo gestures and motion with mobile performance considerations. |
| [animation-performance](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/animation-performance/SKILL.md) | Diagnose frame drops and improve animation execution and rendering costs. |
| [animation-vocabulary](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/animation-vocabulary/SKILL.md) | Translate informal motion descriptions into precise animation terms. |
| [apple-design](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/apple-design/SKILL.md) | Apply Apple-inspired interaction, typography and motion principles to web UI. |
| [ask-sonner](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/ask-sonner/SKILL.md) | Configure and troubleshoot the Sonner React toast library. |
| [break-ui](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/break-ui/SKILL.md) | Stress UI layouts with extreme, missing and multilingual data. |
| [emil-design-eng](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/emil-design-eng/SKILL.md) | Apply the collection's central design-engineering and animation guidance. |
| [find-animation-opportunities](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/find-animation-opportunities/SKILL.md) | Identify useful motion opportunities and explain what should remain static. |
| [improve-animations](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/improve-animations/SKILL.md) | Produce a prioritized motion audit and implementation plans without editing product code. |
| [mobile-native](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/mobile-native/SKILL.md) | Fix mobile-web interaction, viewport, safe-area and touch details. |
| [pick-ui-library](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/pick-ui-library/SKILL.md) | Select from an opinionated set of frontend libraries for a concrete need. |
| [prototype](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/prototype/SKILL.md) | Build distinct UI alternatives behind a live visual switcher. |
| [review-animations](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/review-animations/SKILL.md) | Critique existing motion against explicit interaction and animation standards. |
| [write-swift](https://github.com/emilkowalski/skills/blob/2d228630ba1446365f614a108cb8252f1feda202/skills/write-swift/SKILL.md) | Apply modern Swift modeling, concurrency, performance and testing practices. |


### Addy Osmani — engineering lifecycle

| Skill | Purpose |
|---|---|
| [api-and-interface-design](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/api-and-interface-design/SKILL.md) | Design stable public APIs and module contracts. |
| [browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/browser-testing-with-devtools/SKILL.md) | Use Chrome DevTools MCP to inspect and test a running web app. |
| [ci-cd-and-automation](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/ci-cd-and-automation/SKILL.md) | Build quality gates, CI workflows and deployment automation. |
| [code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/code-review-and-quality/SKILL.md) | Review correctness, security, performance, maintainability and testing. |
| [code-simplification](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/code-simplification/SKILL.md) | Refactor for clarity while preserving behavior. |
| [constraint-driven-development](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/constraint-driven-development/SKILL.md) | Define measurable quality constraints and detect weakened checks. |
| [context-engineering](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/context-engineering/SKILL.md) | Organize rules, relevant files and context for reliable agent work. |
| [debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/debugging-and-error-recovery/SKILL.md) | Diagnose failures systematically and verify safe recovery. |
| [deprecation-and-migration](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/deprecation-and-migration/SKILL.md) | Plan and execute retirement or migration of existing interfaces and systems. |
| [documentation-and-adrs](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/documentation-and-adrs/SKILL.md) | Maintain architecture rationale, public documentation and change records. |
| [doubt-driven-development](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/doubt-driven-development/SKILL.md) | Challenge consequential decisions through fresh-context adversarial review. |
| [frontend-ui-engineering](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/frontend-ui-engineering/SKILL.md) | Build accessible, responsive interfaces with explicit state and component patterns. |
| [git-workflow-and-versioning](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/git-workflow-and-versioning/SKILL.md) | Structure branches, commits, worktrees, recovery and releases. |
| [idea-refine](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/idea-refine/SKILL.md) | Explore alternatives and converge on a concrete proposal. |
| [incremental-implementation](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/incremental-implementation/SKILL.md) | Deliver thin, verifiable slices with safe rollout and rollback considerations. |
| [interview-me](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/interview-me/SKILL.md) | Clarify underlying intent through focused questions. |
| [observability-and-instrumentation](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/observability-and-instrumentation/SKILL.md) | Add useful logs, metrics, traces and operational evidence. |
| [performance-optimization](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/performance-optimization/SKILL.md) | Measure bottlenecks before optimizing frontend, backend or database behavior. |
| [planning-and-task-breakdown](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/planning-and-task-breakdown/SKILL.md) | Turn requirements into ordered tasks with acceptance checks. |
| [security-and-hardening](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/security-and-hardening/SKILL.md) | Threat-model external inputs and apply security controls. |
| [shipping-and-launch](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/shipping-and-launch/SKILL.md) | Prepare rollout, monitoring and rollback before release. |
| [source-driven-development](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/source-driven-development/SKILL.md) | Verify framework-specific choices against version-appropriate primary documentation. |
| [spec-driven-development](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/spec-driven-development/SKILL.md) | Define requirements, boundaries and success criteria before substantial changes. |
| [test-driven-development](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/test-driven-development/SKILL.md) | Develop behavior through red/green/refactor and regression evidence. |
| [using-agent-skills](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/using-agent-skills/SKILL.md) | Discover suitable skills and coordinate their place in the engineering lifecycle. |

## What I would prioritize for you

These are recommendations based on the user's course and projects, not measured rankings of skill effectiveness.

1. **Start with Matt's `writing-for-agents`, `codebase-design`, `diagnosing-bugs` and `tdd`.** They connect skill authoring to the existing TypeScript runner, agent and engineering curriculum. Use questioning skills when a decision needs clarification; a lengthy interview need not precede every small change.
2. **Study pstack's `create-verification-skill`, `maintain-verification-skill` and `correct`.** These connect directly to reliable agent work: make verification repeatable, keep it current, and turn recurring errors into checks. `benchmark-checklist` is particularly relevant to research and inference measurements. Study the small pieces before adopting the full `poteto-mode` orchestration system.
3. **Use HumanLayer's `rpi` for substantial changes and `design-control-loop` as an agent-system case study.** RPI makes research/design/implementation handoffs explicit; the control-loop skill connects observations, decisions and actions. `build-iterated-agentic-loop` becomes useful when a bounded local workflow already has evaluation evidence; scheduled CI execution is a separate deployment choice.
4. **Select Addy's `context-engineering`, `constraint-driven-development`, `source-driven-development` and `observability-and-instrumentation`.** These help control context, define observable acceptance, verify API assumptions and diagnose worker/service behavior. They complement existing engineering skills; they do not all need to run on every task.
5. **Use Emil's `break-ui`, `emil-design-eng` and `review-animations` when working on the Daily Task Panel or another interface.** Extreme/multilingual input testing is immediately relevant to a mixed-language Obsidian UI. Motion and mobile-specific skills become useful when that surface exists; they are lower priority for the current Linux/backend foundations.

## Portability, overlap and adoption limits

- **A format is not a runtime.** The [Agent Skills specification](https://agentskills.io/specification) defines metadata and packaging. Tool availability, invocation, permissions and script execution depend on the host. Review the actual references and scripts before adopting a skill; this survey does not certify them.
- **pstack is a broader plugin workflow.** Its [README](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/README.md) identifies custom subagents, configurable model roles and dependencies on Cursor's built-in skill creation plus `cursor-team-kit` tools such as `control-cli`, `control-ui` and `deslop`. Copying a `SKILL.md` into another host does not recreate those dependencies. Benny is dormant and Cursor-automation-specific.
- **HumanLayer has host details.** Its [README](https://github.com/humanlayer/skills/blob/653b6411c1f70c275a18e37673b042ff99f67ceb/README.md) documents Codex invocation and writable artifact-directory considerations for RPI. In that workflow, “TDD” means a technical design document; in the testing skills it means test-driven development.
- **Browser assumptions need adaptation.** Addy's [browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/browser-testing-with-devtools/SKILL.md) targets Chrome DevTools MCP. This project's default is the in-app browser, so its procedure cannot be assumed to work unchanged here.
- **Names can collide.** Matt and Emil both have `prototype`; Matt and pstack both have `tdd` and `teach`. Specify repository and revision when comparing or installing. Existing local Matt-style skills overlap strongly, but a matching name does not establish version or supporting-file equality.
- **Teaching workflows do not determine course assessment.** pstack's [teach](https://github.com/cursor/plugins/blob/cdb3c41c9f2f6d41f050e3dc25e15e325493d499/pstack/skills/teach/SKILL.md) favors conversational explanation and explicitly avoids quizzes. The course still requires learner attempts, explanations and unfamiliar-change evidence under its charter. Use source ideas selectively rather than replacing the agreed teaching contract.

No skills were installed, updated or executed as part of this review. No script audit, runtime comparison or effectiveness benchmark was performed. Recommended adoption begins with one workflow and a baseline comparison.

## Course integration

The requested addition is [M18 — Agent Skills](../course/modules/agent-skills.md): selection/anatomy, authoring, evaluation and maintenance, estimated at 12–18 directed hours. One learner-authored workflow for the existing runner supplies the practical thread. The collections above are case studies, not mandatory reading or installation of all 142 entries. Scheduling and progress remain with the existing Obsidian owners.
