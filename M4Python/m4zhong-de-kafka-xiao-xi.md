MICAPS4.5版本之后支持了Kafka消息，各个模块均可注册某一topic中的消息，也可向topic中发送消息，不过需要以下DLL的支持：

![](/MICAPS4Dev/M4MsgReliance.PNG)以及：

![](/MICAPS4Dev/libkafka.PNG)

2.Kafka消息的订阅

```
var messageFactory = ServiceLocator.Current.GetInstance<IMessageServiceFactory>();
//创建kafka消息的服务参数
var option = MessageOptions.Create(new MeteoURI("kafka://10.20.67.183:9092"), false, false);
//需要订阅的消息名称
string topicName = "test";
//消息服务
messageService = await messageFactory.CreateMessageServiceAsync(option).ConfigureAwait(false);
var messageHandler = new MessageHandler<MessageData>()
{
     OnReceivedHandler = OnReceived
};
messageService.Subscribe(topicName, messageHandler);
```



