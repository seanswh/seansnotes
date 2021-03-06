2.纹理过滤  
纹理坐标并不受限于纹理图片的分辨率，纹理坐标可以是任意浮点数。因此OPENGL需要将纹理映射到任意的浮点坐标上，尤其是当物体比纹理大很多的时候。这个时候需要的工作就叫“纹理过滤”，对于纹理过滤，OPENGL有很多个选项，不过我们只介绍最常用的2个：GL\_NEAREST and GL\_LINEAR

Texture Pixel也叫Texel，你可以想象你打开一张.jpg格式图片，不断放大你会发现它是由无数像素点组成的，这个点就是纹理像素；注意不要和纹理坐标搞混，纹理坐标是你给模型顶点设置的那个数组，OpenGL以这个顶点的纹理坐标数据去查找纹理图像上的像素，然后进行采样提取纹理像素的颜色。

OPENGL默认使用的方式是GL\_NEAREST，当使用该选项时，OpenGL会选择像素中心点最接近纹理坐标的那个像素。如下图所示：  
![](/assets/filter_nearest.png)  
GL\_LINEAR（也叫线性过滤，\(Bi\)linear Filtering）它会基于纹理坐标附近的纹理像素，计算出一个插值，近似出这些纹理像素之间的颜色。一个纹理像素的中心距离纹理坐标越近，那么这个纹理像素的颜色对最终的样本颜色的贡献越大。下图中你可以看到返回的颜色是邻近像素的混合色：  
![](/assets/filter_linear.png)

下面这个例子可以更好的解释“邻近过滤”和“线性过滤”

![](/assets/texture_filtering.png)

当进行放大\(Magnify\)和缩小\(Minify\)操作的时候可以设置纹理过滤的选项，比如你可以在纹理被缩小的时候使用邻近过滤，被放大时使用线性过滤。我们需要使用glTexParameter\*函数为放大和缩小指定过滤方式。这段代码看起来会和纹理环绕方式的设置很相似：

`glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);                      
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);`

3.MipMaps

假设我们有一个包含着上千物体的大房间，每个物体上都有相同的纹理。有些物体会很远，有些物体会很近，而且两者纹理贴图的分辨率都很高。由于远处的物体可能只产生很少的片段，OpenGL从高分辨率纹理中为这些片段获取正确的颜色值就很困难，因为一个片段可能涵盖了很大一片纹理，而这个片段获取颜色会很困难。在小物体上这会产生不真实的感觉，更不用说对小物体使用高分辨率纹理会浪费很多内存的问题了。

OPENGL引入了MipMaps技术来解决上述问题，这个就是提供一个纹理图像集合\(collection\)，纹理图像依次是前一张的一半。Mipmaps的使用原理很简单，当物体距离观察者超过一个阈值之后，OPENGL 就会从集合中选择一个最为合适的纹理。由于距离观察者较远，因此分辨率较低也不会有较大影响，另外这样带来的计算成本降低也是很显著的。

![](/OPENGL/images/mipmaps.png)

上图就是Mipmaps的一个例子。手工为每个纹理图像创建一系列多级渐远纹理很麻烦，幸好OpenGL有一个glGenerateMipmaps函数，在创建完一个纹理后调用它OpenGL就会承担接下来的所有工作了。

在渲染中切换Mipmaps不同级别时，OpenGL在两个不同级别的纹理之间会产生不真实的生硬边界。就像普通的纹理过滤一样，切换Mipmaps不同级别时也可以在两个不同级别之间使用NEAREST和LINEAR过滤。为了指定不同级别之间的过滤方式，你可以使用下面四个选项中的一个代替原有的过滤方式：

| 过滤方式 | 描述 |
| :--- | :--- |
| GL\_NEAREST\_MIPMAP\_NEAREST | 使用最邻近的Mipmaps纹理来匹配像素大小，并使用邻近插值进行纹理采样 |
| GL\_LINEAR\_MIPMAP\_NEAREST | 使用最邻近的Mipmaps纹理级别，并使用线性插值进行采样 |
| GL\_NEAREST\_MIPMAP\_LINEAR | 在两个最匹配像素大小的Mipmaps之间进行线性插值，使用邻近插值进行采样 |
| GL\_LINEAR\_MIPMAP\_LINEAR | 在两个邻近的Mipmaps纹理之间使用线性插值，并使用线性插值进行采样 |

就像纹理过滤一样，我们可以使用glTexParameteri将过滤方式设置为前面四种提到的方法之一：

```
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
```

一个常见的错误是，将放大过滤的选项设置为多级渐远纹理过滤选项之一（上面语句的第二条）。这样没有任何效果，因为Mipmaps主要是使用在纹理被缩小的情况下的：纹理放大不会使用Mipmaps，为放大过滤设置Mipmaps的选项会产生一个GL\_INVALID\_ENUM错误代码。

