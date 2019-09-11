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

注意：后端名称大小写不敏感，比如'GTK3Agg' and 'gtk3agg'是等效的。

注：上述的第三种方式是目前MICAPS4工具箱显示matplotlib结果的实现方式。

