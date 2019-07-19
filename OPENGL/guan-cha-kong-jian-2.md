### 欧拉角Euler Angle

欧拉角\(Euler Angle\)是表示3D空间中可以表示任何旋转的三个值，如下图所示：

![](/OPENGL/images/camera_pitch_yaw_roll.png)

欧拉角有三种：俯仰角\(Pitch\)、偏航角\(Yaw\)和滚转角\(Roll\)，一般我们在OPENGL的场景中，只会使用到前面2种。

```
direction.x = cos(glm::radians(pitch)) * cos(glm::radians(yaw));
//译注：direction代表摄像机的“前”轴，但此前轴是和本文第一幅图片的第二个摄像机的direction是相反的
direction.y = sin(glm::radians(pitch));
direction.z = cos(glm::radians(pitch)) * sin(glm::radians(yaw));
```

这样我们就有了一个可以把俯仰角和偏航角转化为用来自由旋转的摄像机的3个维度的方向向量了。

### 鼠标输入

偏航角和俯仰角是从鼠标移动获得的，鼠标水平移动影响偏航角，鼠标垂直移动影响俯仰角。它的思想是储存上一帧鼠标的位置，在当前帧中我们当前计算鼠标位置和上一帧的位置相差多少。如果差别越大那么俯仰角或偏航角就改变越大。

首先我们要告诉GLFW，应该隐藏光标，并**捕捉\(Capture\)**它。捕捉鼠标意味着当应用集中焦点到鼠标上的时候光标就应该留在窗口中\(除非应用拾取焦点或退出\)。我们可以进行简单的配置:

```
glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
```

这个函数调用后，无论我们怎么去移动鼠标，它都不会显示了，也不会离开窗口。对于FPS摄像机系统来说很好：

