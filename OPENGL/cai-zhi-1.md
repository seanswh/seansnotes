[https://learnopengl-cn.readthedocs.io/zh/latest/02%20Lighting/03%20Materials/](https://learnopengl-cn.readthedocs.io/zh/latest/02 Lighting/03 Materials/)

真实世界中，每个物体对光的反应都不同，钢看起来比陶瓷花瓶更闪闪发光，一个木头箱子不会像钢箱子一样对光产生很强的反射。每个物体对镜面高光也有不同的反应。有些物体不会散射\(Scatter\)很多光却会反射\(Reflect\)很多光，结果看起来就有一个较小的高光点\(Highlight\)，有些物体散射了很多，它们就会产生一个半径更大的高光。如果我们想要在OpenGL中模拟多种类型的物体，我们必须为每个物体分别定义材质\(Material\)属性。

当描述一个物体的颜色时，我们可以定义综合考虑环境光照颜色、漫反射光照以及镜面光照来定义该物体的光照颜色，通过对每一个片元定义颜色，我们可以对物体的颜色控制有了精确的输出。我们可以定义一个结构体，将镜面高光要素与上述三个材质颜色结合，来描述材质属性：

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

在**片段着色器**中，我们创建一个结构体\(Struct\)，来储存物体的**材质属性。**`ambient`材质向量定义了在环境光照下这个物体反射的是什么颜色；通常这是和物体颜色相同的颜色。`diffuse`材质向量定义了在漫反射光照下物体的颜色。漫反射颜色被设置为\(和环境光照一样\)我们需要的物体颜色。`specular`材质向量设置的是物体受到的镜面光照的影响的颜色\(或者可能是反射一个物体特定的镜面高光颜色\)。最后，`shininess`影响镜面高光的散射/半径。

