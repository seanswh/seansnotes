使用纹理

我们需要告知OPENGL如何对纹理图片进行采样，因此我们需要使用**纹理坐标来**更新**顶点数据\(vertex data\)**：

```
GLfloat vertices[] = {
// ---- 位置 ----      ---- 颜色 ----     - 纹理坐标 -
0.5f,  0.5f, 0.0f,   1.0f, 0.0f, 0.0f,   1.0f, 1.0f,   // 右上
0.5f, -0.5f, 0.0f,   0.0f, 1.0f, 0.0f,   1.0f, 0.0f,   // 右下
-0.5f, -0.5f, 0.0f,   0.0f, 0.0f, 1.0f,   0.0f, 0.0f,  // 左下
-0.5f,  0.5f, 0.0f,   1.0f, 1.0f, 0.0f,   0.0f, 1.0f   // 左上
};
```

上面的顶点数据中增加了一个顶点属性，因此我们需要再一次通知OPENGL顶点数据中的结构，更新后的定点数据结构如下图所示:

![](/OPENGL/images/vertex_attribute_pointer_interleaved_textures.png)

`glVertexAttribPointer(2,2, GL_FLOAT,GL_FALSE,8*sizeof(GLfloat), (GLvoid*)(6*sizeof(GLfloat))); glEnableVertexAttribArray(2);`

注意，这里的步长变成了8\*sizeof\(GLfloat\),而该属性所在的偏移为距离开头6个float位置。

接下来，我们会调整顶点着色器以接受纹理坐标作为顶点属性，然后将这个坐标传递给片元着色器：

```
#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;
layout (location = 2) in vec2 texCoord;

out vec3 ourColor;
out vec2 TexCoord;

void main()
{
    gl_Position = vec4(position, 1.0f);
    ourColor = color;
    TexCoord = texCoord;
}
```

片段着色器应该把输出变量`TexCoord`作为输入变量。

片段着色器也应该能访问纹理对象，但是我们怎样能把纹理对象传给片段着色器呢？GLSL有一个供纹理对象使用的内建数据类型，叫做采样器\(Sampler\)，它以纹理类型作为后缀，比如`sampler1D`、`sampler3D`，或在我们的例子中使用`sampler2D`。我们可以简单声明一个`uniform sampler2D`把一个纹理添加到片段着色器中，稍后我们会把纹理赋值给这个uniform。

```
#version 330 core

in vec3 ourColor;
in vec2 TexCoord;
out vec4 color;

uniform sampler2D ourTexture;

void main()
{
    color = texture(ourTexture, TexCoord);
}
```

我们使用GLSL内建的texture函数来采样纹理的颜色，它第一个参数是纹理采样器，第二个参数是对应的纹理坐标。

texture函数会使用之前设置的纹理参数对相应的颜色值进行采样。这个片段着色器的输出就是纹理图片在（插值）纹理坐标上的\(过滤后的\)颜色。

现在只剩下在调用glDrawElements之前绑定纹理了，它会自动把纹理赋值给片段着色器的采样器：

```
glBindTexture(GL_TEXTURE_2D, texture);
glBindVertexArray(VAO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
glBindVertexArray(0);
```

我们还可以把得到的纹理颜色与顶点颜色混合，来获得更有趣的效果。我们只需把纹理颜色与顶点颜色在片段着色器中相乘来混合二者的颜色：

```
color = texture(ourTexture, TexCoord) * vec4(ourColor,1.0f);
```

最终的效果应该是顶点颜色和纹理颜色的混合色。

片段着色器中使用了uniform sampler2D变量，但是我们没有使用glUniform函数赋值。如果我们想在一个片元着色器中设置多个纹理，我们可以通过使用glUniform1i函数，给纹理采样器\(sampler\)分配一个位置值.一个纹理的位置值通常称为一个纹理单元\(Texture Unit\)。一个纹理的默认纹理单元是0，且它是默认的激活纹理单元，所以我们没有分配位置值。

纹理单元的主要目的是让我们可以在一个纹理着色器中使用多个纹理，通过把纹理单元赋值给采样器，我们可以一次绑定多个纹理，只要我们使用时激活对应的纹理即可，就像glBindTexture一样，我们使用glActiveTexture激活纹理单元，传入我们需要使用的纹理单元：

```
glActiveTexture(GL_TEXTURE0); //在绑定纹理之前先激活纹理单元
glBindTexture(GL_TEXTURE_2D, texture);
```

激活纹理单元之后，接下来的glBindTexture函数调用会绑定这个纹理到被激活的纹理单元，由于纹理单元GL\_TEXTURE0默认总是被激活状态，所以我们在前面使用`glBindTexture`的时候，无需激活任何纹理单元。



