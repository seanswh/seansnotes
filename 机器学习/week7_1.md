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
