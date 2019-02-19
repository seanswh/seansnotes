1.数据压缩
用于将样例数据的Feature维度数减小，2D->1D,3D->2D
2.工具 PCA(Principal Component Analysis)
用向量(vector)方法压缩维度，如下图所示：
![](/机器学习/images/72.PNG)
具体执行过程：
（1）对输入样本集进行标准化预处理
![](/机器学习/images/73.PNG)
（2）计算输入样本矩阵的特征向量 $$\Sigma= \frac{1}{m}\sum_{i=1}^{n}(x^{(i)})(x^{(i)})^T$$
（3）使用octave中的svd方法计算向量 [u,s,v] = svd(Sigma);其中u即为结果矩阵，如果需要降维到k，则从u中取前k列即可。
