上面介绍了通过VBO来进行顶点属性设置，然后绘制的方法，在绘制物体较少，而且绘制属性不多的情况下没什么问题，但是如果有上百个物体，且每个物体的绘制属性很多的情况下，绑定合适的缓冲对象然后配置对应的显示属性会变得效率很低，因此如果把上述的所有配置状态都存在一个对象中，每次通过绑定这个对象来完成状态切换，会是一个很高效的实现。

VAO\(Vertex Array Object\)

就像VBO\(顶点缓存对象\)，VAO也可以被绑定，而且VAO包括了VBO以及后续的顶点属性。这样的好处就是只需配置一次，后续绘制的时候直接绑定相应的VAO即可。这使在不同顶点数据和属性配置之间切换变得非常简单。

OPENGL的核心模式要求必须使用VAO，如果VAO绑定失败，则OPENGL绘制不出任何东西出来。

一个顶点数组对象会储存以下这些内容：

* glEnableVertexAttribArray和glDisableVertexAttribArray的调用。
* 通过glVertexAttribPointer设置的顶点属性配置。
* 通过glVertexAttribPointer调用进行的顶点缓冲对象与顶点属性链接。

![](/OPENGL/images/vertex_array_objects.png)

VAO的创建和使用：



