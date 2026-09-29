# M7 — message brokers and event streaming

Required topic added September 28, 2026 at the student's request. This expands M7's queue and durable-work criteria; existing milestone IDs and earned evidence remain valid. RabbitMQ and Apache Kafka are both studied through bounded experiments. The capstone chooses the transport its workload justifies; it need not operate both.

## Purpose and boundary

Design communication between agent workers that survives retries and partial failure. Distinguish a command asking for work from an event recording what happened, transport delivery from completed business effects, and a broker from a workflow engine or system of record. Explain when a simpler queue or direct request is sufficient.

Entry: M4 worker contracts, M5 processes/networking/containers and restart recovery, basic async code and persistent state; M11 test/review fundamentals. Introduce vocabulary earlier if useful, but do not interrupt current JS/Node work to install brokers.

| Study lens | RabbitMQ lab | Kafka lab |
|---|---|---|
| Primary course example | Route a bounded job to competing workers | Retain job-lifecycle events for independent consumers and replay |
| Core objects | Exchanges, bindings, routing keys, queues, consumers | Topics, partitions, keys, records, consumer groups, offsets |
| Progress and recovery | Publisher confirms, manual consumer acknowledgements, redelivery, prefetch | Producer acknowledgements, offset commits, retention, replay, group reassignment |
| Failure questions | What if the effect completes before the acknowledgement? What if publishing times out? | What if the effect completes before the offset commit? What changes when a partition moves? |

These are teaching examples, not exclusive product categories. RabbitMQ also supports streams; Kafka supports additional consumption models. Advanced variants remain optional. [Official reading map](../../materials/message-brokers.md).

## Learning sequence and bounded labs

| Unit | Work and evidence | Initial budget |
|---|---|---|
| B1. Choose the communication contract | Draw producer → broker → consumer → durable effect. Explain command/event, competing workers versus independent subscriptions, ordering scope and overload. Predict failure at each boundary. | 2–3 core hours |
| B2. RabbitMQ reliable job delivery | A local/disposable broker and two workers; route jobs, use confirms/manual acknowledgements, bound in-flight work, inject worker loss and duplicate delivery, and quarantine a repeatedly failing message with a bounded retry policy. Verify effects by job ID. | Up to 6 hours including setup and assessment |
| B3. Kafka lifecycle stream | A local/disposable KRaft lab; key events by job ID, run independent consumer groups, stop/restart a consumer, replay retained records and rebuild a small projection. Inject a duplicate; explain partition ordering, commits and group reassignment. | Up to 6 hours including setup and assessment |
| B4. Compare and defend | One short ADR for the course workload; compare broker versus application guarantees, storage/operations burden and failure evidence. Diagnose an unfamiliar acknowledgement/commit bug. | 2–3 core hours |

Initial topic estimate: **16–18 hours**, including shared M7 queue/retry learning rather than counting it twice. Core lessons consume the existing 10-hour allocation. If a lab uses the 3-hour project slot, each six-hour lab is a separate two-week project, scheduled sequentially. Preserve the 15-hour weekly total and one active project. Setup overruns trigger a smaller slice or reforecast, not an unbounded project. Dates remain unassigned until readiness review; this addition does not assert that earlier forecasts still fit.

## Required reasoning and acceptance

- Show a crash after the durable effect but before acknowledgement/offset commit. On retry, demonstrate application-level deduplication with a durable identity and consistent state update; a broker acknowledgement alone cannot establish the external effect happened once.
- Distinguish at-most-once and at-least-once delivery from scoped exactly-once processing. Explain why Kafka transactions do not automatically make an arbitrary model API call or external write exactly once. Analyze the database/broker dual-write gap and an outbox/inbox design; implementing a full CDC platform is optional.
- State ordering assumptions: partition/key assignment, concurrency and retry behavior. Never infer global ordering from one successful run.
- Observe ready/unacknowledged messages or consumer lag, oldest-work age, retries, processing latency and resource use. Demonstrate bounded overload behavior and justify a retry/dead-letter policy instead of infinite requeueing.
- Explain persistence, replication/quorum and failure-domain assumptions. A single broker/container restart lab proves local restart behavior, not multi-host availability. M7/M10 still require the separate distributed failure evidence.
- Submit the artifact/configuration, failure trace, independent effect checks, comparison/ADR and learner explanation. Pass an unfamiliar variation under the shared [assessment rubric](../ASSESSMENT.md).

Out of scope for the first labs: production cluster administration, managed-service purchases, full stream-processing/CDC platforms and running brokers alongside inference on an unmeasured small VPS. M8 can later deploy an understood service; Kubernetes is not a prerequisite for the introductory experiments.
