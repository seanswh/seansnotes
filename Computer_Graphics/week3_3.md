Ray Trace 3 相交计算

我们会讲解三角形、球与光线的求交。并会讲到多边形和一般的隐式曲面（implicit surface）与光线的求交。
1。球
![](/Computer_Graphics/images/48.png)
光线是这样定义的：有一个起点P0和方向P1，t是沿着光线的大于等于0的参数，对应于沿着光线的距离。球用球心位置C来定位，对于球表面上的任何点P，P - C 与它自己的点积等于r的平方，其中r是半径。而我们想求的是交点的坐标。
把光线方程代入球的方程。在这个例子中，P = P0 + P1*t。我把它代入球的方程中。即：P0 + P1 * t - C与自己的点积等于r的平方。
进行简化，一个简单的二次方程（如下图）用于求解t。
![](/Computer_Graphics/images/49.png)

    1.如果有2个正实根，意味着光线与球这样相交。在这种情况下，选择小的正实根。
    2.如果两个根相同，意味着光线与球仅相交一次即光线与球相切。
    3.如果有1正1负两个根，意味着光线起点在球里，负根对应这个交点，正根是这个交点。在这种情况下，选择正根，因为光线的参数t不会小于0。
    4.如果有复根，意味着光线与球没有交点。
你应该确定判别式非负。最终你通过求解方程得到交点的参数t值。然后你需要找到真正的交点坐标。把求得的t代回方程 P0 + P1 * t，你可能还需要知道交点的法向，在球的例子中，你知道球表面某点的法向是从球心指向该点的方向，即 P - C，进行归一化。
2。三角形
让我们先考虑这样的一个三角形，三角形的三个顶点是A，B和C。如果需要计算法线，计算方法为：三角形中的任意两个方向，如 C - A 和 B - A，法向可以由 (C - A)×(B - A) 得到，![](/Computer_Graphics/images/50.png)

法向和平面中任何向量的点积为0。所以，如果你考虑平面上的点P，P可以是三角形中任何一点，这里是P，然后你考虑向量P减A，它在平面上，法向与它的点积为0，即：n·(P - A)= 0，即P·n - A·n= 0。光线是P0 + P1 * t。我们把它代入平面方程，即： (P0 + P1 * t)·n = A·n，求t即可得到交点，你得到的t是：((A·n) - (P0·n)) / (P1·n)。注意如果 P1·n = 0，则没有意义，说明光线与平面平行，这种情况下当然不相交。
问题刚解决了一半，你还需要判断交点是否在三角形内。有很多种判断方法，可以同时用于三角形和一般多边形。。一种方法是考虑一个这样的一般多边形，不需要多边形是凸的，在这儿有一个点，你不知道它是在里还是外，所以我从这个点向任何方向画一条线到无穷远，方向是什么无所谓，它可以朝这里，可以朝这里。如果射线与多边形相交了偶数次，则点在多边形外。如果相交奇数次，则点在多边形内部。
然而对于三角形，我们实际上采用参数的方法求交，即使用关于三角形顶点的重心坐标（barycentric coordinate）。如果我知道A，B，C是三角形的顶点，Alpha, beta, 和gamma 是点P相对于A，B和C的权重。它们被归一化了，即alpha + beta + gamma等于1.这就叫做三角形的重心坐标。点P可以通过 alpha A + beta B + gamma C 来表示，三个参数和为1，现在的问题是如何求解？这是个简单的联立方程组。
我可以用P减A （A=$$(\alpha+\beta+\gamma) A$$），得到 beta (B - A)+ gamma (C - A)
![](/Computer_Graphics/images/51.png)

