吴恩达的机器学习第三周
1. 逻辑回归
分類問題通常比較偏向預測出离散的結果\(是/不是\)，这个方法与之前的线型回归方法有些不同，是因为分类方法并不是一个线型方程可以解决的问题。
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
舉例來說，當給予x0(為1),x1兩個參數代入h(θ)函數後，假設得到0.7的數字
那麼代表病患可能有70%的機率罹患惡性腫瘤,我們可以用下列函式來表示：當給予x與θ參數時，惡性腫瘤(y=1)的機率是多少(h(θ))?
$$
h_\theta(x)=P(y=1|x;\theta)=1-P(y=1|x;\theta)
$$

3.Decision boundary
前面的$$h_\theta(x)$$是0-1的连续值，而为了得到0，1这两个离散值，我们定义
$$
h_\theta(x)\ge 0.5 → y=1
$$ 

$$
h_\theta(x) < 0.5 → y=0
$$

根据上面定义可知，z>0 → g(z) >0.5
因此 当 $$\theta^T\ge0$$时,y=1,反之 y=0
The decision boundary is the line that separates the area where y = 0 and where y = 1. It is created by our hypothesis function.