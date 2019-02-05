1. $$\Theta 的初值问题$$
$$\Theta$$的初始值要用一个猜测值，那这个猜测值用全Zero是不合适的，因为这样会使得所有的输入和中间隐藏层的节点都使用相同的权重，各个层的δ(小寫delta)的值都會是一樣的：來源的輸入數值(x)通過比例重分配後重新產生下一層各個unit的不同activation值，而同樣的比例代表產生的activation值也會是一樣的，也因此誤差也會是一樣的....

这样经过几次迭代之后，每一个节点的值都会变成一样的，we initialize each $$\Theta^{(l)}_{ij}$$ to a random value between $$[-\epsilon,\epsilon]$$. Using the above formula guarantees that we get the desired bound
![](/机器学习/images/44.png)
2.