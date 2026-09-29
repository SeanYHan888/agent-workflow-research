---
title: Coding Agent Course — One Tool Cycle
created: 2026-09-11
tags:
  - learning/coding-agents
---
# One tool cycle

[[Notes/Coding Agent Course/00 Start Here|Start Here]] · [[Projects/Archive/terminal-agent-01-agent-loop|Tasks and progress]]

**Question for this session:** when an assistant asks to read a file, which part actually reads it?

Spend 30–45 minutes. You need only the source file and somewhere to write your explanation. This is a reading and tracing session; no API call or installation.

## Before reading

A **model** produces a response. A **tool request** is structured data asking for an operation. A **harness** is the surrounding program that calls the model, invokes tool code and carries messages forward. A **tool result** is the output of that invocation.

Predict the order of events in this deliberately simplified, scripted example. It is not a real provider message format:

```text
User asks: What is in hello.txt?
Model requests: read_file(path="hello.txt", call_id="1")
Harness invokes the registered file-reading function.
Function returns: "hello"
Harness adds the request and matching result to the conversation.
Model receives that conversation and produces an answer.
```

Point to the step that touches the filesystem. Then point to the step that makes the contents available to the next model call.

## Read one function

Open [s01_agent_loop/code.py](file:///Users/seanmacbook/Self-learn/learn-claude-code/s01_agent_loop/code.py) and read only **`agent_loop()`**, lines **87–117** in local revision `0dcafa2ae053` (checked September 11).

The source example uses a Bash tool instead of the scripted file-reading tool above. Locate the model call, assistant-message append, tool execution, tool-result append and normal return. Follow the values in `messages`, `response`, `tool_calls` and `results` for one iteration.

This is a third-party teaching implementation. Its small size makes the flow easy to inspect; it does not define the complete behavior of Claude Code.

## Bring back these answers

1. Who executes the command? Identify the function call that establishes your answer.
2. What is added to `messages` after the model responds and after the tool executes? Why are both needed for the next call?
3. What makes this function return normally? What happens if the model keeps requesting tools? Find any limit on the number of loop iterations, or explain its absence.

Write a short trace in your own words. For each event, name the owner and the value that changes. Record your answers and focused minutes in [[Projects/Archive/terminal-agent-01-agent-loop#Progress log:|the project's progress log]], or bring the answers to our teaching conversation for review.

Stop at the explanation checkpoint. After review, the next session is a tiny fixture-reading dispatcher and an unknown-tool case. Completing this reading alone does not complete the full section.
