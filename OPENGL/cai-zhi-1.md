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

这里有一个列表[devernay.free.fr](http://devernay.free.fr/cours/opengl/materials.html)展示了几种材质属性，这些材质属性模拟外部世界的真实材质。

| Name | Ambient |  |  | Diffuse |  |  | Specular |  |  | shiness |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| emerald | 0.0215 | 0.1745 | 0.0215 | 0.07568 | 0.61424 | 0.07568 | 0.633 | 0.727811 | 0.633 | 0.6 |
| jade | 0.135 | 0.2225 | 0.1575 | 0.54 | 0.89 | 0.63 | 0.316228 | 0.316228 | 0.316228 | 0.1 |
| obsidian | 0.05375 | 0.05 | 0.06625 | 0.18275 | 0.17 | 0.22525 | 0.332741 | 0.328634 | 0.346435 | 0.3 |
| pearl | 0.25 | 0.20725 | 0.20725 | 1 | 0.829 | 0.829 | 0.296648 | 0.296648 | 0.296648 | 0.088 |
| ruby | 0.1745 | 0.01175 | 0.01175 | 0.61424 | 0.04136 | 0.04136 | 0.727811 | 0.626959 | 0.626959 | 0.6 |
| turquoise | 0.1 | 0.18725 | 0.1745 | 0.396 | 0.74151 | 0.69102 | 0.297254 | 0.30829 | 0.306678 | 0.1 |
| brass | 0.329412 | 0.223529 | 0.027451 | 0.780392 | 0.568627 | 0.113725 | 0.992157 | 0.941176 | 0.807843 | 0.21794872 |
| bronze | 0.2125 | 0.1275 | 0.054 | 0.714 | 0.4284 | 0.18144 | 0.393548 | 0.271906 | 0.166721 | 0.2 |
| chrome | 0.25 | 0.25 | 0.25 | 0.4 | 0.4 | 0.4 | 0.774597 | 0.774597 | 0.774597 | 0.6 |
| copper | 0.19125 | 0.0735 | 0.0225 | 0.7038 | 0.27048 | 0.0828 | 0.256777 | 0.137622 | 0.086014 | 0.1 |
| gold | 0.24725 | 0.1995 | 0.0745 | 0.75164 | 0.60648 | 0.22648 | 0.628281 | 0.555802 | 0.366065 | 0.4 |
| silver | 0.19225 | 0.19225 | 0.19225 | 0.50754 | 0.50754 | 0.50754 | 0.508273 | 0.508273 | 0.508273 | 0.4 |
| black plastic | 0.0 | 0.0 | 0.0 | 0.01 | 0.01 | 0.01 | 0.50 | 0.50 | 0.50 | .25 |
| cyan plastic | 0.0 | 0.1 | 0.06 | 0.0 | 0.50980392 | 0.50980392 | 0.50196078 | 0.50196078 | 0.50196078 | .25 |
| green plastic | 0.0 | 0.0 | 0.0 | 0.1 | 0.35 | 0.1 | 0.45 | 0.55 | 0.45 | .25 |
| red plastic | 0.0 | 0.0 | 0.0 | 0.5 | 0.0 | 0.0 | 0.7 | 0.6 | 0.6 | .25 |
| white plastic | 0.0 | 0.0 | 0.0 | 0.55 | 0.55 | 0.55 | 0.70 | 0.70 | 0.70 | .25 |
| yellow plastic | 0.0 | 0.0 | 0.0 | 0.5 | 0.5 | 0.0 | 0.60 | 0.60 | 0.50 | .25 |
| black rubber | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 | 0.4 | 0.4 | 0.4 | .078125 |
| cyan rubber | 0.0 | 0.05 | 0.05 | 0.4 | 0.5 | 0.5 | 0.04 | 0.7 | 0.7 | .078125 |
| green rubber | 0.0 | 0.05 | 0.0 | 0.4 | 0.5 | 0.4 | 0.04 | 0.7 | 0.04 | .078125 |
| red rubber | 0.05 | 0.0 | 0.0 | 0.5 | 0.4 | 0.4 | 0.7 | 0.04 | 0.04 | .078125 |
| white rubber | 0.05 | 0.05 | 0.05 | 0.5 | 0.5 | 0.5 | 0.7 | 0.7 | 0.7 | .078125 |
| yellow rubber | 0.05 | 0.05 | 0.0 | 0.5 | 0.5 | 0.4 | 0.7 | 0.7 | 0.04 | .078125 |

为一个物体赋予一款正确的材质是非常困难的，这需要大量实验和丰富的经验，所以由于错误的设置材质而毁了物体的画面质量是件经常发生的事。

有了物体的材质属性，我们修正一下物体的颜色，我们将光照颜色偏量与物体的各个属性颜色相乘，最后得到最终片元的颜色。

当给着色器中的结构体赋值时，一个结构体值扮演uniform变量的封装体，所以如果我们希望给这个结构体赋值，我们就仍然必须设置结构体中的各个元素的uniform值，但是这次带有结构体名字作为前缀：

```
GLint matAmbientLoc = glGetUniformLocation(lightingShader.Program, "material.ambient");
GLint matDiffuseLoc = glGetUniformLocation(lightingShader.Program, "material.diffuse");
GLint matSpecularLoc = glGetUniformLocation(lightingShader.Program, "material.specular");
GLint matShineLoc = glGetUniformLocation(lightingShader.Program, "material.shininess");
glUniform3f(matAmbientLoc, 1.0f, 0.5f, 0.31f);
glUniform3f(matDiffuseLoc, 1.0f, 0.5f, 0.31f);
glUniform3f(matSpecularLoc, 0.5f, 0.5f, 0.5f);
glUniform1f(matShineLoc, 32.0f);
```



