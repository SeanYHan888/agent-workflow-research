# Message broker and event-stream readings

For [M7 broker study](../course/modules/message-brokers.md). Official sources checked September 28, 2026. Select sections for the lab question; pin broker/client/image versions when activating a lab. Kafka 4.3 documentation below is a reading reference, not a claim that a local version is installed.

| Source | Reading question |
|---|---|
| [RabbitMQ work queues](https://www.rabbitmq.com/tutorials/tutorial-two-python) | How do competing consumers, manual acknowledgements, persistence and prefetch affect a worker that fails? Translate the example into the learner's chosen supported client rather than requiring a second language course. |
| [RabbitMQ confirms and acknowledgements](https://www.rabbitmq.com/docs/confirms) | Which boundary does each confirmation cover? What remains uncertain after a lost connection? |
| [RabbitMQ dead-letter exchanges](https://www.rabbitmq.com/docs/dlx) | Where do rejected/expired messages go, and how do we avoid a retry cycle? |
| [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues) | Which replication and availability assumptions hold? Distinguish one-node persistence from a replicated deployment. |
| [Kafka introduction](https://kafka.apache.org/43/getting-started/introduction/) | How do retained records, partitions and independent consumers support replay? |
| [Kafka design](https://kafka.apache.org/43/design/design/) | Read the delivery-semantics and replication sections: where are offsets and effects coordinated, and what does exactly-once cover? |

Assessment questions and experiment design are our course synthesis. This source selection neither installs a broker nor selects a production transport. A tutorial's happy-path output is not sufficient acceptance evidence.
