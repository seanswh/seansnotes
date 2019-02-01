神经网络应用
第一个简单的应用是实现 AND 逻辑运算，如果建立的神经网络结构如下如所示：
$$\left[
\begin{matrix}
x_0\\
x_1\\
x_2
\end{matrix}
\right]→
\left[
g(z^{(2)}
\right]→
h_\theta(x)
$$
 $$x_0$$ is our bias variable and is always 1.
 加入第一个theta矩阵为：
 $$
 \Theta^{(1)}=
 \left[
 \begin{matrix}
 -30 & 20 & 20
 \end{matrix}
 \right]
 $$
 输出结果为：
 ![](/机器学习/images/32.png)
 
 基于以上考虑，我们可以得出以下逻辑运算对应的$$\theta$$,我们也可以讲这些逻辑运算进行结合，这样就构成了一个网络![](/机器学习/images/33.png)
 该网络可以计算较为复杂的逻辑运算