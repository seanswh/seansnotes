课外学习：关于VBO、VAO
学习材料1：VAO与VBO的前世今生(http://www.photoneray.com/opengl-vao-vbo/)
OpenGL作为图形API，制定的是绘图标准，采用的是CS模式。它将自己看作Server端，接收Client端传过来的数据，然后开启流水线，按需绘制出最终结果。

按照其他说法： An application program written to use the OpenGL API is the "client" and runs on the CPU. The implementation of the OpenGL graphics engine (including the GLSL shader programs you will write) is the "server" and runs on the GPU. 姑且认为，CPU上的程序是client，GPU上的是Server。
然后，Geometry and many other types of attributes are stored in buffers called Vertx Buffer Objects (or VBOs). These buffers are allocated on the GPU and filled by your CPU program.

具体来说，就是：The data for an OpenGL object to be displayed is stored in a vertex array object (VAO). A VAO encapsulates geometry and related attributes whose values can change from one vertex to another. Each such attribute (coordinates, color, etc.) is sent to the GPU in a vertex buffer object (VBO). In general, one VAO can reference an arbitrary number of VBOs. 

VAOs and VBOs are "named" using unsigned integers. Each such "name" must be assigned by an OpenGL name broker routine. VAO names are assigned by **glGenVertexArrays**; VBO names are assigned by glGenBuffers. Note that the interface to the name broker routines allows an arbitrary number of names to be assigned at once. Here we are asking for only a single name of each type.VAO和VBO都是一个无符号整型数字定义，而且该值必须由OPENGL创建

We make the VAO and VBOs active (i.e., open for editing or use) by binding them. Binding is accomplished by passing a single assigned name to glBindVertexArray (for a VAO) or glBindBuffer (for VBOs).创建或申请完VAO和VBO后还要绑定激活。

Once a VBO has been bound, the routine glBufferData can be used to both (i) dynamically allocate GPU storage for the buffer and (ii) send CPU data to the dynamically allocated GPU buffer storage.

Finally, the glEnableVertexAttribArray call tells the "vertex fetch" processor (see the OpenGL pipeline) to actually obtain values for this attribute from the VBO. It might seem like you would always want to do this, but we will see an alternative possibility and motivations for it later.
------------------------代码------------------
来源：http://www.zwqxin.com/archives/opengl/vao-and-vbo-stuff.html
下列代码很好的解释了VAO、VBO的关系，代码分为2个部分，构建部分与绘制部分
初始化部分：

```
/* Allocate and assign a Vertex Array Object to our handle */
glGenVertexArrays(1, &m_nQuadVAO); 
/* Bind our Vertex Array Object as the current used object */
glBindVertexArray(m_nQuadVAO);  
  
 /* Allocate and assign one Vertex Buffer Object to our handle */  
glGenBuffers(1, &m_nQuadPositionVBO); 
/* Bind our first VBO as being the active buffer and storing vertex attributes (coordinates) */ 
glBindBuffer(GL_ARRAY_BUFFER, m_nQuadPositionVBO); 
/* Copy the vertex data from diamond to our buffer */ 
glBufferData(GL_ARRAY_BUFFER, sizeof(fQuadPos), fQuadPos, GL_STREAM_DRAW);  
  
glEnableVertexAttribArray(VAT_POSITION);  
/* Specify that our coordinate data is going into attribute index 0, and contains two floats per vertex */
glVertexAttribPointer(VAT_POSITION, 2, GL_INT, GL_FALSE, 0, NULL);
  
glGenBuffers(1, &m_nQuadTexcoordVBO);  
glBindBuffer(GL_ARRAY_BUFFER, m_nQuadTexcoordVBO);  
glBufferData(GL_ARRAY_BUFFER, sizeof(fQuadTexcoord), fQuadTexcoord, GL_STREAM_DRAW);  
  
glEnableVertexAttribArray(VAT_TEXCOORD);  
glVertexAttribPointer(VAT_TEXCOORD, 2, GL_INT, GL_FALSE, 0, NULL);  
  
glGenBuffers(1, &m_nQuadIndexVBO);  
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_nQuadIndexVBO);  
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(nQuadIndex), nQuadIndex, GL_STREAM_DRAW);  
  
  
glBindVertexArray(NULL);  
  
glBindBuffer(GL_ARRAY_BUFFER, NULL);  
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, NULL); 
```
绘制部分：

```
glBindVertexArray(m_nQuadVAO);  
  
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, NULL);  
  
glBindVertexArray(NULL); 
```



