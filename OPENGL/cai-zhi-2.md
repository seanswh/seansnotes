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



