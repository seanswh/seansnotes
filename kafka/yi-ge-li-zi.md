来源：[https://www.learningjournal.guru/article/kafka/kafka-core-concepts/](https://www.learningjournal.guru/article/kafka/kafka-core-concepts/)

原文：Let's assume that we have a retail chain. In every store, there are few billing counters. You want to bring all of the invoices from every billing counter to your data center. Since you learned Kafka and you find Kafka as an excellent solution to transport data from billing locations to the data center. You decided to implement it.

The first thing you might want to do is to create a producer at every billing site. These Producers will send bills as a message to a Kafka topic. The next thing you might want to do is to create a consumer. The consumer will read data from the Kafka Topic and write them into your data center. It sounds like a perfect solution. Right?But there is a small problem. Think of the scale. You have hundreds of producers pushing data into a single topic. How will you handle that volume and velocity? You learned Kafka exceptionally well. So you decided to create large Kafka cluster and partition your topic. So your topic is partitioned and distributed across the cluster. Now several brokers are sharing the workload to receive and store data. From the source side, you have many producer and several brokers to share the workload. What about the destination side?

You have a single unfortunate consumer. There comes the consumer group. You create a consumer group and start executing many consumers in the same group, and tell them to share the workload. So far so good. But how do we split the work?

That's not a difficult question. I have 600 partitions. And I am starting 100 consumers. So each of the consumers takes six partitions. We will see, If they can't handle six partitions, we will start some more consumers in the same group. We can go up to 600 consumers, so each of them will have just one partition to read.

If you followed this example correctly, You understand that partitioning and consumer group is a tool for scalability. And also realize that the maximum number of consumers in a group is equal to the total number of partitions you have on a topic. Kafka doesn't allow more than one consumers to read from the same partition simultaneously. This restriction is necessary to avoid double reading of records.

假设有较大规模的连锁品牌,每一个连锁店中都有一些柜员机，你需要把每一个柜员机上的交易汇聚到统一的数据中心。既然我们学习了Kafka，我们认为这是一个较为完美的解决方案，咱们看看怎么实现它。

首先需要做的，是为每一个收费点创建一个producer。这个producer会把每一个交易记录整理成**消息**发送到Kafka的一个topic中去。其次，我们来创建这个消息的消费者\(consumer\)，它负责从topic中读取消息，并把它写道数据中心中。

但是有一个小问题，规模。如果是一个中等级别的连锁品牌，会有成百上千的柜员机向同一个topic中写消息，如何在如此规模下保持高效呢？学过kafka后，你决定建立一个“集群”来解决，同时可以将一个topic建立多个partition，这样，同一个topic就会被分布式化，会被负载到多个机器上去。这样，多个broker会共享这个工作，那么消息的另外一端呢？

一个消费者绝对是悲催的，因此我们考虑引入group的概念，我们创建了一个group，用来组织一些消费者，同样的，告诉这些消费者来共同分担消息处理的工作，但是我们怎么来分配消费工作呢？

比如我们建立对了600个partitions,我们创建了100个消费者，那么每一个消费者就被分配处理6个partitions，如果每一个消费者不能及时处理6个partitions，那我们就多加一些消费者进这个组就好了，最多，我们可以加到600个消费者，每一个消费者负责一个partition即可。

这个例子可以很好的说明，partition和consumer group是一种水平扩展的工具，一个group的consumer个数最多与要处理的topic中的partition相同。kafka不允许一个partition同时被一个组中的多个consumer消费，这可以很好的避免一个记录被重复处理。

