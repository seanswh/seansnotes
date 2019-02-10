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

 2)Plot learning curves to decide if more data, more features, etc. are likely to help

另外可以透過Error analysis來人工檢驗出錯的郵件，藉此觀察是哪邊可能出了系統性的錯誤(下圖將詳細說明Error analysis)