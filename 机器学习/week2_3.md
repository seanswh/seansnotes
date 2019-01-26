吴恩达的机器学习 第二周3
Feature Scaling

We can speed up gradient descent by having each of our input values in roughly the same range.
目标：
$$-1\leq x_{(i)} \leq 1$$
方法：
 feature scaling and mean normalization
** Feature scaling** involves dividing the input values by the range (i.e. the maximum value minus the minimum value) of the input variable