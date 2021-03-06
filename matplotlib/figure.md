### 3.Figure

![](/assets/anatomy.png)

上图是一个Figure的组成，一个Figure包含各个轴（axes\),一部分特殊元素（标题，图例等）以及画布\(canvas\)，一个画布是绘制区域，但是对于用户来说通常是不可见的。一个Figure可以有任意多个轴\(axes\)，一般来说，通常都会至少有一个轴存在。

### Axes

这个就是图像单元，是一个数据空间内的图像化展示，一个figure可以包含多个axes，但是一个指定的axes对象只能在一个figure中。一个Axes可以有两个axis\(坐标轴\)或三个axis对象，注意Axes和Axis的区别。Axis会考虑数据的边界问题\(也可以通过set\_xlim或者set\_ylim函数控制轴的范围\).每一个Axes都有一个标题\(title\),一个x-label（可以通过set\_xlabel\)设置，一个y-label.

Axes类和它的成员函数是面向对象接口进行编程的主要入口

### Axis

这是**数字-线**型\(number-line-like\)的对象。它用来负责绘制图形的边界，创建刻度线\(ticks\)以及刻度线上的字符串\(tickable\)。刻度的位置由Locator对象决定，tickable的字体格式由Formatter对象决定。

### Artist

一般来说，你在figure上看到的任何图元都是一个Artist\(甚至包括figure，Axes，以及Axis等对象\)。Artist包括了文本对象、Line2D对象，集合对象\(collection objects\)以及Patch对象等。当figure被绘制的时候，所有的artists被绘制在canvas上。绝大多数的Artist被绑定在一个Axes上，而Artist无法被多个Axes共享，也不能在Axes之间移动



