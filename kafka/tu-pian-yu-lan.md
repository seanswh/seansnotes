新的尝试：MICAPS图片预览功能

大概流程：预报员通过“产品保存助手”选择14类数据的类型和保存地址，当用户选择“临时保存”时，将数据存放在一个临时共享目录里，然后给kafka服务器发送消息，MESIS服务器接收并处理该消息，从共享目录中拿到数据后进行出图任务，然后返回

目前完成：

1。改造module.toolbox模块，在SaveCommand.cs文件中增加InitializeMessage方法以及SendMessage方法

