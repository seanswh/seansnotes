MICAPS4中的总线使用了依赖注入这样的容器技术以及serviceLocator资源定位工具，使得模块和模块之间可以通过底层框架中的方法进行通讯，

通讯双方为“消息发送者”和“消息消费者”，发送者将消息发送给MICAPS的IBUS的消息总线，接受者通过IBUS消息总线接受和处理，但是目前消息的发送和接受者的约定为**“消息类型”。**通讯方法如下所示：

1.发送消息方法：

ServiceLocator.Current.GetInstance&lt;IBus&gt;\(\).Publish&lt;string&gt;\("messageQueue\_" + md.source\);

通过ServiceLocator获取到实现IBUS的实例，然后广播一个类型为string的消息，消息内容为一个字符串。

2.消息订阅方法：

\_serviceLocator.GetInstance&lt;IBus&gt;\(\).Subscribe&lt;string&gt;\(OncommandStarup\);

Subscribe一个类型为string的消息，然后通过OncommandStarup函数进行处理，这个函数的定义为：

```
 private void OncommandStarup(string startupMessage)
 {
 
 }
```



