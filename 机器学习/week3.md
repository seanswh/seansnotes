吴恩达的机器学习 第二周
表达方式  $$x_j^{(i)}$$表示第i个训练集下的第j个属性 value of feature j in the $$i^{th}$$ training example
所以梯度下降方法可以归纳成：
$$\theta_j:=\theta_j-\alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)}-y^{(i)})\cdot x_j^{(i)}$$ for j:=0...n