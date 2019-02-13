1.kernels
SVM是一种经典的机器学习算法，主要解决数据分类问题。
SVM引入kernel的概念，是logistic regression的进一步简化。将z=$$\theta^TX$$中的X变成一个f=g(x),于是就有了z=$$\theta^Tf$$
主要目的还是为了减少计算量，如果是在一副照片中识别物体，照片中的每一个像素都是一个feature，而使用高阶多项式，则计算量将会相当巨大。![](/机器学习/images/64.PNG)
如上图所示，f3替换x1x2,而上面这个f=g(x)，则成为**核函数**
核函数包括：
（1）Linear Kernel 线性核
实际上就是不使用Kernel，直接使用\theta^{T} X作为cost function的自变量
（2）Gaussian Kernel 高斯核