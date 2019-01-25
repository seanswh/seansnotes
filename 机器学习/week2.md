吴恩达机器学习第一周 第二部分
1.损失函数
We can measure the accuracy of our hypothesis function by using a cost function损失函数是用来测量假定的函数的正确性的，公式如下：

$$J(\theta_0,\theta_1)=\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x_i)-y_i)^2$$

引入损失函数的目的是，计算$$\theta_0,\theta_1$$,使得h$$_\theta(x)$$最接近于训练集中的y值，也即$$J(\theta)=0$$
2.梯度下降法
梯度下降法Gradient Descent的目的是确立损失函数中的参数，使得损失函数最小，也就是$$h_\theta(x)$$函数结果最接近y。设定不同的$$\theta_0,\theta_1$$,对于其组成的假设函数，其损失函数值如下图所示
