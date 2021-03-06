### 镜面光照

冯氏光照\(Phong Lighting Model\)模型的最后一项是镜面光照。

与漫反射光照类似，镜面光照计算也是基于片元的法向量以及光线方向，同时，还依赖于观察的视线方向。镜面光照依赖于光的反射特性。如果我们希望物体表面像镜子一样，我们不论在哪看，镜面反射的光照都是最强的。如下图所示：

![](/OPENGL/images/basic_lighting_specular_theory.png)

我们首先通过法向量计算反射方向，然后我们计算视线角度与反射方向之间的夹角，夹角越小，反射光的强度越强。

计算镜面反射需要视角向量，我们可以用观察者的世界坐标以及片元的世界坐标来求得。然后我们计算反射面的密度乘以光线颜色，最后加上环境光和漫反射即可。下面的代码完成了这件事：

```
float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
vec3 specular = specularStrength * spec * lightColor;
```



