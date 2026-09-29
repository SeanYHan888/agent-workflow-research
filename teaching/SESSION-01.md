# Session 01 — teacher preparation

Historical/review preparation. The tool-cycle section was completed September 13; use the roadmap and current Obsidian evidence to prepare the active session.

Purpose: determine whether the learner can distinguish a model's request from execution by the harness. Planned student effort: 30–45 minutes. No API call or installation.

Student handout: [One tool cycle](handouts/03%20One%20Tool%20Cycle.md). Preserved progress owner: Obsidian `Projects/Archive/terminal-agent-01-agent-loop.md`.

## Source checked September 11

`/Users/seanmacbook/Self-learn/learn-claude-code/s01_agent_loop/code.py`, local commit `0dcafa2ae053`, `agent_loop()` lines 87–117. This is a third-party teaching implementation. Inspect the file again if its revision changes.

## Teaching sequence

Ask the learner to predict the order before identifying the code lines. If vocabulary blocks the attempt, use the handout's tiny scripted trace. Read only the function, then ask for an explanation in their own words.

Review anchors:

- Lines 89–92 obtain a model response. The model returns content, including possible tool requests.
- Line 95 appends the assistant response. Lines 98–102 find tool-use blocks and return if none exist.
- Line 108 calls `run_bash`; Python/harness execution invokes the tool. The model is not itself executing the command.
- Lines 110–117 associate output with the tool call ID and append results for the next request. In this example the provider format represents these results in a user-role message.
- Continued tool requests keep this function looping; it has no explicit turn-count bound. `max_tokens` on one model call is not a limit on total loop iterations. Exceptions can also abort execution, which differs from normal return.

If they say “the AI runs it,” ask them to point to the actual function call. If they confuse tool output with the final answer, ask what the next `messages` list contains. If they claim a global iteration cap, ask them to locate it.

The first checkpoint is the explanation and trace. The full section also requires the later fixture-reading dispatcher and an unknown-tool case. Do not mark the section complete after this reading alone.

After the explanation is reviewed, prepare Session 2 interactively: a narrow fixture-reading tool with scripted requests. Give a stub or hints appropriate to the demonstrated gap; do not prebuild its solution. Use Tau only after the simple cycle is understood, introducing async separately before following async code.
