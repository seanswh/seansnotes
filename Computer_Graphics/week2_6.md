渲染管线顺序
OPENGL编程中，管线(pipeline)渲染顺序如下图所示：

![](/Computer_Graphics/images/41.png)
1）We start with an object defined in object coordinates that's in the native coordinate system of the object.
2)apply the modelview transforms which corresponds to the modelview matrix.Note that this has both a model transformation, which is the object transformation,and the view transformation, which is glm::lookAt,which positions the camera appropriately.
3)Thereafter you apply the projection matrix,which goes from 3D to 2D,and this corresponds to glm::perspective
4)clip coordinates.Here everything is in the range of -1 to +1. mapping the world essentially into a unit cube.