还有一个问题，就是光源的每一个偏量其实强度时不同的，比如从光源的位置到物体，环境光的强度应该很小，漫反射光的强度也不应该与环境光相同，因此我们需要一个新的结构体来调整：

```
struct Light
{
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};
uniform Light light;
```

一个光源的`ambient`、`diffuse`和`specular`光都有不同的亮度。环境光通常设置为一个比较低的亮度，因为我们不希望环境色太过显眼。光源的`diffuse`元素通常设置为我们希望光所具有的颜色；经常是一个明亮的白色。`specular`元素通常被设置为`vec3(1.0f)`类型的全强度发光。

