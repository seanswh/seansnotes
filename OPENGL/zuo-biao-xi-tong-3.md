### 正交投影

正射投影\(Orthographic Projection\)矩阵定义了一个类似立方体的平截头体，指定了一个裁剪空间，每一个在这空间外面的顶点都会被裁剪。创建一个正射投影矩阵需要指定可见平截头体的宽、高和长度。所有在使用正射投影矩阵转换到裁剪空间后如果还处于这个平截头体里面的坐标就不会被裁剪。它的平截头体看起来像一个容器：![](/OPENGL/images/orthographic_frustum.png)

![](/OPENGL/images/orthographic_frustum.png)

