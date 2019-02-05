1. $$\Theta 的初值问题$$
$$\Theta$$的初始值要用一个猜测值，那这个猜测值用全Zero是不合适的，因为这样会使得所有的输入和中间隐藏层的节点都使用相同的权重，各个层的δ(小寫delta)的值都會是一樣的：來源的輸入數值(x)通過比例重分配後重新產生下一層各個unit的不同activation值，而同樣的比例代表產生的activation值也會是一樣的，也因此誤差也會是一樣的....

这样经过几次迭代之后，每一个节点的值都会变成一样的，we initialize each $$\Theta^{(l)}_{ij}$$ to a random value between $$[-\epsilon,\epsilon]$$. Using the above formula guarantees that we get the desired bound
![](/机器学习/images/44.png)
2. To sum up.....
当我们考虑使用神经网络解决问题时，第一个需要确定的是：网络结构。包括总共要有多少层，每个隐藏层要有多少单元，而有些参数可以通过以下方式确定：
 (1)Number of input units = dimension of features $$x^{(i)}$$ 
 (2)Number of output units = number of classes
 (3)Number of hidden units per layer = usually more the better (must balance with cost of computation as it increases with more hidden units)
 (4)Defaults: 1 hidden layer. If you have more than 1 hidden layer, then it is recommended that you have the same number of units in every hidden layer.
 
 之后即可以通过以下步骤训练神经网络了
  （1）Randomly initialize the weights.上一节讲过了
  （2）Implement forward propagation to get $$h_\Theta(x^{(i)})$$ for any $$x^{(i)}$$
  （3）Implement the cost function（第五周1）
  （4）Implement backpropagation to compute partial derivatives（第五周2）