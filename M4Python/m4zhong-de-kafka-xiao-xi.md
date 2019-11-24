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
//消息服务句柄
messageService = await messageFactory.CreateMessageServiceAsync(option).ConfigureAwait(false);
//消息接收处理方法
var messageHandler = new MessageHandler<MessageData>()
{
     OnReceivedHandler = OnReceived
};
//消息订阅注册
messageService.Subscribe(topicName, messageHandler);
```

上述操作之后，来自指定地址的指定topic中的消息将会被监听，当接收到该消息后，会调用OnReceived函数进行处理，该函数定义为：

```
 private void OnReceived(MessageData md)
  {
            if (null == md || string.IsNullOrWhiteSpace(md.source))
            {
                return;
            }
  }
```

这里需要注意的是，MessageData需要实现定义，这个与订阅消息时需要的messageHandler使用的是同一个类型，这个与Kafka中的消息结构一一对应



