LINQ的定义

LINQ\(Language Intergated Query\)——语言集成查询，是C\#下设计的从不同内存结构进行数据查询的语法\(is uniform query syntax in C\# and VB.NET to retrieve data from different sources and formats.\)LINQ使得用同一种类似于SQL的语法来检索不同结构的数据，只要该结构实现了_IEnumerable_或者_IEnumerable&lt; T &gt;_接口即可。如下图所示：

![](/assets/linq-usage.png)

LINQ语句查询返回的都是统一的对象结果，这样一方面可以对结果使用面向对象的函数调用，另一方面也将不同内存数据集中的结果进行了格式的统一转化。

LINQ有一个特性是延迟执行，它是指查询操作并不是在查询运算符定义的时候执行，真正**使用集合中的数据时**才执行。

