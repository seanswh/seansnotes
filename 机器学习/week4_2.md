神经网络

以logistic regression為例，Neural Network會以x作為輸入，θ作為處理的權重，然後輸出hypothesis
![](/机器学习/images/27.png)
(x0是一個bias unit，代表其對應的θ0為獨立的常數，所以x0為1)
如果建立成一个三层网络，则如下图所示
![](/机器学习/images/28.png)
 In neural networks, we use the same logistic function as in classification,$$\frac{1}{1 + e^{-\theta^Tx}} $$, yet we sometimes call it a **sigmoid (logistic) activation functio**n. In this situation, our "theta" parameters are sometimes called "**weights**".
Our input nodes (layer 1), also known as the "input layer", go into another node (layer 2), which finally outputs the hypothesis function, known as the "output layer".
除了第一層跟最後一層之外，中間的層都通稱為hidden layer,we label these intermediate or "hidden" layer nodes $$a^2_0 \cdots a^2_n $$ and call them "activation units."
$$
a^(j)_i="activation" of unit i in layer j
Θ(j)=matrix of weights controlling function mapping from layer j to layer j+1
$$

下圖表示著輸入、處理跟輸出的函式
![](/机器学习/images/29.png)
activation表示該單位的值，θij代表輸入單位j與與輸出單位i的處理權重
x0就是前面所提到的數字 1
那為什麼會有個g()包住這些多項式呢？
因為這是個用來解決 logistic regression問題的Neural Network，g(z) 代表的是一個 sigmoid的函數