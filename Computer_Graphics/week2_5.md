课外学习：关于VBO、VAO
学习材料1：VAO与VBO的前世今生(http://www.photoneray.com/opengl-vao-vbo/)
OpenGL作为图形API，制定的是绘图标准，采用的是CS模式。它将自己看作Server端，接收Client端传过来的数据，然后开启流水线，按需绘制出最终结果。

按照其他说法： An application program written to use the OpenGL API is the "client" and runs on the CPU. The implementation of the OpenGL graphics engine (including the GLSL shader programs you will write) is the "server" and runs on the GPU. 姑且认为，CPU上的程序是client，GPU上的是Server。
然后，Geometry and many other types of attributes are stored in buffers called Vertx Buffer Objects (or VBOs). These buffers are allocated on the GPU and filled by your CPU program.

具体来说，就是：The data for an OpenGL object to be displayed is stored in a vertex array object (VAO). A VAO encapsulates geometry and related attributes whose values can change from one vertex to another. Each such attribute (coordinates, color, etc.) is sent to the GPU in a vertex buffer object (VBO). In general, one VAO can reference an arbitrary number of VBOs. 
