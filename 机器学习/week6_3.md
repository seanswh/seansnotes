回到一開始的問題：當今天我們的模型發生令人無法接受的誤差時，我們有哪些解決辦法呢？
    1）Getting more training examples: Fixes high variance
    2）Trying smaller sets of features: Fixes high variance
    3）Adding features: Fixes high bias
    4）Adding polynomial features: Fixes high bias
    5）Decreasing λ: Fixes high bias
    6）Increasing λ: Fixes high variance.
    
再看神经网络结构，當network的結構越為簡單時，代表其越有著Underfitting的問題；而當network的結構越為複雜時，代表其除了運算成本很高外，還可能有著Overfitting的問題，也因此可以適時導入Regularization來解決。
Using a single hidden layer is a good starting default. You can train your neural network on a number of hidden layers using your cross validation set. You can then select the one that performs best.
