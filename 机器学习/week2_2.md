吴恩达的机器学习 第二周  
表达方式  $$x_j^{(i)}$$表示第i个训练集下的第j个属性 value of feature j in the $$i^{th}$$ training example  
所以梯度下降方法可以归纳成：  
$$\theta_j:=\theta_j-\alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)}-y^{(i)})\cdot x_j^{(i)}$$ for j:=0...n  
下面这张图显示了一个属性与多个属性的梯度下降  
![](5.png)

1. 扩展属性与多项式回归

We can improve our features and the form of our hypothesis function in a couple different ways.
We can **combine **multiple features into one. For example, we can combine $$x_1$$​and $$x_2$$ ​into a new feature $$x_3$$ ​by taking $$x_1*x_2$$​.

多项式回归：
hypothesis function need not be linear (a straight line) if that does not fit the data well.
In the cubic version, we have created new features $$x_2$$ and $$x_3$$ where $$x_2 = x_1^2 and x_3=x_1^3$$