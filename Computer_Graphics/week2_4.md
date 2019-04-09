(1)shader 代码分析
看一下下面的fragment shader代码
![](/Computer_Graphics/images/38.png)
首先计算漫反射，根据Lambert计算公式求得lambert光照结果，然后根据Blinn-Phong公式计算镜面反射光照。