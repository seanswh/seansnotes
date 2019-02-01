神经网络

以logistic regression為例，Neural Network會以x作為輸入，θ作為處理的權重，然後輸出hypothesis
![](/机器学习/images/27.png)
(x0是一個bias unit，代表其對應的θ0為獨立的常數，所以x0為1)
如果建立成一个三层网络，则如下图所示
![](/机器学习/images/28.png)
每一層都可以看到有著：輸入、處理跟輸出，而除了第一層跟最後一層之外，中間的層都通稱為hidden layer
下圖表示著輸入、處理跟輸出的函式