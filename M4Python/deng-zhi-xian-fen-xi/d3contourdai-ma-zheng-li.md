d3contour工程位于surfacepro笔记本的C:\Users\sean\Documents\Projects\d3contour\_C\d3contour\_C目录下，是之前仿照d3.js移植过来的版本。主要考虑到javascript与C++中对于数据结构使用上的差异以及C\#调用C++内存释放的问题，在C++中进行了一些调整。

1. 首先调用InitializeCases函数创建一个定长的数组case，跟d3一样的方式进行初始化
2. 根据等值线的值进行循环遍历：
   1. 设计了结构体contour\_struct，用来存放所有的等值线，但这个结构体使用了int\*用来存放每一个等值线点的个数，使用 unsigned char\*标识每一个等值线的属性，使用float\*存放等值线上的经纬度位置。
   2. 使用vector存放所有的等值线contour\_struct实例
3. 遍历主程序create\_contours\_baseon\_value：
   1. 函数中定义了3个结构：polygon\_of\_a\_value,plygon\_size\_vector,polygon\_or\_holes\_sign，此处仿照d3中的isoring函数，
   2. 上下左右分别进行了1个单元格的扩展，先从左下角开始遍历，每一个单元格调用stitch\_loop进行分析
      1. 判断单元格中的等值线片段是一段还是两端，对每一段调用stitch函数
      2. 定义了全局变量 fragmentByStart和fragmentByEnd，类型均为map&lt;int,fragment\*&gt;。map为std::map，判断某一Key是否存在不能用contains这样的函数，技巧为：fragmentByStart.find\(endIndex\) !=fragmentByStart.end\(\)
      3. 这里有一个问题：每次新开辟的fragment结构体都是new出来的，但是没有被释放过！



