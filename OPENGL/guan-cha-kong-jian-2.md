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





