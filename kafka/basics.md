资料来源：[https://blog.csdn.net/shangmingtao/article/details/79567921](https://blog.csdn.net/shangmingtao/article/details/79567921)  
由Scala和Java编写,Kafka是一种高吞吐量的分布式发布订阅消息系统.

## **术语介绍**

* Broker : Kafka集群包含一个或多个服务器，这种服务器被称为broker
* Topic : 每条发布到Kafka集群的消息都有一个类别，这个类别被称为Topic。（物理上不同Topic的消息分开存储，逻辑上一个Topic的消息虽然保存于一个或多个broker上但用户只需指定消息的Topic即可生产或消费数据而不必关心数据存于何处）
* Partition : Partition是物理上的概念，每个Topic包含一个或多个Partition.
* Producer : 负责发布消息到Kafka broker
* Consumer : 消息消费者，向Kafka broker读取消息的客户端。
* Consumer Group : 每个Consumer属于一个特定的Consumer Group（可为每个Consumer指定group name，若不指定group name则属于默认的group）。

![](/assets/20180315151540326.png)

MQ\(消息队列\)：是在服务端存储一个队列.生产者把消息丢到MQ server,消费者从MQ server消费.这样一来解决了生产者和消费者的高耦合问题,同时也解决了生产速度和消费速度差异导致的消费者跟不上生产者的生产速度而导致的消费者压力过大问题.

在kafka中的topic就是**一系列队列**的总称,称为一个主题.当然ActiveMQ和RabbitMQ中都有这个概念.一类消息都会丢到一个topic中去.

partition\(分区\)是kafka独有的东西,也是kafka实现横向扩展和高并发的一个重要设计.我们试想一下,如果每个topic只有一个队列,随着业务增加topic里消息越来越多.多到一台server装不下了怎么办.为了解决这个问题,我们引入了partition这个概念.一个partition\(分区\)代表了一个物理上存在的队列.topic只是一组partition\(分区\)的总称,也就是说topic仅是逻辑上的概念.这样一来当topic上的消息越来越多.我们就可以将新增的partition\(分区\)放在其他server上.也就是说topic里边的partition\(分区\)可以分属于不同的机器.

从Producer\(生产者\)角度,一个消息丢到topic中任务就完成了.至于具体丢到了topic中的哪个partition\(分区\),Producer\(生产者\)不需要关注.这里kafka自动帮助我们做了负载均衡.当然如果我们指定某个partition\(分区\)也是可以的.

