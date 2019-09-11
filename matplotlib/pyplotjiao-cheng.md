[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)是使matplotlib像MATLAB一样工作的命令函数的集合。每一个pyplot函数都会对figure对象进行修改，比如创建一个figure，创建plot area，在plot area中绘制一些线条，在plot上进行一些标注等等。

在pyplot中，各个函数调用之间，状态是会被保留的，这样就能跟踪当前图像\(figure\)和绘图区的状态了，而且每一个绘图操作都会直接执行到当前的轴\(current axes\)上。（这个axes是figure中的绘图区，不是axis的复数）

注意： pyplot直接调用的API函数通常不如面向对象的API灵活。

### 多个figure与Axes之间进行绘制

pyplot有当前figure或者当前Axes的概念，所有的绘图操作都是对当前axes操作，可以通过gca函数返回当前的axes（是一个matplotlib.axes.Axes的实例），gcf函数返回当前figure\(matplotlib.figure.Figure实例）。

```
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```

[figure\(\)](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure)命令可以不写，因为默认情况下将pyplot会创建`figure(1)`，就像默认情况下创建`subplot(111)`一样。[subplot\(\)](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot)命令指定`numrows`,`numcols`,`plot_number`，其中`plot_number`的范围`从1到numrows*numcols`。如果`numrows * numcols <10`，则subplot命令中的逗号是可选的。因此`subplot(211)`与`subplot(2, 1, 1)`相同。

可以创建任意数量的子图和轴。如果要手动放置轴，即不在矩形网格上，请使用 axes\(\) 命令，该命令允许您将位置指定为`axes([left，bottom，width，height])`，其中所有值均为小数（0到1）坐标。

可以使用

[clf\(\)](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf)

清除当前图形，使用

[cla\(\)](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.cla.html#matplotlib.pyplot.cla)

清除当前轴

