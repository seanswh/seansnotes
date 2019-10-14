EBO\(Element Buffer Object\)  
EBO主要用在不同物体之间有很多重叠的顶点时，如果不使用EBO，则每个顶点都要存储，这样会有很多的地址冗余和空间浪费。EBO的思想是，使用VBO存储所有的顶点，但是EBO存储每一个物体的顶点索引顺序。  
与VBO一样，EBO也是一个缓冲，只不过存储的是索引。  
创建索引缓冲对象：

`GLuint EBO;              
glGenBuffers(1, &EBO);`

与VBO类似，首先绑定EBO，然后用glBufferData把索引复制到缓冲里。和VBO类似，我们会把这些函数调用放在绑定和解绑函数调用之间，只不过这次我们把缓冲的类型定义为GL\_ELEMENT\_ARRAY\_BUFFER。

```
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
```

最后一件要做的事是用glDrawElements来替换glDrawArrays函数，来指明我们从索引缓冲渲染。使用glDrawElements时，我们会使用当前绑定的索引缓冲对象中的索引进行绘制：

```
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
```

第一个参数指定了我们绘制的模式，这个和glDrawArrays的一样。第二个参数是我们打算绘制顶点的个数，这里填6，也就是说我们一共需要绘制6个顶点。第三个参数是索引的类型，这里是GL\_UNSIGNED\_INT。最后一个参数里我们可以指定EBO中的偏移量（或者传递一个索引数组，但是这是当你不在使用索引缓冲对象的时候），但是我们会在这里填写0。

glDrawElements函数从当前绑定到GL\_ELEMENT\_ARRAY\_BUFFER目标的EBO中获取索引。这意味着我们必须在每次要用索引渲染一个物体时都要绑定相应的EBO，这还是有点麻烦。不过顶点数组对象\(VAO\)同样可以保存索引缓冲对象\(EBO\)的绑定状态。VAO绑定时正在绑定的索引缓冲对象会被保存为VAO的元素缓冲对象。绑定VAO的同时也会自动绑定EBO。

VAO的结构图会变成这样：

![](/OPENGL/images/vertex_array_objects_ebo.png)

这个图也就类似成为上一篇中结构体的真实样子了。

当目标是GL\_ELEMENT\_ARRAY\_BUFFER的时候，VAO会储存glBindBuffer的函数调用。这也意味着它也会**储存解绑调用**，所以在解绑VAO之前一定不要解绑EBO，否则它就没有这个EBO配置了。

最后，代码看起来类似于这样：

最后的初始化和绘制代码现在看起来像这样：

```
// ..:: 初始化代码 :: ..
// 1. 绑定顶点数组对象
glBindVertexArray(VAO);    
// 2. 把我们的顶点数组复制到一个顶点缓冲中，供OpenGL使用
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);    
// 3. 复制我们的索引数组到一个索引缓冲中，供OpenGL使用
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);    
// 3. 设定顶点属性指针
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0);
    glEnableVertexAttribArray(0);
// 4. 解绑VAO（不是EBO！）
glBindVertexArray(0);
[...]
// ..:: 绘制代码（游戏循环中） :: ..
glUseProgram(shaderProgram);
glBindVertexArray(VAO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
glBindVertexArray(0);
```



