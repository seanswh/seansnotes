吴恩达的斯坦福《机器学习》

第一周：  
1.机器学习定义。  
两种定义：  
1）the field of study that gives computers the ability to learn without being explicitly programmed。这个定义较为传统，且非正式  
2）A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E。这个定义较为符合现代机器学习的定义。  
**Example**: playing checkers.  
E = the experience of playing many games of checkers  
T = the task of playing checkers.  
P = the probability that the program will win the next game.

机器学习分为2类:监督学习和非监督学习.  
2.监督学习\(方向\)

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

监督学习可分为：回归、分类。回归分析中，我们可获得连续性的输出；分类分析中，我们只能或得到离散的结果。

3.非监督学习

Unsupervised learning allows us to approach problems with little or no idea what our results should look like.

非监督学习用“聚类分析”将相似属性进行分析。

4.模型表达

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function h : X → Y so that h\(x\) is a “good” predictor for the corresponding value of y。


