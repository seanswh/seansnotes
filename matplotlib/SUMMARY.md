所有的绘制函数都支持np.array或者np.ma.masked\_array作为输入，一些“数组类型”的类如pandas数据对象或者np.matrix可能会无法正常显示，如果需要使用，最好将上述类型转换成np.array类型

**Matplotlib, pyplot and pylab之间的关系**:**Matplotlib**是整个包，**pyplot**是绘制模块。在pyplot模块中，总会有一个“当前”\(current\)的figure和axes

```
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()
```

上述代码中，第一次调用plot函数的时候会创建一个axes，后续的plot调用都会在当前的axes中进行叠加绘制，xlabel,ylabel,title,legend都是在当前的axes中进行叠加绘制

**pylab**是一个快捷模块，将pyplot和numpy模块一次性的import进来，由于命名空间污染等问题，**不建议使用pylab模块**

对于非交互式绘图，建议使用pyplot创建图形（figure），然后使用类对象的方式进行绘图。

为了避免不必要的麻烦，建议按照一下方式引用模块：

```
import matplotlib.pyplot as plt
import numpy as np
```



