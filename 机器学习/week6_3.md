1.学习曲线
那么，训练样本的个数对于损失函数有没有影响呢？或者说对于学习的效果有没有帮助呢。
學習曲線為一個觀察隨著訓練樣本數(m)不斷增加，J_train跟J_cv的變化圖形，如下图所示
![](/机器学习/images/52.png)
假設在預測模型是一個已經調整到非常不錯的狀態（说明不再调整$$\theta$$），那麼我們可以看到隨著樣本數增加，J_train也會緩緩地上升，而J_cv會因為參數漸漸地精準起來而隨之下降
  1）但是我们的训练模型有underfit的问题呢？
![](/机器学习/images/53.png)
我們可以發現当m从一个很小的值增大时$$J_{train}$$_會大幅上升，到一定程度後就趨於緩慢，而_$$J_{cv}$$則會在下降到一定程度後便幾乎不再下降，而兩者趨同，但最终两个误差值都会很高
结论：If a learning algorithm is suffering from high bias, getting more training data will not (by itself) help much.
![](/机器学习/images/54.png)
  2）如果训练模型有overfit呢？
  Low training set size: $$J_{train}(\Theta)$$ will be low and $$J_{CV}(\Theta)$$ will be high.
  Large training set size: $$J_{train}(\Theta)$$ increases with training set size and $$J_{CV}(\Theta)$$ continues to decrease without leveling off. Also, $$J_{train}(\Theta) < J_{CV}(\Theta)$$ but the difference between them remains significant.
  结论：If a learning algorithm is suffering from high variance, getting more training data is likely to help.
  ![](/机器学习/images/55.png)