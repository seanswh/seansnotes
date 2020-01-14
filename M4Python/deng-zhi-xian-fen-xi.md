MICAPS4的等值线分析参考d3.js工程中的代码，对javascript代码进行移植，形成C++代码，主要是考虑到代码不容易被反编译。

原始的javascript代码在surfacepro电脑中，位置为：D:\Projects\node\_projects\learnyounode，需要安装Node.js进行调试。

移植后的C++代码在C:\Users\sean\Documents\Projects\d3contour\_C目录下。

现在为了总结，特立此贴。

等值线分析算法原理不难，主要是javascript的算法提供了快速遍历的方法，可以显著提升效率

