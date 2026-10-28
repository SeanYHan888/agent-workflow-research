# M19 — Model Context Protocol: connect, expose and secure agent tools

Added October 17, 2026 at the student's request: “is mcp covered in this course … add a course for that.” MCP previously appeared only as optional Claude Academy selections (A6 chapter, A7/A8) and as a one-line distinction in M18 AS1. This required, bounded course teaches MCP through one learner-built server for the existing runner, connected to real harnesses, not completion of every protocol feature.

**Why now.** MCP has become a common integration boundary for coding agents. Pi, previously the course's main example of a harness that refused MCP, shipped built-in MCP with Codemode in 0.99/1.0 (September 29–October 1, 2026). Its tools are reached through a sandboxed JavaScript composition tool rather than loaded eagerly into every request ([Earendil: “You said no MCP”](https://earendil.com/posts/you-said-no-mcp/), [pi.dev](https://pi.dev/)). The [2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28) removed the session handshake in favor of stateless, self-describing requests. Both changes are fresh; verify current behavior at lesson preparation instead of trusting this summary.

## Useful result

Let any MCP host inspect, and in a gated way control, jobs in the learner's own runner. The learner builds one small MCP server that exposes runner job status/logs as read-only context and a narrow set of tools (for example, list jobs, read a job's log tail, request cancellation). Use local fixtures first; connect to a remote node over SSH only after M5 readiness. The deliverable is the versioned server, a recorded protocol trace, a two-host comparison and a short boundary report.

**Observable acceptance:** from two different hosts (Pi 1.0 and one other), an agent answers a held-out question about a fixture job using only the server, a malformed tool call returns a validated error rather than a crash, and an unauthorized or out-of-scope request (another workspace, a destructive action without approval) is refused by the server or host, not merely discouraged by a description. The learner explains which process executed each action.

## Placement and prerequisites

- MC1 needs M1 tool-cycle orientation and M2 processes/stdin-stdout/JSON. It can run once the JS/Node runner exists; it does not block the JS/Node restart.
- MC2 needs M3 tool contracts and runtime validation; it extends the same runner rather than starting a new agent.
- MC3 belongs with M4 harness study: Pi is already on the M4 source route. Compare with M18 skill/CLI evidence when it exists.
- MC4's local experiments follow MC2; remote HTTP transport, OAuth and SSH-tunnelled use need M5 N1–N3/S1 network and access-boundary checkpoints.
- M19 is a graduation requirement and contributes to M10. Full M19 is not an entry gate to M3, M4 or early Linux work.

## Course sequence

| Block | Learner build or investigation | Evidence | Hours |
|---|---|---|---:|
| MC1 — Trace the protocol | Run a reference server under the MCP Inspector or a raw stdio client. Predict, then capture, the JSON-RPC for discovery, `tools/list` and `tools/call`, one error and one cancellation. Identify host, client and server; contrast a model tool call (M1) with an MCP request; note what moved from the old `initialize` handshake into per-request `_meta`. | Annotated trace; a diagram of who executes what; one prediction that was wrong and why. | 2–3 |
| MC2 — Build a narrow server | Learner-authored TypeScript stdio server over the runner: one resource (job status/log), two or three tools with JSON Schema inputs, tool errors versus protocol errors, progress or cancellation for a slow call. Test with fixtures and the Inspector before any agent. | Server source, tests for normal, malformed and missing-job cases, version pin of the SDK and spec revision. | 5–7 |
| MC3 — Connect and compare hosts | Configure the same server in Pi (built-in MCP/Codemode) and one other host (Claude Code or Codex). Keep model, task and fixtures fixed. Compare eager versus deferred/Codemode tool loading, number of calls, context or token use where exposed, failures and recovery. Compare against the equivalent CLI or M18 skill: when does MCP add value? | Per-host traces, a small results table and a defended recommendation, including “a CLI is enough” if the evidence says so. | 3–4 |
| MC4 — Secure the boundary | Treat tool descriptions and returned data as untrusted. Test a fixture whose log content asks for more authority, a path outside the allowed root, a destructive tool without approval, a stale or revoked credential (environment for stdio; OAuth only with remote HTTP), and a protocol-version mismatch. Decide what the server enforces, what the host enforces and what remains unprotected. | Denied-operation evidence, threat notes and one unseen attack or change defended by the learner. | 3–4 |
| **Total** | Includes reading, attempts, feedback and assessment. | No duplicated M1 tool-cycle, M3 validation or M18 evaluation instruction. | **13–18** |

