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



