1.过拟合 overfitting
就是结果太过逼近样本数的结果

“If we have too many features, the learned hypothesis may fit the training set very well (J(θ)=0), but fail to generalize to new examples(Predictions on new examples)”

那我們要怎麼解決Overfitting的問題呢？

有幾種做法：

1. 降低features的數量：人工選擇、model selection algorithm

2. Regularization：維持現有的features，但是降低部分不重要feature的影響力。這對於有著許多feature的hypothesis很有幫助