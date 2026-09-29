# How GitHub-triggered Claude development works

Research date: 2026-09-24. Read-only investigation; no app installed, credentials inspected, workflow enabled, issue comment posted, or job launched.

## What the user is seeing

There are two distinct entry points. **Claude Tag** is an organization-level Slack integration for Team and Enterprise plans. **Claude Code GitHub Actions** runs Claude Code from repository workflows in response to GitHub events. A GitHub `@claude` mention or a label named `claude` is not itself the Claude Tag product. [Claude Tag documentation](https://code.claude.com/docs/en/claude-tag)

The change is where a developer submits work and observes results. The coding engine can still be Claude Code, executed remotely rather than in a developer's interactive terminal. The GitHub Action is built on the Claude Agent SDK. [GitHub Actions overview](https://code.claude.com/docs/en/github-actions)

## Verified trigger and execution behavior

```text
Issue/PR event
  → workflow event filter
  → actor authorization + trigger check
  → GitHub Actions runner and repository checkout
  → Claude reads context and repository instructions
  → edits + permitted checks + commits
  → result comment and branch / PR follow-up
```

The shipped mention example listens for comments, issue opening/assignment, and PR reviews. It uses an Ubuntu runner, checks out the repository, and invokes `anthropics/claude-code-action@v1`. Build/test commands are illustrated as explicitly allowed tools; a mention does not magically configure a project's dependencies or test environment. [Official example workflow](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml)

The trigger implementation supports:

- A configured phrase, normally `@claude`, in supported issue/PR text or comments.
- An issue assignment matching `assignee_trigger`.
- An **issue** `labeled` event matching `label_trigger`.
- A supplied `prompt`, which bypasses mention detection for automation workflows.

The workflow must first subscribe to the event and allow it through its own conditions. Adding `label_trigger` alone to the shipped mention-only example is insufficient: that example does not subscribe to `issues: labeled`. [Trigger implementation](https://github.com/anthropics/claude-code-action/blob/main/src/github/validation/trigger.ts), [official example](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml)

## What “done automatically” actually means

For the default mention workflow, an issue creates a new working branch; an open PR receives commits on its existing branch. Progress and results update one comment. The FAQ says new changes normally finish with a prefilled **Create a PR** link, not an automatically opened PR. Reading CI results requires the corresponding Actions access. [Official FAQ](https://github.com/anthropics/claude-code-action/blob/main/docs/faq.md)

The source assembles issue/PR text, comments, changed-file context and repository instructions. Its default prompt directs the agent to plan relevant setup, lint and tests, report missing capabilities, and push its work before claiming completion. It forbids approval and merging; it does not constitute an independent proof that the implementation meets the product requirement. [Prompt implementation](https://github.com/anthropics/claude-code-action/blob/main/src/create-prompt/index.ts)

**Inference:** “issue → implementation → tests → independent review → repairs → draft PR” is a workflow we can assemble around this action. Automatic draft creation, bounded retry policy, required checks, review handling, and escalation criteria must be deliberately configured. Automatic merge or deployment is not a default guarantee.

## Access, accounts and cost

Setup requires repository admin access, a GitHub App installation, workflow files and authentication. Direct authentication supports an API key or subscription OAuth token; the latter supports Pro, Max, Team and Enterprise. API authentication incurs API usage; OAuth uses subscription usage. GitHub Actions runner usage is separate. The documentation recommends maximum turns, workflow timeouts and concurrency limits. [Setup and costs](https://code.claude.com/docs/en/github-actions)

By default, actors need repository write access and bots are rejected unless allowed. The action uses a short-lived token scoped to its repository. Its security documentation cautions against running untrusted checked-out code with privileged workflow secrets. Tool permissions and GitHub permissions are separate controls. [Action security](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)

Documentation caveat: the FAQ's claim that the official app lacks workflow-write permission conflicts with the current product docs, which list that permission. Do not use the FAQ as the current app-install permission inventory; inspect the installation screen and current docs before enabling it. [Current app permissions](https://code.claude.com/docs/en/github-actions#github-app-permissions)

## Proposed Listen Phirst pilot

These are recommendations using the existing pilot brief, not verified installed behavior in that repository:

1. Finish the field-scope decision for issue #23. A trigger cannot resolve which patient information the product ought to expose.
2. Approve one backend slice from #25, then its matching UI slice from #27, using the existing patient session and synthetic data.
3. Define an issue template containing acceptance checks, permitted scope, reproducible checks and stop conditions.
4. Use one trusted trigger, one bounded run and explicit branch/base settings. Preserve `sean/<slug>` and draft PR target `test`; the action exposes `base_branch` and `branch_prefix` inputs. [Configuration reference](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md)
5. Implement automatic draft-PR creation and verification as explicit workflow steps. Keep patient-data/access decisions and merge/deployment with the human initially.
6. Measure actual intervention count, passed checks, unresolved review findings and run cost before building a custom controller.

This can test the autonomous-development idea using GitHub as the initial job interface. It does not require finishing the Linux course or implementing Redis/RQ first.
