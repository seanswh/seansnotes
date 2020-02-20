在数据源检索窗口中增加一个关键字检索功能，用户可以在窗口中输入一个字符串，下方的树形结构中只显示与字符串匹配的内容。

整体工作复杂度不高，涉及到一些算法和IT技巧记录在此：

1.已经事先将相关的BDIPS中的数据目录导出在一堆txt文件中，为了每次进行匹配时效率高一些，将该txt文件进行二进制处理。目前考虑的是将所有的txt内容存储在一个map中，通过protobuf对C\#的map进行序列化与反序列化，顺便还能实现字符串压缩和加密的功能。

实验了一天，现在可以跑通了：1）从github上下载release版的protobuf，里面包含protoc.exe程序，把手工创建的proto文件放在exe同级目录下，然后执行语句：

`protoc --csharp_out=D:\softwares\protoc-3.11.3-win32\bin test.proto`

test.proto原始文件为：

```
syntax = "proto3";
package SeraializationAllBDIPSDic;

message BDIPS
{
    map<string,string> rawInfos = 1;
    map<string,string> translatedInfos = 2;
}
```

2.建立工程SeraializationAllBDIPSDic，路径在Sean-Mini主机的C:\Users\Sean\Documents\Visual Studio 2017\Projects\SeraializationAllBDIPSDic地址下

通过Nuget包管理离线导入google.protobuf库

然后读取cassandra导出的各级目录，通过protobuf写入一个二进制文件

3.通过protobuf读取此二进制文件,然后根据用户输入的字符串进行查询

使用数组匹配查询，效果超出预期，全部字符串匹配下来时间只需20ms

-------------------------------------MICAPS4数据源检索模块问题

1. 旧版本中，“重新加载”按钮点击后只会重绘'mdfs‘标签页下的树形结构，但是新版本下点击“重新加载”后，整个tab页全部重绘了，这个是影响“重新加载”效率的原因之一
2. 每一次过滤检索，都要递归遍历所有的Node，这个根本没必要！只要检查当前节点的所有下一级子节点就行了！，比如第一次只需要判断mdfs根节点和所有的二级节点。如果用户点击了”数据源检索“二级节点中的“EC细网格”节点以后，就只判断”EC细网格“节点下面的子节点全局路径在不在dic里面key=“EC细网格"的List&lt;string&gt;中即可，没必要再从mdfs根节点遍历一遍。
3. FindSearchNode函数：



