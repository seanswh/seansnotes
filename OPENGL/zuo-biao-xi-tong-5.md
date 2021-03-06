### 深度测试

OpenGL存储它的所有深度信息于Z缓冲区\(Z-buffer\)中，也被称为深度缓冲区\(Depth Buffer\)。GLFW会自动为你生成这样一个缓冲区 \(就如它有一个颜色缓冲区来存储输出图像的颜色\)。深度存储在每个片段里面\(作为片段的z值\)当片段像输出它的颜色时，OpenGL会将它的深度值和z缓冲进行比较然后如果当前的片段在其它片段之后它将会被丢弃，然后重写。这个过程称为**深度测试\(Depth Testing\)**并且它是由OpenGL自动完成的。

OPENGL中深度测试默认是关闭的，我们通过`glEnable`函数来开启深度测试：

```
glEnable(GL_DEPTH_TEST);
```

另外，由于OPENGL是一个状态机，因此在每一个渲染周期，我们都会要清除深度缓冲，不然就算在动画，有些片元也永远不可能显示在前面了。

