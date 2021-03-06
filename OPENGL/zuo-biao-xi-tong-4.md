### To Sum Up

我们为上述的每一个步骤都创建了一个转换矩阵：模型矩阵、观察矩阵和投影矩阵。一个顶点的坐标将会根据以下过程被转换到裁剪坐标：

Vclip=Mprojection⋅Mview⋅Mmodel⋅Vlocal

注意每个矩阵被运算的顺序是相反的\(记住我们需要从右往左乘上每个矩阵\)。计算的结果会赋值给顶点着色器的gl\_position变量，而OPENGL会自动执行透视划分和裁剪。

> 顶点着色器的输出保证所有的顶点坐标都在裁剪空间之内，这也是我们变换矩阵所做的。OPENGL随后会使用透视划分的方法将裁剪空间内的坐标转换成NDC坐标，然后使用glViewPort函数及其参数，将NDC坐标转换成屏幕坐标，这个过程叫做视口变换。

### 3D例子

1.第一步，我们先创建一个模型矩阵，这个模型矩阵包含了移动、缩放、旋转。可以将我们的对象顶点变换到全局世界空间中。我们可以尝试把这个平面通过x轴旋转一下，创建出了一个模型矩阵：

```
glm::mat4 model;
model = glm::rotate(model, -55.0f, glm::vec3(1.0f, 0.0f, 0.0f));
```

通过将顶点坐标乘以这个模型矩阵我们将该顶点坐标转换到世界坐标。我们的平面模拟世界场景下的地板~~

2.我们创建一个视图矩阵，我们想要稍微向后移动一下视角，这样我们的对象就变得可见了\(因为在世界坐标系下，我们现在还在0,0,0这个位置上\)。我们可以将物体按照相反的方向移动，也就是将物体向前移动一下。

因为OPENGL中的坐标轴符合右手定理，因此将整个场景向前移动，也就是朝着Z轴的负值方向移动。代码中我们的视图矩阵是这样的：

```
glm::mat4 view;

// 注意，我们将矩阵向我们要进行移动场景的反向移动。

view = glm::translate(view, glm::vec3(0.0f, 0.0f, -3.0f));
```

3.最后，我们定义投影矩阵，我们想使用透视投影，因此我们声明的投影矩阵如下段代码所示：

```
glm::mat4 projection;
projection = glm::perspective(45.0f, screenWidth / screenHeight, 0.1f, 100.0f);
```

4.我们将定义好的一系列变换矩阵传递到我们的着色器中，首先我们在顶点着色器中定义uniform的变换矩阵，然后传递进去，最后将它们乘以顶点坐标：

```
#version 330 core

layout (location = 0) in vec3 position;
...
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    // 注意从右向左读
    gl_Position = projection * view * model * vec4(position, 1.0f);
    ...
}
```

变换矩阵一般都在每次渲染的时候传递到着色器中：

```
GLint modelLoc = glGetUniformLocation(ourShader.Program, "model");
glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm::value_ptr(model));
... 
// 观察矩阵和投影矩阵与之类似
```



