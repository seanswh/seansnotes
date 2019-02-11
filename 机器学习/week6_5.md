1.Error Metrics for Skewed Data
比如当前有这样一个情况：預測病人是否得到腫瘤，如果通过训练，我们的算法誤差率是1%(99%的準確率)。但是如果我们知道，所有的样本中，得癌症得比例只有0.5%,那如果我们“改良”一下算法——对所有样本，结果均是“没有癌症”，那“改良”后得算法正确率会提升到99.5%,误差率为0.5%,降低了一半哦~~那这个“改进”能称之为“优化”么？
显然不能~
那就牵扯出一个问题：到底应该如何评估一个算法是”改善“了呢？
我们使用precision和recall来评估~如下图所示：
![](/机器学习/images/57.png)

True positive：預測為1，實際也為1
False positive：預測為1，實際為0
False negative：預測為0，實際為1
True negative：預測為0，實際也為0

Precision: 預測為1的狀況下，實際的值為1的比率
$$\frac{True Positive}{True positive+false positive}$$
Recall:實際的值為1下，預測為1的比率為多少
$$\frac{True positive}{true positive+false negative}$$
一个好的分类器算法应该保证precision 和recall效果都好。但是真的能做到这点么？

2.Handling Skewed Data
回想逻辑回归得定义：
$$h_x(\theta) \ge 0.5 => y=1$$
$$h_x(\theta) < 0.5 => y = 0$$
好比我們使用Logistic Regression來預測病患是否有著腫瘤，我們會通常會設定門檻值為0.5，代表當今天輸入一大串資料進入函式後，我們會得到一個機率，當這個機率大於0.5時，我們將會預測病患擁有腫瘤
但若是我們希望只有當非常確定的時候才告訴病患他罹有腫瘤呢？(可能病患被騙的話會腦羞然後告你)，這時候我們便會將門檻值上調至0.7之類的數字。
这样的结果，会造成 precision很高，但是recall很低
相反地若是寧願錯殺也不願錯放的話，門檻值便會下調。Recall很高，Precision很低。
