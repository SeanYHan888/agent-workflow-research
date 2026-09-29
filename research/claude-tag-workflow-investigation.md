# How Claude Tag turns a request into development work

Role: dated research/proposal, not current scheduling authority. Consult the [research index](README.md), [project catalog](../course/PROJECTS.md) and [charter](../course/CHARTER.md) before adopting or executing a route. Preserve historical findings; recheck tool/service facts at use.

Investigated September 24, 2026. Primary-source documentation review, not a configured integration or a reliability test. The user asked to investigate existing automation before implementing the proposed pipeline.

## What the announcement establishes

The June 23 announcement describes a Slack product: users mention `@Claude`, delegate work and receive results asynchronously. Anthropic reports that its internal version creates 65% of its product team's code. That is an internal adoption claim, not a measurement that 65% of engineering work needs no human involvement. The article does not establish that developers universally stopped using Claude Code. [Announcement](https://www.anthropic.com/news/introducing-claude-tag)

## The execution engine and interface

Claude Tag uses the same engine as Claude Code and the cloud sandbox infrastructure used by Claude Code on the web. Naming an authorized repository causes it to clone that repository. Checked-in `CLAUDE.md`, rules and skills load; personal machine configuration does not. Repository hooks do not run in Tag, and MCP access comes from admin-managed connections rather than the local MCP configuration. Routine actions use auto-mode permission checking and administrator allow rules. [Guide for Claude Code users](https://claude.com/docs/claude-tag/concepts/for-claude-code-users)

This explains the apparent shift away from a terminal: the human-facing session moves into Slack, while the coding engine runs remotely.

## Lifecycle

```text
Slack request or configured routine
    ↓
Thread session + channel access
    ↓
Cloud sandbox + authorized repository
    ↓
Investigate → change code → run checks → inspect results
    ↓
Draft PR / report + reply in Slack
    ↓
Optional PR subscription → CI/review feedback → follow-up work
    ↓
Human decision or acceptance at the defined boundary
```

The session tracks its work in a checklist. Separate threads have separate working sessions, and teammates can steer an active thread. Session context and channel memory can persist after an idle sandbox is discarded; files that exist only inside that sandbox do not. Save deliverables to durable systems such as GitHub. The diagram combines documented lifecycle and coding recipes; it is not a claim about unpublished scheduling internals. [Session lifecycle](https://claude.com/docs/claude-tag/concepts/how-it-works)

## What makes automatic completion possible

The bug-fix recipe explicitly defines a repository, task and finish condition, then requests a draft PR. Claude can reproduce a reported failure, make a fix and return a result or diagnosis. Naming a checkable outcome, rather than merely asking it to “finish the issue,” gives the session a target to verify. Access to GitHub is a prerequisite. [Bug-fix workflow](https://claude.com/docs/claude-tag/users/use-cases/fix-bugs)

The GitHub recipe can additionally subscribe to the resulting PR, act on CI failures and review comments, and push follow-ups. Human merge policy must be enforced through repository protection rules; a sentence asking the agent not to merge is guidance, not an access control. [GitHub workflow](https://claude.com/docs/claude-tag/users/use-cases/work-with-github)

Operationally, fewer interruptions come from preparation: a useful task brief, runnable environment, repository conventions, enough scoped access, explicit verification and a place to preserve results. This is an engineering inference from the documented workflow, not a guarantee every task will succeed.

## Humans still appear in Anthropic's own example

Anthropic's August CI incident-response account describes runbooks, investigation skills, saved incident lessons and monitoring connections. Claude investigates and proposes or implements fixes; humans can steer. The account says PRs have named human owners and changes still require merge approval and the normal CI gates. It also describes a separate agent for controlled feature-flag rollout. That deployment arrangement should not be assumed to be the default for every Tag installation. [Anthropic's on-call account](https://claude.com/blog/ai-ci-cd-on-call)

## Availability and access

Current docs list Tag on first-party Claude Team and Enterprise plans, not individual Free/Pro/Max plans. An organization Owner connects Slack, grants repositories/tools and configures spending. Channel/thread work is usage-billed from the organization balance. A personal subscription alone does not establish access. We have not checked the user's organization eligibility or installed Tag. [Overview and setup](https://claude.com/docs/claude-tag/overview)

Channel access belongs to the configured agent identity. Credentials can be attached at the network boundary and outbound destinations restricted. This is why organizational setup matters before a teammate can simply mention the agent. [Agent identity](https://claude.com/blog/agent-identity-access-model)

## Slack Tag versus a GitHub issue mention or label

Claude Tag is the Slack entry point. Claude Code GitHub Actions is a separate route, using GitHub events and an Actions runner. A mention or a chosen issue label can serve as a trigger only after the matching workflow has been configured. See the companion [GitHub automation investigation](claude-github-automation-research.md) for verified triggers, default branch/PR behavior and authentication.

Do not assume an issue label is a universal command, that every trigger automatically creates a PR, or that a coding result automatically gets merged.

## Implication for our dashboard plan

Investigate the existing managed routes before implementing a custom controller. The original Node runner is a candidate, not a prerequisite for useful autonomous work. Choose according to available organizational access and the desired work surface:

- Slack Tag fits shared discussion, coding and connected research if the organization can provision it.
- A GitHub workflow is a natural candidate for a bounded issue-to-code pilot already tracked in GitHub.
- The local runner remains useful if those routes fail an actual requirement or for deliberate implementation learning.

For Listen Phirst, retain patient-first and the existing session. The first delegated job can investigate #23 and produce an evidenced patient-field proposal; it cannot infer the unresolved product decision from the fact that it was tagged. Once resolved, scope one #25 backend slice and matching #27 UI slice, use synthetic fixtures, preserve the repository's `sean/` branch convention and `test` PR target, and distinguish local checks from remote CI evidence. These are the previously verified pilot constraints, not capabilities already tested with Tag.

An evaluation should demonstrate repository access, dependency setup, one complete task, CI feedback handling and the human decision path before adopting any route. No permissions, subscriptions, workflows or cloud state were changed by this investigation.
