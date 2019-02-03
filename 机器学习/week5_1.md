1.神经网络相关的损失函数
先介绍相关的变量
L = total number of layers in the network
$$s_l$$ = number of units (not counting bias unit) in layer l
K = number of output units/classes

 We denote $$h_\Theta(x)_k$$ as being a hypothesis that results in the $$k^{th}$$ output
 基于以上的定义，我们将逻辑回归的损失函数进行如下调整后结果为：
 ![](/机器学习/images/34.png)
 （1）前項跟原本logistic regression相比的話，會發現多了個Σ跟k的符號，這是因為這裏Neural Network的hypothesis是multiclass的假設，會輸出多個結果。因此要求預估誤差的話，就需要針對每個hypothesis的輸出單位k跟正確答案y的每個輸出單位k
 （2）regularization就跟前面提到的概念是一樣的：我們要加總所有θ的平方項。
這邊表示方式稍微複雜了點，但是其所做的事情跟上述所提如出一徹，最外面的Σ是為了要從layer 1一直算到layer n，第二個Σ跟第三個 layer是為了求兩個 layer之間的theta值(請將其想像成是連接不同單位、unit的線)
(θji代表後一層輸入單位j與前一層輸出單位i的處理權重、連接線)，由於通常會忽略bias unit，也就是我們通常不會去把θj0：從某個layer的bias uni連出去的線列入考量，因此 j從1開始。
$$\Theta$$矩阵中的列数为当前层次的unit（include the bias unit）个数，行数为下一层unit的个数