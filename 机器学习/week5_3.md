3 反向传递的解释
首先看看正向传递(forward propagation)的解释
如下图所示，正向传递就是从左至右的过程
![](/机器学习/images/39.png)
每一個節點、unit的數值都是由上一層的unit透過不同的比重後重新組成得出的

那么当最终的结果跟样本期望的结果有偏差，偏差是如何反向订正回每一层的unit上呢？
![](/机器学习/images/40.png)
如上图所示，反向查看下一层的偏差由上一层“贡献”了多少
In the image above, to calculate $$\delta_2^{(2)}$$, we multiply the weights $$\Theta_{12}^{(2)}$$ and $$\Theta_{22}^{(2)}$$ by their respective $$\delta$$ values found to the right of each edge.So we get $$\delta_2^{(2)}$$ = $$\Theta_{12}^{(2)}$$ *$$\delta_1^{(3)}$$ +$$\Theta_{22}^{(2)}$$ *$$\delta_2^{(3)}$$
​	 .