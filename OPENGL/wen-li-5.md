# 纹理单元

片段着色器中使用了uniform sampler2D变量，但是我们没有使用glUniform函数赋值。如果我们想在一个片元着色器中设置多个纹理，我们可以通过使用glUniform1i函数，给纹理采样器\(sampler\)分配一个位置值.一个纹理的位置值通常称为一个纹理单元\(Texture Unit\)。一个纹理的默认纹理单元是0，且它是默认的激活纹理单元，所以我们没有分配位置值。

纹理单元的主要目的是让我们可以在一个纹理着色器中使用多个纹理，通过把纹理单元赋值给采样器，我们可以一次绑定多个纹理，只要我们使用时激活对应的纹理即可，就像glBindTexture一样，我们使用glActiveTexture激活纹理单元，传入我们需要使用的纹理单元：

```
glActiveTexture(GL_TEXTURE0); //在绑定纹理之前先激活纹理单元
glBindTexture(GL_TEXTURE_2D, texture);
```

激活纹理单元之后，接下来的glBindTexture函数调用会绑定这个纹理到被激活的纹理单元，由于纹理单元GL\_TEXTURE0默认总是被激活状态，所以我们在前面使用`glBindTexture`的时候，无需激活任何纹理单元。

如果我们使用了多个采样器\(sampler\)，那么我们需要在片段着色器中接收它：

```
#version 330 core

...

uniform sampler2D ourTexture1;
uniform sampler2D ourTexture2;

void main()
{
    color = mix(texture(ourTexture1, TexCoord), texture(ourTexture2, TexCoord), 0.2);
}
```

最终输出颜色现在是两个纹理的结合。GLSL内建的mix函数需要接受两个值作为原始输入，然后通过第三个值进行线性插值。如果第三个值是0，则全部使用第一个纹理颜色，如果第三个值是1.0，则全部使用第二个纹理颜色。`0.2`会返回`80%`的第一个输入颜色和`20%`的第二个输入颜色，即返回两个纹理的混合色。

使用纹理的顺序大致为：创建纹理对象-&gt;加载图片-&gt;使用glTexImage2D将图片创建成纹理。使用的时候先激活这个纹理对象，然后绑定。除此之外，我们还要用glUniform1i告诉我们的片段着色器，哪个着色采样器对应哪个纹理单元\(texture unit\)



