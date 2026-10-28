# Material versions

## Pi updated to v1.4.0 — October 27, 2026

At the student's request Pi moved from `71dca871bc80` (coding-agent 0.85.1, September 11) to the **v1.4.0** release tag, `4a080252f06c` (October 22), because M19 needs Pi's built-in MCP and Codemode (first shipped in 0.99/1.0). The pin is the release tag rather than main's head so lessons cite a published version.

Rechecked against v1.4.0: M3's Pi contract, validation and loop line ranges were updated in [typed-agent](../course/modules/typed-agent.md); every Pi file the M4 guide links still exists except `packages/server`, which v1.4.0 removed with the other experimental server/client packages, so [agent-harnesses](../course/modules/agent-harnesses.md) now uses RPC mode as the worker interface; [M19](../course/modules/mcp.md) now links Pi's local MCP docs, extension, client and conformance harness. The September 11 notes below describe the earlier revision. `~/Self-learn/pi` was not updated.

## Pinned submodules — October 27, 2026

The seven Mac-only shortcuts into `~/Self-learn` were replaced by Git submodules under [sources/](README.md#source-repositories), so a fresh clone gets the same files. Each was pinned to the commit verified on September 11 (unchanged since): tau `55df51608b8b`, pi `71dca871bc80`, learn-claude-code `0dcafa2ae053`, You Don't Know JS `044120ef5556`, System Design Primer `ae9bbd7b02d9`, System Design 101 `b28380a4710c`, Grokking OOD `ba7927f641f2`. The `~/Self-learn` checkouts were not modified.

Repositories the course already cited at a fixed commit were added at that commit: nanocode `b009d3dbedf1`, mini-swe-agent `04d809ceab9d`, Claude Code public repository `c017428c8c27`, the five M18 skill repositories, Codex `e16b631d08cd`, Cua `1cb7b6fb2415`, YSAP Bash course `0fb288afb1a3` (September 10 check) and nanochat `d5759400f967`. Repositories the course linked without a pin were pinned to their default-branch head on October 27 (T3 Code, MCP specification/TypeScript SDK/Inspector, nano-vllm, Crafting Interpreters, OpenCode, vLLM, FlashAttention, llama.cpp, MLX LM, SGLang); Omarchy was pinned to the `v4.0.0` release the M17 map cites. Those new pins establish reproducibility, not that the pinned revision matches every statement in the course; recheck the assigned section before teaching.

Grokking OOD's case-only `README.md`/`readme.md` collision still applies on case-insensitive filesystems: after checkout Git reports one modified file. Both originals remain in [provenance/grokking-ood-case-collision](provenance/grokking-ood-case-collision/README.md).

## Verified upstream refresh — September 11, 2026

Ran `git pull --ff-only --no-rebase --no-recurse-submodules --no-autostash` for all seven linked repositories. Then compared each HEAD with `git ls-remote`: all seven match their upstream branch, which is also the remote default branch, as of `2026-09-11T22:03:42.885246+00:00`. Source versions are recorded in [the machine-readable pull report](provenance/refresh-2026-09-11.json).

| Material | Branch | Before | After | Incoming commits |
|---|---|---|---|---:|
| tau | `main` | `55df51608b8b` | `55df51608b8b` | 0 |
| pi | `main` | `d12cd92e45e3` | `71dca871bc80` | 7 |
| learn-claude-code | `main` | `0dcafa2ae053` | `0dcafa2ae053` | 0 |
| you-dont-know-js | `2nd-ed` | `044120ef5556` | `044120ef5556` | 0 |
| system-design-primer | `master` | `ae9bbd7b02d9` | `ae9bbd7b02d9` | 0 |
| system-design-101 | `main` | `b28380a4710c` | `b28380a4710c` | 0 |
| grokking-ood | `master` | `3d35276091bc` | `ba7927f641f2` | 25 |

All pre-existing untracked files were hash-checked and preserved. Six worktrees retain their prior clean/untracked-only state. **Grokking OOD has an upstream case-only filename collision:** its Java airline example tracks both `README.md` and `readme.md`. This Mac cannot materialize both at once, so Git reports one modified file after the pull. [Both original blobs are preserved separately](provenance/grokking-ood-case-collision/README.md). No reset, stash or local commit was used.

Pi's updates do not change our selected agent-loop or extension readings. The three selected Grokking OOAD/class/sequence readings are unchanged. Grokking adds implementations, tests and design documents, so the earlier blanket description of its examples as non-executable is no longer sufficient. The root README retains that warning while the new library-example README describes an executable implementation; those implementations/tests were not run by this refresh. Optional reading placement remains appropriate.

The immediate learn-claude-code assignment is unchanged: `agent_loop()` remains at lines 87–117. Git pull updates source; it does not verify learning completion or install/update executable tools. Boot.dev, Node documentation, YSAP, LFS101 and other web-only references have no local Git checkout to pull. Use their live pages; publisher lesson versions were not audited in this Git refresh.

## Historical refresh — September 10, 2026

**Location update — September 11:** Tau and Pi were extracted to `~/Self-learn/tau` and `~/Self-learn/pi`. Complete file/symlink manifests and Git HEADs matched across the move; both repositories remained clean. The generated agent-learning parent, chapters and mini-agent were then deleted as requested. The September 10 observations below describe that earlier inspection; the linked locations have been updated.

Fetched all six existing Git repositories and fast-forwarded their current upstream branches. Each HEAD matches its fetched upstream; each branch is also the remote default. No tracked local edits existed. Existing untracked `.DS_Store` files were preserved and hash-checked.

| Material | Branch | Before | Current | Incoming commits |
|---|---|---|---|---:|
| [Tau](<sources/agents/tau>) | `main` | `5b00d95` | `55df516` | 240 |
| [Pi](<sources/agents/pi>) | `main` | `351efc8` | `d12cd92` | 1488 |
| [learn-claude-code](<sources/agents/learn-claude-code>) | `main` | `ec9ea87` | `0dcafa2` | 123 |
| [System Design Primer](<sources/design/system-design-primer>) | `master` | `b02784f` | `ae9bbd7` | 10 |
| [System Design 101](<sources/design/system-design-101>) | `main` | `b28380a` | `b28380a` | 0 |
| [You Don’t Know JS](<sources/javascript/you-dont-know-js>) | `2nd-ed` | `e3f784b` | `044120e` | 2 |

Tau’s current package declares **0.4.2**; Pi’s coding-agent package declares **0.85.1**. These are source checkouts; no dependencies or executable installations were changed by Git updates. This verifies freshness, not passing upstream tests or complete pedagogical accuracy.

## Course references affected

- learn-claude-code changed from the previously inspected 20-chapter track to **17 current root-level chapters**, with English as the default README. The old 12-lesson transition track remains separate. Use the current index for later chapters: tasks s10, background s11, cron s12, teams/worktrees s13, MCP s14, integrated harness s15, workflow runtime s16, goal loop s17.
- Tau’s tool-dispatch helper is now `_execute_tool_call`; the loop and event interfaces have changed significantly. Re-read the current function when teaching it.
- The generated `agent-learning` parent folder is not a Git repository and has no upstream to pull. Its prose remains outside the required syllabus.

## Linked materials without a local checkout

Checked these upstream default heads using `git ls-remote --symref`; no local copies were created:

- [SDE interview roadmap](https://github.com/aasthas2022/SDE-Interview-and-Prep-Roadmap): `81efbbf5c1b106bc824395c3b14f36ad8251ed04`.
- [YSAP Bash course](https://github.com/bahamas10/bash-course): `0fb288afb1a3bf96d5ffd4e33603047a22f55048`.

Boot.dev JS/TS, LFS101 and Effect are live course/documentation sites in this project, not local Git checkouts. Their URLs continue to serve current material; they have no local version to pull. Git freshness does not establish whether a course publisher has revised a particular lesson.

## Herdr 0.9.0

The Homebrew-installed client was already **0.9.0**, matching the [latest stable upstream release](https://github.com/herdrdev/herdr/releases/tag/v0.9.0) and [Homebrew formula](https://formulae.brew.sh/formula/herdr). No reinstall was needed. The named `terminal-practice` server was still **0.8.0** with an incompatible private protocol.

After explicit user approval to stop its pane processes, backed up saved session state and global config under `/tmp/herdr-terminal-practice-before-0.9.0`, stopped only that named server using Herdr, and started it with the installed 0.9.0 binary. Verified:

- Client 0.9.0; named server 0.9.0, running.
- Endpoint compatible: yes; private protocol 22, compatible: yes.
- Restart needed: no; server binary stale: no.
- No other named server was running when checked; no remote server was upgraded.

The server was started headlessly. Attach from a terminal with `herdr --session terminal-practice`. Previous shell processes were stopped as approved; this was not a live handoff. UI attachment, restored pane layout and new-feature exercises have not been verified in this update.

Relevant 0.9 changes to study later: saved SSH machines in one client, independent multi-client navigation, and improved client/server update compatibility. These are [release-note claims](https://github.com/herdrdev/herdr/releases/tag/v0.9.0), not newly completed exercises.

## Node.js learning references — added September 10, 2026

Official [Node.js Learn](https://nodejs.org/learn/getting-started/introduction-to-nodejs) and [API documentation](https://nodejs.org/api/) are now required live references. No local source checkout was created. The unversioned API site may describe a different release from the installed runtime; choose matching versioned docs when running the labs. No runtime/package-manager upgrade was performed.
