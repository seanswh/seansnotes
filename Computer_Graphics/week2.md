1.坐标系
一般我们得到的物体是在模型坐标系下的，我们现在把物体切换到世界坐标系。
点和物体模型用向量表示，他们通过乘不同的矩阵来实现变换的目的：
一般变换有三种：旋转、缩放和错切
（1）缩放矩阵：
$$
\left\{
  \begin{matrix}
   s_x&0&0\\
   0&s_y&0\\
   0&0&s_z
  \end{matrix}
\right\}
$$
缩放矩阵是一个对角矩阵，逆操作就是各个参数的倒数
（2）错切：
通过错切可将矩形变成一个平行四边形
![](/Computer_Graphics/images/1.png)
如上图所示，中心线没有移动，上下两边分别在x方向上移动了距离a，而y方向保持不变。因此矩阵的第二行仍然为[0 1],矩阵的第一行，$$x'=x+ay$$,因此第一行为[1 a]，逆变换就是把a换成-a
(3)旋转：
旋转变换像其它变换一样也是矩阵。该矩阵使得X方向和Y方向的变换叠加，相当于先在X方向旋转再在Y方向旋转，接下来的问题是，二维旋转矩阵是什么样子的？
用极坐标来表示非常简单。假设p的X坐标等于某个半径r乘以cos(alpha)，这个角度就等于alpha。相应的Y坐标等于r乘以sin(alpha)。那么p'等于多少呢？对于p’这个组合起来的角度等于alpha + theta。因此p'的X坐标等r乘以cos(alpha+thata)，相应的Y坐标等于r乘以sin(alpha+thata)。这就是p'的位置。为了放到笛卡尔坐标系下，我们需要使用标准的三角公式展开cos(alpha+theta)和sin(alpha+theta)，因此cos(alpha+theta）= cos(alpha)cos(theta)-sin(alpha)sin(theta)而sin(alpha + theta) = sin(alpha)cos(theta) + cos(alpha)sin(theta)。首先看一下X坐标，P'的X坐标值公式里的r*cos(alpha)和r*sin(alpha)这两项。你会注意到r*cos(alpha)正是P点的X坐标，而r*sin(alpha)正好是P点的Y坐标。因此p_x'可以写成x*cos(theta) - *sin(theta)。综上所述，x' = x*cos(theta) - y*sin(theta)。同理，对 y'做相似的推导你会发现，y' = y*cos(theta) + x*sin(theta)。 上面讲到的都是二维旋转，
这个矩阵控制二维旋转变换。