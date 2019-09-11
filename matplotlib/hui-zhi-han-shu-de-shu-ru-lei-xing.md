什么是后端程序\(backends\)？

matplotlib针对许多不同的应用场景定义了不同的输出格式。有些人在python shell中以交互方式使用matplotlib，并在键入命令时弹出绘图窗口。有些人运行[Jupyter](https://jupyter.org/)笔记本并绘制内联\(inline\)图以进行快速数据分析。其他人将matplotlib嵌入到图形用户界面（如wxpython或pygtk）中以构建丰富的应用程序。有些人在批处理脚本中使用matplotlib从数值模拟生成后处理\(postscript\)图像，还有一些人运行Web应用程序服务器来动态提供图形。

为了支持所有这些用例，matplotlib可以定义不同的输出，并且这些功能中的每一个都称为后端（Backends）; “前端（frontend）”是面向用户的代码，即绘图代码，而“后端（Backends）”完成幕后的所有艰苦工作以生成对应的图形。 有两种类型的后端：用户界面后端（用于pygtk，wxpython，tkinter，qt4或macosx;也称为“交互式后端”）和硬拷贝后端来制作图像文件（PNG，SVG，PDF，PS; 也被称为“非交互式后端”）。

有四种方式来配置后端，如果这些方式之间有冲突，那么后面介绍的方法会覆盖掉前面的，例如，调用[use\(\)](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.use)将覆盖`matplotlibrc`中的设置。

方法1:修改matplotlibrc文件

方法2：设置MPLBACKEND环境变量，设置这个环境变量后会覆盖matplotlibrc文件中的参数

方法3：代码实现：

```
import matplotlib
matplotlib.use('PS')# generate postscript output by default
```

如果要使用use\(\)函数，该函数必须要在 import matplotlib.pyplot 语句之前，否则不会起作用。使用use之后，如果用户需要使用不同的backend，需要用户调整代码方式。

> 注意：后端名称大小写不敏感，比如'GTK3Agg' and 'gtk3agg'是等效的。
>
> 注：上述的第三种方式是目前MICAPS4工具箱显示matplotlib结果的实现方式。

为了使图形用户界面可以更加自定义，matplotlib将画布（绘图所在的位置）与渲染器（实际进行绘制的工具）的概念分开，一般使用用户界面进行绘制的经典渲染器就是AGG渲染器了，它使用[Anti-Grain Geometry](http://antigrain.com/) C++ 库来进行图像绘制。除了macosx以外，除macosx之外的所有用户界面都可以与agg渲染一起使用，包括WXAgg，GTK3Agg，QT4Agg，QT5Agg，TkAgg等。

渲染器有矢量与栅格之分，矢量渲染器的渲染命令更像是“从某点到某点绘制一条线”，而栅格渲染器则是生成线段的像素显示，其精度取决于DPI的大小。

下面是matplotlib渲染器的摘要\(每个渲染器都有一个同名的后端；它们是非交互式后端，能够写入文件\)：

| 渲染格式 | 文件类型 | 描述 |
| :--- | :--- | :--- |
| [AGG](https://matplotlib.org/glossary/index.html#term-agg) | [png](https://matplotlib.org/glossary/index.html#term-png) | [raster graphics](https://matplotlib.org/glossary/index.html#term-raster-graphics)-- 使用[反纹理几何（Anti-Grain Geometry）](http://antigrain.com/)引擎的高质量图像。 |
| PS | [ps](https://matplotlib.org/glossary/index.html#term-ps)[eps](https://matplotlib.org/glossary/index.html#term-eps) | [vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics)--[Postscript](https://en.wikipedia.org/wiki/PostScript)output |
| PDF | [pdf](https://matplotlib.org/glossary/index.html#term-pdf) | [vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics)--[Portable Document Format](https://en.wikipedia.org/wiki/Portable_Document_Format) |
| SVG | [svg](https://matplotlib.org/glossary/index.html#term-svg) | [vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics)--[Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) |
| [Cairo](https://matplotlib.org/glossary/index.html#term-cairo) | [png](https://matplotlib.org/glossary/index.html#term-png)[ps](https://matplotlib.org/glossary/index.html#term-ps)[pdf](https://matplotlib.org/glossary/index.html#term-pdf)[svg](https://matplotlib.org/glossary/index.html#term-svg) | [raster graphics](https://matplotlib.org/glossary/index.html#term-raster-graphics)和[vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics)-- 使用[Cairo图形库\(Cairo graphics\)](https://www.cairographics.org/)库 |



