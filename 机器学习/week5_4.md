1.Unrolling Parameters
In order to use optimizing functions such as "fminunc()", we will want to "unroll" all the elements and put them into one long vector:


```
thetaVector = [ Theta1(:); Theta2(:); Theta3(:); ]
deltaVector = [ D1(:); D2(:); D3(:) ]
```



If the dimensions of Theta1 is 10x11, Theta2 is 10x11 and Theta3 is 1x11, then we can get back our original matrices from the "unrolled" versions as follows:


```
Theta1 = reshape(thetaVector(1:110),10,11)
Theta2 = reshape(thetaVector(111:220),10,11)
Theta3 = reshape(thetaVector(221:231),1,11)

```

总之，就是为了使用现成的函数而将Matrix转化成Vector，计算出结果后再反算回来的技巧

2.Gradient Checking
我们使用 $$\Theta = \Theta - \frac {\partial}{\partial \Theta}J$$ 来多次对初始$$\Theta$$进行订正，但如何保证 $$\frac {\partial}{\partial \Theta}J$$每次都计算正确呢，本节就是探讨这个话题
根据偏导的定义，微分所做的事情就是求得某個點的切線斜率，如下图所示，偏导就是斜率(y2-y1)/(x2-x1)
![](/机器学习/images/42.png)
為了求得某點的切線斜率，我們分別往上(+ε)跟往下(-ε)，ε可以想像為一個個極小的變數(小寫epsilon，ε 大概为$$10^{-4}$$)。取兩個極近的點，並透過取這兩點的斜率來得到近似於切線斜率的數值k,最後再透過確認原本偏導項的數值與k是否相近來確信back propagation是否運作正確。
因此，当得出以下结论时，就说明梯度下降参数正确
$$\frac {\partial}{\partial \Theta}J ≈ \frac {J(Θ+ϵ)−J(Θ−ϵ)}{2ϵ}$$
对于复杂函数，![](/机器学习/images/43.png)

Once you have verified once that your backpropagation algorithm is correct, you don't need to compute gradApprox again. The code to compute gradApprox can be very slow.记得检查完以后关闭~~