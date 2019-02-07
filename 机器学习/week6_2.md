1. bias and variance
   在机器学习模型(model)的选型中，经常会遇到一个问题，feature的多项式次数(degree of polynomial,d)与欠拟合(underfit)和过拟合(overfit)之间的关系。如果一个模型的预测结果$$h_\theta$$很差，是由underfit造成的还是由overfit造成的？
    
     Bias即所謂的Underfitting，因為參數過少連Training set都會有頗大的預測誤差.
    Variance即所謂的Overfitting，因為參數過多導致過度符合Training set的資料特性，使得其無法預測較為普遍的資料集.
    我们所要做的，就是找到a golden mean between these two，介于underfit和overfit之间的一个合适次数。
    The training error will tend to decrease as we increase the degree d of the polynomial.
At the same time, the cross validation error will tend to decrease as we increase d up to a point, and then it will increase as d is increased, forming a convex curve.如下图所示：

![](/assets/50.png)
根据上图可断言：
High bias (underfitting): both $$J_{train}(\Theta)$$ and $$J_{CV}(\Theta)$$ will be high. Also, $$J_{CV}(\Theta) \approx J_{train}(\Theta)$$。

High variance (overfitting): $$J_{train}(\Theta)$$ will be low and $$J_{CV}(\Theta)$$ will be much greater than $$J_{train}(\Theta)$$.
因此，我们可以通过对比训练数据(training set)与交叉验证损失函数(cost function)结果来判断是多项式次数多还是少。

2.Regularization and Bias/Variance
為了解決Overfitting的問題，在先前的文章中有提到可以使用Regularization的方法來處理，但是這還存在一個問題：我們的λ要用多大算是合适呢？
不同的λ將可能造成不同的問題：若是λ很大的話，將會使得所有的參數都變得很小而沒什麼影響力，這會造成Underfitting的問題；若是λ很小的則就像是λ根本沒加進去一樣，仍然沒解決Overfitting的問題![](/assets/51.png)
上图显示了，不同的lambda影响了不同的$$\theta$$的结果，从而使得$$h_\theta(x)$$函数结果出现了欠拟合(最左侧)与过拟合（最右侧）的情况。那如何在中间选区一个合适的值呢？

我們會採用上一篇文章提到的：Training set, Cross Validation set跟Test set的概念，也就是我們先用traning set代入不同的λ來訓練模型，再將cross validation的資料丟入這些不同λ的模型得出不同的誤差值，最後再從中得到最好的λ、模型(最小的誤差值)，具体过程为：

 1）Create a list of lambdas (i.e.λ∈{0,0.01,0.02,0.04,0.08,0.16,0.32,0.64,1.28,2.56,5.12,10.24});
 2）Create a set of models with different degrees or any other variants.
 3）Iterate through the $$\lambda$$s and for each λ go through all the models to learn some Θ.(注意，这一步训练$$\theta$$的时候要代入$$\lambda$$)
 4）Compute the cross validation error using the learned Θ (computed with λ) on the $$J_{CV}(\Theta)$$ without regularization or λ = 0.(注意，这一步使用validate cross数据集的时候不带λ，因为Θ已经训练出来了)
 5）Select the best combo that produces the lowest error on the cross validation set.Using the best combo Θ and λ, apply it on $$J_{test}(\Theta)$$ to see if it has a good generalization of the problem.