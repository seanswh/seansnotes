ASCII使用1个字节，只能存储128个字符
UTF-16使用固定的2个字节
UTF-32使用固定的4个字节
UTF-8使用变长的1-4个字节，而且向下兼容ASCII，现在各个系统推荐使用UTF-8来存储字符串。
![](/pythonwebdata/images/Utf8webgrowth.svg.png)
上图显示了各个编码格式使用的趋势