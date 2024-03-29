1.\)d3算法是对Marching Square算法的实现，不过做了些许调整：在前一篇讲到单元格的15种情况对应的15个数值的时候，使用的是从左上角开始顺时针旋转，四个顶点分别占位4，3,2,1（由高到低）。在D3中，是从左下角开始，进行逆时针旋转，分别占位4,3,2,1（由高到低）。两种编码规则等效，只要对应的等值线片段正确即可。

2\)增加了方向：所有的等值线片段中，置位1的顶点均出现在片段的右侧，这样就能保证最后连接的等值线，如果是顺时针的线条，其内部的数据是大于等值线的值的；如果是逆时针旋转的线条，其内部的格点是小于等值线的值的。

将上述的规则进行了预处理，存储了一个长度为15的数组\(cases\)，数组中每一个成员也是Points数组，Point的x,y值存放的是“类索引”内容，即单元格的左下角是x=0.5,y=0.5，右上角是x=1.5,y=1.5。

注：顺时针逆时针判断可以用向量叉积，根据右手定理，逆时针为正，顺时针为负

3）d3的等值线分析第一步分析函数为isorings，在这个函数里会逐行分析每一个单元格的等值线片段。

首先将格点**向外扩展一圈,**然后从格点场的左下角单元格开始依次逐行分析等值线片段\(d3的算法大量用到了“按位移动”的方式，这也与前两步初始化单元格结合起来，因此这里判断效率较高\)。通过检索cases数组得到片段，然后进行拼接

```
1.拼接函数为stitch:因为cases中存储的片段都是当前单元格的相对索引值，所以首先将片段加上当前的索引偏移，然后根据片段上的点的x，y索引值获取\\*\\*当前点的索引值,方法为函数index,方法为：\\*\\*
```

```
     index = x*2+y*(size_x+1)*4
```

线段的起点索引为startIndex，终点索引为endIndex

stitch函数中创建了2个数组：fragmentByStart及fragmentByEnd，前者存放的是所有等值线中的起始索引以及其对应的结构体，后者存放的是所有等值线中的结束点的索引及其对应的结构体，结构体如下所示：

```
{start: startIndex, end: endIndex, ring: [start, end]}
```

这个结构体中，start表示当前拼接后的等值线的起始点索引值，end表示当前拼接的等值线的结束点的索引值，ring为当前等值线中从start开始到end结束，所有的点的索引值。

具体算法过程可参考 onedrive/个人/文档/d3等值线算法.vsdx

