为了能够把纹理映射\(Map\)到三角形上，我们需要指定三角形的每个顶点各自对应纹理的哪个部分。这样每个顶点就会关联着一个纹理坐标\(Texture Coordinate\)，用来标明该从纹理图像的哪个部分采样（译注：采集片段颜色）。三角形的其它片段上可以通过片段插值\(Fragment Interpolation\)来获得相应的颜色。

![](/assets/tex_coords.png)

无论在x还是y轴上，纹理坐标范围都为0到1之间（注意我们使用的是2D纹理图像）。使用纹理坐标获取纹理颜色的过程叫做采样\(Sampling\)。上图展示了如何把纹理到三角形上，纹理坐标左下角是\(0,0\),右上角是\(1,1\)。

我们希望三角形的左下角用纹理的左下角，因此三角形左下角的纹理坐标为\(0,0\)；三角形的顶点为纹理上部中间的点，因此我们用\(0.5,1\)，右下角使用纹理的右下角，所以纹理坐标为\(1,0\)。我们只需要把这**3个纹理坐标传递给顶点着色器**中，随后在片元着色器中会为每个片元进行纹理坐标的插值。

纹理坐标看起来就像这样：

```
GLfloat texCoords[] = {

0.0f, 0.0f, // 左下角
1.0f, 0.0f, // 右下角
0.5f, 1.0f// 上中
};
```

随后，我们需要告诉OpenGL该怎样对纹理**采样**。

1.纹理环绕方式

当纹理坐标超出了\(0,0\)到\(1,1\)值域区间以后，OPENGL默认会重复继续使用纹理图像，初次之外，我们还可以指定如下参数进行相应的处理：

| 环绕方式\(Wrapping\) | 描述 |
| :---: | :---: |
| GL\_REPEAT | 对纹理的默认行为。重复纹理图像。 |
| GL\_MIRRORED\_REPEAT | 和GL\_REPEAT一样，但每次重复图片是镜像放置的。 |
| GL\_CLAMP\_TO\_EDGE | 纹理坐标会被约束在0到1之间，超出的部分会重复纹理坐标的边缘，产生一种边缘被拉伸的效果。 |
| GL\_CLAMP\_TO\_BORDER | 超出的坐标为用户指定的边缘颜色。 |

当纹理坐标超出默认范围时，每个选项都有不同的视觉效果输出。我们来看看这些纹理图像的例子：

![](/assets/texture_wrapping.png)

上述的每一个环绕参数都可通过glTexParameter\*函数对指定的坐标轴来分别设置，\(s,t,r对应x,y,z轴\)：

```
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT);
```

第一个参数指定了纹理目标；我们使用的是2D纹理，因此纹理目标是GL\_TEXTURE\_2D。第二个参数需要我们指定设置的选项与应用的纹理轴。我们打算配置的是`WRAP`选项，并且指定`S`和`T`轴。最后一个参数需要我们传递一个环绕方式，在这个例子中OpenGL会给当前激活的纹理设定纹理环绕方式为GL\_MIRRORED\_REPEAT。

如果我们选择GL\_CLAMP\_TO\_BORDER纹理环绕方式，我们还需要指定一个边缘的颜色。这需要使用glTexParameter函数的`fv`后缀形式，用GL\_TEXTURE\_BORDER\_COLOR作为它的选项，并且传递一个float数组作为边缘的颜色值：

```
float borderColor[] = { 1.0f, 1.0f, 0.0f, 1.0f };
glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, borderColor);
```



