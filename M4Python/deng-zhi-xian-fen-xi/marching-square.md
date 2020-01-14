来源：[https://en.wikipedia.org/wiki/Marching\_squares](https://en.wikipedia.org/wiki/Marching_squares)

操作步骤：

1.将网格上的每一个2\*2单元格进行如下处理：

将  
单元格的点与要分析的数值\\(v\\)进行比对，如果大于v，则该点置位1，如果小于v，则该点置位0。这样，一个单元格可能如下15种情况，如果对单元格自左上角开始，顺时针4个位置分别代表二进制的1位，就有如下图所示的结果：  
![](/M4Python/images/7.png)

这里面会有2个歧义点，也叫鞍点

