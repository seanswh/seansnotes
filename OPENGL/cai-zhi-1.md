[https://learnopengl-cn.readthedocs.io/zh/latest/02%20Lighting/03%20Materials/](https://learnopengl-cn.readthedocs.io/zh/latest/02 Lighting/03 Materials/)

真实世界中，每个物体对光的反应都不同，钢看起来比陶瓷花瓶更闪闪发光，一个木头箱子不会像钢箱子一样对光产生很强的反射。每个物体对镜面高光也有不同的反应。有些物体不会散射\(Scatter\)很多光却会反射\(Reflect\)很多光，结果看起来就有一个较小的高光点\(Highlight\)，有些物体散射了很多，它们就会产生一个半径更大的高光。如果我们想要在OpenGL中模拟多种类型的物体，我们必须为每个物体分别定义材质\(Material\)属性。

当描述一个物体的颜色时，我们可以定义综合考虑环境光照颜色、漫反射光照以及镜面光照来定义该物体的光照颜色，通过对每一个片元定义颜色，我们可以对物体的颜色控制有了精确的输出。我们可以定义一个结构体，将镜面高光要素与上述三个颜色结合，来描述材质属性：

```
#version 330 core
struct Material
{
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;    
    float shininess;
};
uniform Material material;
```



