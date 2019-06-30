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



