2.反向传播算法（Backpropagation Algorithm） 在前面所有的章节学习了基础准备概念之后，这周开始学习关于神经网络的算法了。 
与之前学习线性回归、逻辑回归的思路一样，神经网络也需要找到使得损失函数(cost function)最小的方法，我们的目标同样是 $$min_\Theta J(\Theta)$$
 跟之前第一週、第二週提到的Gradient Descent原理一樣，我們要先求出各個參數的偏導項(partial derivative)，之後再用迭代地方式减去這些偏導項。首先的目标是计算$$\frac{\partial}{\partial \Theta^{l}{i,j}} J\Theta$$ 因為推導過程過於複雜，因此我們先知道大概的步骤和結論就好: 