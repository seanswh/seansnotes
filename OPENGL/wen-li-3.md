加载和显示纹理

纹理图片可以存储在几十种格式的文件中，每一种都有自己的结构定义和数据存储顺序，那么我们怎么在我们的应用中获得这个图像呢？一种办法是我们选定一种格式\(比如.png\)后，自己实现一个加载器，然后把文件读入字节数组。这个工作量不小，而且如果要适配更多文件类型，那工作量就更大了。

一个简单的方式是加载一个“图片加载库”，该库支持多种文件类型，比如stb\_image.h

**创建纹理**

与之前介绍的OPENGL对象一样，纹理也是靠ID值来引用的，如下代码所示：

```
GLuint texture;
glGenTextures(1, &texture);
```

glGenTextures函数第一个参数是创建纹理的数量，然后存储在第二个参数数组中，就像其他对象一样，我们需要首先绑定它，这样**后续任何纹理相关的指令都可以配置当前绑定的纹理**：

```
glBindTexture(GL_TEXTURE_2D, texture);
```

现在纹理已经绑定了，我们可以使用前面载入的图片数据生成一个纹理了。纹理可以通过glTexImage2D来生成：

```
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image);
glGenerateMipmap(GL_TEXTURE_2D);
```

函数很长，参数也不少，所以我们一个一个地讲解：

* 第一个参数指定了纹理目标\(Target\)。设置为GL\_TEXTURE\_2D意味着会生成与当前绑定的纹理对象在同一个目标上的纹理（任何绑定到GL\_TEXTURE\_1D和GL\_TEXTURE\_3D的纹理不会受到影响）。
* 第二个参数为纹理指定mipmap的级别，如果你希望单独手动设置每个Mipmap级别的话。这里我们填0，也就是基本级别。
* 第三个参数告诉OpenGL我们希望把纹理储存为何种格式。我们的图像只有`RGB`值，因此我们也把纹理储存为`RGB`值。
* 第四个和第五个参数设置最终的纹理的宽度和高度。我们之前加载图像的时候储存了它们，所以我们使用对应的变量。
* 下个参数应该总是被设为`0`（历史遗留问题）。
* 第七第八个参数定义了源图的格式和数据类型。我们使用RGB值加载这个图像，并把它们储存为
  `char`\(byte\)数组，我们将会传入对应值。
* 最后一个参数是真正的图像数据。

一但glTexImage2D函数被调用以后，之前被绑定的纹理对象就会有纹理图像附加上，然而目前只有mipmap中的基本级别被附加上了，如果我们需要使用mipmap，我们需要自己设置其他级别的纹理图像，\(通过逐渐增加第二个参数的值\)，或者在生成纹理之后直接调用glGenerateMipmap。这会为当前绑定的纹理自动生成所有需要的多级渐远纹理。

当创建完纹理和对应的mipmaps之后立即释放图片内存是一个好习惯


