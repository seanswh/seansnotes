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



