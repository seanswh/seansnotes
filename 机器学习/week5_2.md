2.反向传播算法（Backpropagation Algorithm） 在前面所有的章节学习了基础准备概念之后，这周开始学习关于神经网络的算法了。 
与之前学习线性回归、逻辑回归的思路一样，神经网络也需要找到使得损失函数(cost function)最小的方法，我们的目标同样是 $$min_\Theta J(\Theta)$$
 跟之前第一週、第二週提到的Gradient Descent原理一樣，我們要先求出各個參數的偏導項(partial derivative)，之後再用迭代地方式减去這些偏導項。首先的目标是计算$$\frac{\partial}{\partial \Theta^{l}{i,j}} J\Theta$$ 因為推導過程過於複雜，因此我們先知道大概的步骤和結論就好: 
 最终结果：
 ![](/机器学习/images/36.png)
 说明：
（1）. Δ(大寫delta)是用來求出偏導向的誤差和，在本節最後面會提到如何計算。而Δ需要由δ(小寫delta)跟a的乘積來求得
   (1.1)a是由 forward propagation求得的activation(見前面的Model Representation)，就是前面在計算cost function時會得到的各個unit的數值
   (1.2) δ則需由以下的函式來計算，δ可以將之理解為各個節點上的數值誤差.除了最後一層(output layer，這邊是4)外，其他層的運算函式都一樣
   ![](/机器学习/images/37.png)
   除了最後一層(output layer，這邊是4)外，其他層的運算函式都一樣.而第一層(input layer)無須計算，因為用來輸入的數值不存在誤差的現象。
  具体计算方式： 
  ![](/机器学习/images/35.png)
  For training example t =1 to m:
 （1）Given training set $$\lbrace (x^{(1)}, y^{(1)}) \cdots (x^{(m)}, y^{(m)})\rbrace$$ Set $$\Delta^{(l)}{i,j}$$:= 0 for all (l,i,j), (hence you end up having a matrix full of zeros)
 （2）Set $$a^{(1)} := x^{(t)}$$, 開始算第二、三、四...一直到輸出層的a,使用下图所示公式：
 ![](/机器学习/images/38.png)
 (3) Using $$y^{(t)}$$, compute $$\delta^{(L)} = a^{(L)} - y^{(t)}$$
 (4) Compute $$\delta^{(L-1)}, \delta^{(L-2)},\dots,\delta^{(2)}$$ using $$\delta^{(l)} = ((\Theta^{(l)})^T \delta^{(l+1)})\ .*\ a^{(l)}\ .*\ (1 - a^{(l)})$$
 (5) $$Δ_{i,j}^{(l)} :=Δ_{i,j}^{(l)}+a_j^{(l)}	​δ_i^{(l+1)} $$ or with vectorization, $$\Delta^{(l)} := \Delta^{(l)} + \delta^{(l+1)}(a^{(l)})^T$$
 
 从1到m, we update our new $$\Delta$$ matrix
 最终：
 $$D_{i,j}^{(l)}:= \frac{1}{m}(Δ_{i,j}^{(l)} +λΘ_{i,j}^{(l)}),  if j≠0.$$
 $$D_{i,j}^{(l)}:=\frac{1}{m}Δ_{i,j}^{(l)}$$,  if j=0