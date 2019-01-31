
吴恩达的机器学习第三周
1. 逻辑回归
分类回顾通常偏向有限结果的，如果结果只存在0/1的结果，则属于二元回归
为何不用线性回归解决逻辑回归的问题？
因为分类问题不是一个线性问题，

2.逻辑回归的Hypothesis function
我们将逻辑回归的 $$h_\theta(x)$$的值定义在{0，1}之间，而我们还用$$\theta^Tx$$多项式来定义这个假设方程，
我们引入了sigmoid 方程，also called the "Logistic Function"，
$$
h_\theta(x) = g(\theta^Tx)
$$
$$
z=\theta^Tx
$$
$$
g(z)=\frac{1}{1+e^{-z}}
$$


符合如下特质
![](8.png)
方程的结果会无限逼近0和1
