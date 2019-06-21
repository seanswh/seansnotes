[https://lotabout.me/2018/kafka-introduction/](https://lotabout.me/2018/kafka-introduction/)

Kafka 在概念上将一个 Topic 分成了多个 Partition，写入 topic 的消息会被（平均）分配到其中一个 Partition。Partition 中会为消息保存一个 Partition 内唯一的 ID ，一般称为偏移量\(offset\)。这样当性能/存储不足时 Kafka 就可以通过增加 Partition 实现横向扩展。

