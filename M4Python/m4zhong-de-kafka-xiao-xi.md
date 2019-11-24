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

这里需要注意的是，MessageData需要实现定义，这个与订阅消息时需要的messageHandler使用的是同一个类型，这个与Kafka中的消息结构一一对应。

3.Kafka消息的发送

Kafka消息的发送与订阅中使用的messageService构造方式一样，最后调用的方法不是Subscribe函数，而是SendAsync方法，如下所示：

```
messageService.SendAsync<MessageData>("product_preview", md);
```

MessageData与前面订阅中使用的消息类型一致，也是用来转化成json字符串时所需的结构体，第一个参数是topic名称，第二个参数为要发送的MessageData实例。

4.MessageData说明

MessageData为用来接收\发送消息时从json字符串转化的结构体，如下面所示的是一种结构：

```
public class MessageData
{
    public string source;
}
```

这个结构对应的消息内容只包含一个key-value对，即：source:{"......"}

