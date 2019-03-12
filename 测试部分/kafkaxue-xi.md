最近工程需要用到Kafka作为消息中间件将不同的预报、服务系统串联起来，因此考虑使用消息中间件进行消息传递。
通过对比分析，目前主流的消息中间件技术有Kafka和RabbitMQ两类，两者的优劣对比在如下网页中有较详细的介绍：
https://itnext.io/kafka-vs-rabbitmq-f5abc02e3912
最终选型使用Kafka
除此之外，高惠已经在中央台部署了服务器10.20.90.35:9092，因此就尝试使用一下。
之前韩丰设计了消息格式
使用该格式在10.28.30.43机器上的jupyter上做了测试，分别写了测试端与服务器端，测试了单消息发送、中文消息发送、将Dictionary封装成Json字符串后发送，隔1ms发送1000条消息等，效率和结果都还不错~
![](/测试部分/images/1.png)
![](/测试部分/images/2.png)

发现一个问题，测试了好久：jupyter notebook由于采用了异步机制，造成可能会同时执行多个consumer的情况，因此在执行cosumer的时候，最好还是在命令行下执行py文件好了~~

consumer代码如下，这里增加了offset的设置机制，确保客户端down机一段时间后重启也能拿到历史数据的情况。
另外，为了避免每次启动都会从 offset=0开始获取，这里增加了enable_auto_commit=True语句，记录客户端down机前识别的最后一个offset。
```
consumer = KafkaConsumer(
    'test',
     bootstrap_servers=['10.20.90.35:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda m: json.loads(m.decode('utf8')),
     group_id='my-group',
    )
for message in consumer:
    print(message)
```
另外，设置不同的group_id，可以确保不同的进程都能获取到消息。
