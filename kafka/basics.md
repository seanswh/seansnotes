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

Consumer Group\(消费组\)顾名思义就是一组Consumer\(消费者\)的总称.如果只有一组内且组内只有一个Consumer,那这个就是传统的点对点模式,如果有多组,每组内都有一个Consumer,那这个就是发布-订阅\(pub-sub\)模式.每组都会收到同样的消息.

首先,一个Consumer\(消费者\)的一个线程在某个时刻只能接收一个partition\(分区\)的数据,一个partition\(分区\)某个时刻也只会把消息发给一个Consumer\(消费者\).我们设计出来几种场景:

**场景一:** topic-1 下有partition-1和partition-2 。group-1 下有consumer-1和consumer-2和consumer-3 

所有consumer只有一个线程,且都消费topic-1的消息. 消费情况 : consumer-1只消费partition-1的数据 

consumer-2只消费partition-2的数据 consumer-3不会消费到任何数据 原因 : 只能接受一个partition\(分区\)的数据

**场景二: **topic-1 下有partition-1和partition-2 ，group-1 下有consumer-1 。consumer只有一个线程,且消费topic-1的消息. 消费情况 : consumer-1先消费partition-1的数据 consumer-1消费完partition-1数据后开始消费partition-2的数据 

原因 : 这里是kafka检测到当前consumer-1消费完partition-1处于空闲状态,自动帮我做了负载.所以大家看到这里在看一下上边那句话的”某个时刻” 

特例: consumer在消费消息时必须指定topic,可以不指定partition,场景二的情况就是发生在不指定partition的情况下,如果consumer-1指定了partition-1,那么consumer-1消费完partition-1后哪怕处于空闲状态了也是不会消费partition-2的消息的.



