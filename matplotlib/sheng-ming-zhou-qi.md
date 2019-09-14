matplotlib有两种接口，第一个是面向对象的接口，我们使用Axes的实例，而Axes又是在figure的实例上绘制的。第二种方式是基于类似于MATLAB方式的基于状态\(state-base\)的接口，这个接口被封装在pyplot模块之中。

有两点是需要注意的：

1. Figure形成了最重的图像\(Image\)，包含一个或多个Aexs
2. Aexs代表一个独立的图形\(plot\)

我们可以调用Axes上的绘制函数进行直接绘制，这种方式提供了更加灵活和强大的自定义绘制方式。也就是说，尽量使用面向对象的绘图方式，而不是使用Pyplot中的。

存储：

使用[`figure.Figure.savefig()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.savefig)可以将当前figure存储在磁盘中，有以下常用参数:

`transparent=True`makes the background of the saved figure transparent if the format supports it.

`dpi=80`controls the resolution \(dots per square inch\) of the output.

`bbox_inches="tight"`fits the bounds of the figure to our plot.



