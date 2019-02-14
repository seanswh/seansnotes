1.关于如何应用SVM解决识别问题
logistic regression(LR)、神经网络、support vector machine的目的都是为了在数据中获取boundary已解决数据中的分类问题，最终目的都是为了计算合适的$$\theta$$
![](/机器学习/images/68.png)

2.因为在高斯函数中有一个平方项，因此要在使用高斯核之前先做feature scaling.
另外，similarity function 除了高斯函数以外还有很多，在SVM实践中，只要符合Mercer's Theorem都可以作为核函数。

3. 关于landmark $$l_{(i)}$$的选取，一般选择所有的test data作为l