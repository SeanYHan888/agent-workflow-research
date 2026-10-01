# I010 — Remote credential access for agents

Captured September 29, 2026 at the student's request: “Add this to future plan.”

## Need and placement

While away from the laptop, the student wants an agent to complete authorized sign-ins without sharing the Mac login password or password-manager master password. The immediate trigger was the prepared OVHcloud Hillsboro checkout: Apple Passwords on the Mac was locked, and the student could not approve its local unlock prompt. No sign-in or purchase was completed in that flow.

Preferred outcome to evaluate: approve a specific website login from the phone, let the remote browser sign in, and keep the website password out of the agent's conversation and logs. Separately evaluate scoped unattended access for routine API/CLI work; that grants standing access and is a different permission model from approving each login.

Disposition: deferred tool investigation and optional exercise within M4 harness authority and M5 credentials/least privilege, reusable in M7 remote workers. This adds no required milestone or deadline. 1Password is a candidate, not a selected or purchased dependency.

## Candidate routes and known limits

Official documentation checked September 29, 2026; recheck availability, subscription requirements and integration support before activation.

| Route | Potential use | Limit to test or preserve |
|---|---|---|
| [1Password item sharing](https://support.1password.com/share-items/) | Share only a selected website credential using an expiring link from the phone | Recipients can read/copy the secret. Expiration does not revoke a copied password. This does not meet the preferred outcome of keeping secrets out of agent context. |
| [Service accounts](https://www.1password.dev/service-accounts/get-started) and a dedicated automation vault | Scoped token authentication for a runner, avoiding a desktop unlock for each request | The runner can access allowed secrets. Use minimal read permissions, expiry/revocation and limited API credentials where possible. Bootstrap-token storage and preventing secret output require an explicit design; a CLI alone is not secure browser autofill. |
| [Desktop CLI integration](https://www.1password.dev/cli/app-integration) | Interactive local developer authentication | Can still require device authentication, reproducing the away-from-laptop blocker. |
| [Agentic Autofill](https://www.1password.dev/agentic-autofill) | Inject credentials into an agent-controlled browser without exposing them to the model | Documentation describes early access through Browserbase Director with desktop-app approval. Phone-only approval and compatibility with the current in-app browser are unverified. |

## Smallest useful investigation

Use at most one future **2-hour exploration slot** within the existing 15-hour weekly budget, replacing that week's other exploration. Do not activate another project or buy a subscription solely from this note.

1. Confirm whether the desired mode is phone approval per login, scoped unattended API access, or both. Check the owning Obsidian project and prerequisites before assigning work.
2. Compare existing supported tools before designing a custom credential broker. Verify subscription cost, supported browser/runtime, phone approval and initial setup needs.
3. With a disposable account and dummy secret, test from the phone while the laptop's password manager is locked. Record where approval occurs, which process receives the secret, whether the agent/logs can see it, and whether login actually succeeds.
4. Test a denied request, expired/revoked access and an unauthorized destination or vault. Keep MFA and purchase authorization separate from credential retrieval.
5. Record evidence and choose adopt, defer or reject. A successful secret read alone does not prove a working remote browser-login flow.

If implementation needs more than the exploration slot, propose a separately bounded project with a useful deliverable within 21 days and a realistic allocation from the existing 3h/week project budget. Link its owning Obsidian note only when activated; this brief is not a progress tracker.

Revisit before the first unattended workflow requiring authenticated external access, or when a supported phone-approved autofill integration becomes available. Current result: planning captured; no integration tested, software installed, secrets migrated or access granted.
