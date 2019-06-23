来源：[https://www.learningjournal.guru/article/kafka/kafka-core-concepts/](https://www.learningjournal.guru/article/kafka/kafka-core-concepts/)

原文：Let's assume that we have a retail chain. In every store, there are few billing counters. You want to bring all of the invoices from every billing counter to your data center. Since you learned Kafka and you find Kafka as an excellent solution to transport data from billing locations to the data center. You decided to implement it.

The first thing you might want to do is to create a producer at every billing site. These Producers will send bills as a message to a Kafka topic. The next thing you might want to do is to create a consumer. The consumer will read data from the Kafka Topic and write them into your data center. It sounds like a perfect solution. Right?But there is a small problem. Think of the scale. You have hundreds of producers pushing data into a single topic. How will you handle that volume and velocity? You learned Kafka exceptionally well. So you decided to create large Kafka cluster and partition your topic. So your topic is partitioned and distributed across the cluster. Now several brokers are sharing the workload to receive and store data. From the source side, you have many producer and several brokers to share the workload. What about the destination side?

You have a single unfortunate consumer. There comes the consumer group. You create a consumer group and start executing many consumers in the same group, and tell them to share the workload. So far so good. But how do we split the work?

That's not a difficult question. I have 600 partitions. And I am starting 100 consumers. So each of the consumers takes six partitions. We will see, If they can't handle six partitions, we will start some more consumers in the same group. We can go up to 600 consumers, so each of them will have just one partition to read.

If you followed this example correctly, You understand that partitioning and consumer group is a tool for scalability. And also realize that the maximum number of consumers in a group is equal to the total number of partitions you have on a topic. Kafka doesn't allow more than one consumers to read from the same partition simultaneously. This restriction is necessary to avoid double reading of records.

