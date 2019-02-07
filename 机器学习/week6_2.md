1. bias and variance
   在机器学习模型(model)的选型中，经常会遇到一个问题，feature的多项式次数(degree)与欠拟合(underfit)和过拟合(overfit)之间的关系。如果一个模型的预测结果$$h_\theta$$很差，是由underfit造成的还是由overfit造成的？
    
     Bias即所謂的Underfitting，因為參數過少連Training set都會有頗大的預測誤差.
    Variance即所謂的Overfitting，因為參數過多導致過度符合Training set的資料特性，使得其無法預測較為普遍的資料集.
    