Tasks, MCP Apps, sampling and Skills-over-MCP are optional depth: introduce one only when the runner needs it (for example, Tasks for a long-running job). Building a general MCP gateway, registry or marketplace is out of scope.

## Connection to the distribution

A node running the agent-first distribution can expose its job state and controls through the M19 server. Because stdio is a supported transport, `ssh node <server>` gives a remote MCP connection that reuses SSH host identity and access control rather than opening a new network port. MC4 decides whether that, an HTTP transport with authorization, or no MCP surface at all is the right release choice; M10 records the decision with evidence. The server must stay within the lightweight resource budget measured in M10.

## First session brief — ready after owner review

- **Deliverable:** an annotated stdio trace of one `tools/list` and one `tools/call` against a reference server, plus a who-executes-what diagram.
- **Acceptance check:** the learner points to the request that discovered tools, the one that executed a tool, and the process that ran it, and explains how this differs from the M1 tool cycle.
- **Learner's next action:** before running anything, predict the messages a host sends to list and call one tool, and write the prediction down.
- **Timebox:** 60–90 minutes within MC1; most time goes to running the Inspector or a raw client, comparing with the prediction and explaining differences. Teacher gives hints and the spec section to read when blocked; no server is written for the learner.
- **Close:** observed trace, the learner's explanation and one next question for MC2. Record help used.

## Capacity, ownership and activation

This adds **13–18 directed hours** under the 15h/week charter cap. It does not add weekly hours or move existing deadlines. The A7/A8 Academy courses become M19 materials; their hours are counted here, and the MCP chapter of the A6 API course counts once where it overlaps with MC1. No Obsidian owner exists yet: create or select one at activation through the vault's project workflow, check current capacity in the live overview, and identify displaced work then.

Use at most 6–9 project hours per execution slice, with a useful result within 21 days at the actual allocation. MC2 is the natural first project slice; MC3/MC4 can form a second. No project, date, installation, remote deployment, credential or completion is created by this brief.

## Assessment

Use the [shared rubric](../ASSESSMENT.md). Require MC1–MC4 evidence: a learner-explained protocol trace, a learner-authored and tested server, a fixed-condition two-host comparison and enforced-boundary experiments. Reuse M1 tool-cycle, M3 validation, M4 Pi trace and M18 evaluation evidence for the criteria they already demonstrate. A configured third-party server or a working demo alone does not establish mastery. A well-supported conclusion that MCP is not worth it for a given workflow is acceptable.

## Primary references

Checked October 17, 2026. Recheck versions at lesson preparation.

- [MCP specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28): architecture, [base protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic) (JSON-RPC, statelessness, `_meta`, authorization), server and client features, extensions. The [TypeScript schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2026-07-28/schema.ts) is authoritative.
- Official MCP TypeScript SDK and MCP Inspector: pin the versions used in MC2.
- [Earendil, “You said no MCP”](https://earendil.com/posts/you-said-no-mcp/), September 29, 2026, and [pi.dev](https://pi.dev/): Pi's reversal, Codemode and deferred tools. Earlier, [Mario Zechner's November 2025 post](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) argued against MCP; reading both is the MC3 design debate.
- [Claude Academy: Introduction to MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol) and [Advanced topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics) (A7/A8): supporting lessons. Check that their examples match the current spec revision; earlier revisions used an `initialize` session.
