关于SOCKETS，Ports，HTTP协议等，  
知识较为基础，没有太多笔记，重要的是sample codes  
另外，python默认的字符串编码格式是UTF-8,而网络传输的字符串默认格式是Bytes，因此，在通过socket发送消息的时候需要先将消息encode\(\)成bytes格式。从socket上接收到消息显示的时候，还需要decode成unicode格式
![](/pythonwebdata/images/2.PNG)

