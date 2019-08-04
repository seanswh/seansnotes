[https://learnopengl-cn.readthedocs.io/zh/latest/02%20Lighting/03%20Materials/](https://learnopengl-cn.readthedocs.io/zh/latest/02%20Lighting/03%20Materials/)

真实世界中，每个物体对光的反应都不同，钢看起来比陶瓷花瓶更闪闪发光，一个木头箱子不会像钢箱子一样对光产生很强的反射。每个物体对镜面高光也有不同的反应。有些物体不会散射\(Scatter\)很多光却会反射\(Reflect\)很多光，结果看起来就有一个较小的高光点\(Highlight\)，有些物体散射了很多，它们就会产生一个半径更大的高光。如果我们想要在OpenGL中模拟多种类型的物体，我们必须为每个物体分别定义材质\(Material\)属性。

