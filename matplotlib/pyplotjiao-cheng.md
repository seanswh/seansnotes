[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)是使matplotlib像MATLAB一样工作的命令函数的集合。每一个pyplot函数都会对figure对象进行修改，比如创建一个figure，创建plot area，在plot area中绘制一些线条，在plot上进行一些标注等等。

在pyplot中，各个函数调用之间，状态是会被保留的，这样就能跟踪当前图像\(figure\)和绘图区的状态了，而且每一个绘图操作都会直接执行到当前的轴\(current axes\)上。（这个axes是figure中的绘图区，不是axis的复数）

注意： pyplot直接调用的API函数通常不如面向对象的API灵活。

### 多个figure与Axes之间进行绘制

pyplot有当前figure或者当前Axes的概念，所有的绘图操作都是对当前axes操作，可以通过gca函数返回当前的axes（是一个matplotlib.axes.Axes的实例），gcf函数返回当前figure\(matplotlib.figure.Figure实例）。

