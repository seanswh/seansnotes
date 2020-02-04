原始的项目是在SEAN-MINI主机上做了部分集成：首先是在MICAPS4.0的基础上做了一个分支，自定义了界面窗口；其次是使用了新的等值线分析算法，同时为了配合新的等值线分析算法，使用了新的MICAPS底层库：CMA.MICAPS.Renders.dll,当进行格点数据显示时，底层框架会直接调用CMA.MICAPS.Algorithm.dll库中的CMA.MICAPS.Algorithms.Contours.Contour.CreateContourPolygonsEx函数。这个函数返回值是Line2F数组，用来存放所有等值线的边界。

这里发现了点小问题：

> C\#代码中使用了contour\_get\_line\_status函数用来判断当前闭合等值线是polygon\(true\)还是hole\(false\)，如果是hole,就直接跳出，如果是polygon再进行绘制。C++代码中contour\_get\_line\_status函数是返回的polygon\_ring数组中的内容，这个数组是在stitch中进行赋值，也是判断多边形的面积，这里判断如果面积大于0，标记为true,如果面积小于0，标记为false，根据对面积计算的算法进行分析结果判断（分析过程在visio文件：d3等值线算法中）小于0是逆时针也就是hole，&gt;0是顺时针也就是polygon，看似C\#中代码判断是正确的。
>
> 但实际上不是这样
>
> 显示EC数据后发现，结果正好相反：true的时候是hole，false的时候是polygon，这是咋回事呢~



