1.如何有效的优化已有的机器学习算法？假設我們為了預測房價而擬定了一個Linear Regression的模型來預測，
但是卻發現這個模型出現了難以接受的誤差，這時候我們有幾個選擇可以來試著改善：
![](/机器学习/images/46.png)
而每個選擇看似簡單，實則容易擴張成動輒數月、耗費時間跟金錢的專案。但是許多人選擇的方式常常都只是憑著"gut feeling"，也近似於隨機選取了.在下面，將會提到我們將藉由Machine Learning diagnostic的方式來診斷出模型的問題，並依此作為一個改善模型的依據。
机器学习诊断法：
A test that you can run to gain insight what is/isn't working with a learning algorithm,and gain guidance as to how best to improve its performance.

2.Evaluating a Hypothesis
A hypothesis may have a low error for the training examples but still be inaccurate (because of overfitting). Thus, to evaluate a hypothesis, given a dataset of training examples, we can **split up the data into two sets**: a training set and a test set. Typically, the training set consists of** 70 % **of your data and the test set is the remaining 30 %.

The new procedure using these two sets is then:

  (1) Learn $$\Theta$$ and minimize $$J_{train}(\Theta)$$ using the training set
  (2) Compute the test set error $$J_{test}(\Theta)$$
![](/机器学习/images/47.png)

3. 模型选择
前面一步可以**评估**一个模型的好坏,但是还有一个问题，是如何选择一个**最好**的模型。这是什么意思呢？假設我們用跟前面的方式將資料分成兩種：Training set跟Test set，且目前我們手上有多個不同的模型(二次方、三次方...等)
![](/assets/48.png)
原先的做法應該是透過Training set來訓練這些不同的模型，然後再透過Test set來得到這些不同模型的預測誤差，最後我們再從中挑選出最好的模型A(Test set中最小的預測誤差)