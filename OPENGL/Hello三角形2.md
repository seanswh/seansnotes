还没结束，OpenGL还不知道它该如何解释显存中的顶点数据，以及它该如何将顶点数据链接到顶点着色器的属性上。我们需要告诉OpenGL怎么做

1。链接顶点属性

顶点着色器允许我们指定任何格式来输入顶点属性，因此我们必须必须在渲染前指定输入数据的哪一个部分对应顶点着色器的哪一个顶点属性。

比如我们自定义的顶点数据组织如下：

![](/OPENGL/images/vertex_attribute_pointer.png)

自定义的顶点数据满足以下定义：

位置数据被储存为32-bit（4字节）浮点值。每个位置包含3个这样的值。在这3个值之间没有空隙（或其他值）。这几个值在数组中紧密排列。数据中第一个值在缓冲开始的位置。

如何把上述信息传递给OPENGL，从而对该内存进行有效解析——使用glVertexAttribPointer函数

```
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0);
glEnableVertexAttribArray(0);
```

第一个参数指定我们要配置的顶点属性。我们在顶点着色器中使用`layout(location = 0)`定义了position顶点属性的位置值\(Location\)，这里这个参数也为0 ，代表当前数据段中的数据是给顶点着色器中的position属性的。

第二个参数指明了该属性的大小，由于在顶点着色器中position属性是vec3，因此这里是3个连续的变量。

第三个参数指定了要素类型，GL\_FLOAT表明了类型为float

第四个参数标识是否需要将原始数据**标准化，**如果我们设置为GL\_TRUE，所有数据都会被映射到0（对于有符号型signed数据是-1）到1之间。

第五个参数是**步长，**也就是连续两个定点之间的间隔，如上图所示：每一个定点都有XYZ三个分量，每个分量都是一个float，因此此处值为：3 \* sizeof\(GLfloat\)。要注意的是由于我们知道这个数组是紧密排列的（如上图所示，在两个顶点的position属性之间没有空隙）我们也可以设置为0来让OpenGL决定具体步长是多少（只有当数值是紧密排列时才可用）。一旦我们有更多的顶点属性，我们就必须更小心地定义每个顶点属性之间的间隔。这个参数的意思简单说就是从这个position属性第二次出现的地方到整个数组0位置之间有多少字节。

最后一个参数是**偏移，**意思是当前属性\(position\)在整个数据段中起始位置的偏移，因为当前属性\(position\)是从整个数据的起始位置开始，因此这里赋值为GLVoid\*.

> **注意：**所有的顶点属性均从VBO通过GL\_ARRAY\_BUFFER绑定的显存数据中来，这个绑定是在调用glVetexAttribPointer函数前确定的，因此顶点属性0会关联到顶点数据上。

现在我们已经指明了OPENGL如何解析顶点数据，我们就可以调用glEnableVertexAttribArray来应用这个属性了，参数是该属性的位置值\(当前为0，也是glVertexAttribPointer的第一个参数\)，默认情况下属性是被禁用的。

至此，所有的设置都做完了，我们把顶点数据放在了VBO\(顶点缓冲区对象\)中，设置了顶点和片段着色器，也告诉OPENGL如何把顶点属性与顶点数据关联起来了。现在就可以像下面代码这样绘制了：

```
// 0. 复制顶点数组到缓冲中供OpenGL使用
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
// 1. 设置顶点属性指针
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0);
glEnableVertexAttribArray(0);
// 2. 当我们渲染一个物体时要使用着色器程序
glUseProgram(shaderProgram);
// 3. 绘制物体
someOpenGLFunctionThatDrawsOurTriangle();
```



