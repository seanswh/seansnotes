1. Optimization Objective
先从 Logistic Regression 得cost function定义说起：
![](/机器学习/25.png)
将上式展开，可得下图结果：
![](/机器学习/images/58.png)
當y為1的時候，我們要盡可能提高z(z=$$θ^T*x$$)，好讓使用z的$$h_{\theta}(x)$$盡可能貼近1，而使總體cost降至0。下图显示了y=1时，cost function与Z的关系曲线。
![](/机器学习/images/59.png)

而為了運算效率，support vector machine將於原本的曲線圖形更動為筆直的直線，並設定當z為1的時候，cost變為0
当y為0時，我們要盡可能降低z，好讓使用z的htheta(x)盡可能貼近1，而使總體cost降至0。而為了運算效率，support vector machine將於原本的曲線圖形更動為筆直的直線，並設定當z為-1的時候，cost變為0
![](/机器学习/images/60.png)
这样，上面第一幅图中的公式便可精简为如下图所示：
![](/机器学习/images/61.png)
如果把系数$$\frac{1}{m}$$去掉，让C=$$\frac{1}{\lambda}$$,最终结果cost function为：
![](/机器学习/images/62.png)
2.Large Margin Intuition
支持向量机如下图所示：
![](/机器学习/images/63.png)
支持向量机所需要找到一个合适的θ，使得y=1与y=0时，cost function结果最小，又根据前一章节对$$cost_0(z)$$和$$cost_1(z)$$的定义，得知支持向量机与logistic regression的区别在于前者是要对z取两个范围，这个范围也就构成了 margin