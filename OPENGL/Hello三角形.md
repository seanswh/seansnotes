1.顶点输入（准备工作）  
**注意：**OpenGL是一个3D图形库，所以我们在OpenGL中指定的所有坐标都是3D坐标（x、y和z）。OpenGL不是简单地把所有的3D坐标变换为屏幕上的2D像素；OpenGL仅当3D坐标在3个轴（x、y和z）上都为-1.0到1.0的范围内时才处理它。所有在所谓的标准化设备坐标\(Normalized Device Coordinates\)范围内的坐标才会最终呈现在屏幕上（在这个范围以外的坐标都不会显示）。  
一旦你的顶点坐标已经在顶点着色器中处理过，它们就应该是标准化设备坐标\(Normalized Device Coordinates, NDC\)了，标准化设备坐标是一个x、y和z值在-1.0到1.0的一小段空间。任何落在范围外的坐标都会被丢弃/裁剪，不会显示在你的屏幕上。通过glViewport中设置的参数进行视口变化（Viewport Transform），这些NDC坐标会被转化成屏幕空间坐标。

定义这样的顶点数据以后，我们会把它作为输入发送给图形渲染管线的第一个处理阶段：顶点着色器。它会在GPU上创建内存用于储存我们的顶点数据，还要配置OpenGL如何解释这些内存，并且指定其如何发送给显卡。顶点着色器接着会处理我们在内存中指定数量的顶点。

我们通过顶点缓冲对象\(Vertex Buffer Objects, VBO\)管理上述内存，它会在GPU内存\(通常被称为显存\)中储存大量顶点。使用这些缓冲对象的好处是我们可以一次性的发送一大批数据到显卡上，而不是每个顶点发送一次。从CPU把数据发送到显卡相对较慢，所以只要可能我们都要尝试尽量一次性发送尽可能多的数据。当数据发送至显卡的内存中后，顶点着色器几乎能立即访问顶点，这是个非常快的过程。

顶点缓冲对象是我们在OpenGL教程中第一个出现的OpenGL对象。就像OpenGL中的其它对象一样，这个缓冲有一个独一无二的ID，所以我们可以使用glGenBuffers函数和一个缓冲ID生成一个VBO对象：

`unsigned int VBO;`

`glGenBuffers(1, &VBO);`

OpenGL有很多缓冲对象类型，顶点缓冲对象的缓冲类型是GL\_ARRAY\_BUFFER。OpenGL允许我们同时绑定多个缓冲，只要它们是不同的缓冲类型，**每一个类型的缓冲绑定一次**。我们可以使用glBindBuffer函数把新创建的缓冲绑定到GL\_ARRAY\_BUFFER目标上

`glBindBuffer(GL_ARRAY_BUFFER, VBO);`

从这一刻起，**我们使用的任何GL\_ARRAY\_BUFFER缓冲调用都会用来配置当前绑定的缓冲\(VBO\)**。然后我们可以调用glBufferData函数，它会把之前定义的顶点数据复制到缓冲的内存中（从内存到显存）：

`glBufferData(GL_ARRAY_BUFFER,sizeof(vertices), vertices, GL_STATIC_DRAW);`

现在我们已经把顶点数据储存在**显存中**了，同时用刚定义好的VBO对象进行了绑定。

下面我们会创建一个顶点和片段着色器来真正处理这些数据。

2。 顶点着色器

如果我们打算做渲染的话，现代OpenGL需要我们至少设置一个顶点以及一个片段着色器，因此顶点着色器\(vertex shadex\)是我们要编写的第一个着色器。

我们需要做的第一件事是用着色器语言GLSL\(OpenGL Shading Language\)编写顶点着色器，然后编译这个着色器，这样我们就可以在程序中使用它了。

为了设置顶点着色器的输出，我们必须把位置数据赋值给预定义的gl\_Position变量，它是内置的`vec4`类型的。在顶点着色器中main函数的最后，我们将gl\_Position设置的值会成为该顶点着色器的输出。在真实的程序里输入数据通常都不是标准化设备坐标，所以我们首先必须先把它们转换至OpenGL的可视区域内。

3.编译着色器

顶点着色器源码存在一个类C语言的字符串中，为了能够让OpenGL使用它，我们必须在运行时动态编译它的源码。

编译的第一步是调用glCreateShader函数创建一个着色器对象（shader object）,注意还是用ID\(GLunit类型\)来引用的。

`unsigned int vertexShader;`

`vertexShader = glCreateShader(GL_VERTEX_SHADER);`

下一步我们把这个着色器源码附加到着色器对象上，然后编译它：

`glShaderSource(vertexShader,1, &vertexShaderSource, NULL);`

`glCompileShader(vertexShader);`

4.片段着色器\(fragment shader\)

片段着色器的全部工作就是计算像素的颜色。片段着色器只需要一个输出变量，这个变量是一个4分量向量，它表示的是最终的输出颜色。编译片段着色器的过程与顶点着色器类似，只不过我们使用GL\_FRAGMENT\_SHADER常量作为着色器类型：

`GLuint fragmentShader;`

`fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);`

`glShaderSource(fragmentShader,1, &fragmentShaderSource, null);`

`glCompileShader(fragmentShader);`

5.着色器程序

两个着色器现在都编译了，剩下的事情是把两个着色器对象链接到一个用来渲染的着色器程序\(Shader Program\)中。着色器程序对象\(Shader Program Object\)是多个着色器合并之后并最终链接完成的版本。如果要使用刚才编译的着色器我们必须把它们链接为一个着色器程序对象，然后在渲染对象的时候激活这个着色器程序。当链接着色器至一个程序的时候，它会把每个着色器的输出链接到下个着色器的输入。当输出和输入不匹配的时候，你会得到一个连接错误。创建一个程序对象很简单：

```
GLuint shaderProgram;
shaderProgram = glCreateProgram();
```

glCreateProgram函数创建一个程序，并返回新创建程序对象的ID引用。现在我们需要把之前编译的着色器附加到程序对象上，然后用glLinkProgram链接它们：

```
glAttachShader(shaderProgram, vertexShader);
glAttachShader(shaderProgram, fragmentShader);
glLinkProgram(shaderProgram);
```

得到的结果就是一个程序对象，我们可以调用glUseProgram函数，用刚创建的程序对象作为它的参数，以激活这个程序对象：

```
glUseProgram(shaderProgram);
```

在glUseProgram函数执行之后的着色器调用和渲染调用都会使用这个程序对象（也就是之前写的着色器\)了。对了，**在把着色器对象链接到程序对象以后，记得删除着色器对象**，我们不再需要它们了：

```
glDeleteShader(vertexShader);
glDeleteShader(fragmentShader);
```

现在，我们已经把输入顶点数据发送给了GPU，并指示了GPU如何在顶点和片段着色器中处理它。

