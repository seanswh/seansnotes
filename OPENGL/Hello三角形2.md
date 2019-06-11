还没结束，OpenGL还不知道它该如何解释显存中的顶点数据，以及它该如何将顶点数据链接到顶点着色器的属性上。我们需要告诉OpenGL怎么做

1。链接顶点属性

顶点着色器允许我们指定任何格式来输入顶点属性，因此我们必须必须在渲染前指定输入数据的哪一个部分对应顶点着色器的哪一个顶点属性。

比如我们自定义的定点数据组织如下：

![](/OPENGL/images/vertex_attribute_pointer.png)

自定义的顶点数据满足以下定义：

位置数据被储存为32-bit（4字节）浮点值。每个位置包含3个这样的值。在这3个值之间没有空隙（或其他值）。这几个值在数组中紧密排列。数据中第一个值在缓冲开始的位置。

如何把上述信息传递给OPENGL，从而对该内存进行有效解析——使用glVertexAttribPointer函数

```
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0);
glEnableVertexAttribArray(0);
```

第一个参数指定我们要配置的顶点属性。我们在顶点着色器中使用`layout(location = 0)`定义了position顶点属性的位置值\(Location\)，这里这个参数也为0 ，代表当前数据段中的数据是给顶点着色器中的position属性的。

