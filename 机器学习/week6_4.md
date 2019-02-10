实战篇

制作一个垃圾邮件过滤器
（1）判断垃圾邮件的规则，是识别原始邮件中是否有一些敏感词汇，我们可以构建一个含10000~50000个这样词汇的向量，当包含某一个敏感词汇时，向量值为1，否则为0，如下图所示：
![](/机器学习/images/56.png)
随后我们可以训练模型，以识别某一邮件是否为垃圾邮件。
那么如何提升我们的过滤器的识别质量呢？
 1）Collect lots of data (for example "honeypot" project but doesn't always work)
 2）Develop sophisticated features (for example: using email header data in spam emails)
 3）Develop algorithms to process your input in different ways (recognizing misspellings in spam).
 而以上三种方式很难说哪个更加有效。
 
（2）Error Analysis
 建议用以下顺序来解决机器学习问题：
 
 1)可以先快速的建立一個簡單所需的演算法，然後用其驗證cross-validation的資料

 2)Plot learning curves to decide if more data（variance problem）, more features(bias problem), etc. are likely to help

 3)透過Error analysis來人工檢驗出錯的郵件，藉此觀察是哪邊可能出了系統性的錯誤(下圖將詳細說明Error analysis)
 
 假設在cross validation set中我們發現有100個分類錯誤，接下來以人工的方式檢驗：分類這些錯誤的資料(像是釣魚郵件)、或許可以改善的特點(不尋常的字母编写方式或邮件路由地址等)
 最后，我们应该使用定量化的评估结果。For example if we use stemming, which is the process of treating the same word with different forms (fail/failing/failed) as one word (fail), and get a 3% error rate instead of 5%, then we should definitely add it to our model. However, if we try to distinguish between upper case and lower case letters and end up getting a 3.2% error rate instead of 3%, then we should avoid using this new feature.
 
 we should try new things, get a numerical value for our error rate, and based on our result decide whether we want to keep the new feature or not.