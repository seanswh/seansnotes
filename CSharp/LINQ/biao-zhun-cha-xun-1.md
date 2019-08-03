LINQ的标准操作\(Standard Query Operators\)[https://www.tutorialsteacher.com/linq/linq-standard-query-operators](https://www.tutorialsteacher.com/linq/linq-standard-query-operators)

标准化的查询操作被定义在`System.Linq.Enumerable`and`System.Linq.Queryable`类中![](/CSharp/LINQ/images/standard-query-operators-linq-query-syntax.png) 标准化的查询操作符

![](/CSharp/LINQ/images/standard-query-operators-linq-method-syntax.png)扩展函数

注意，标准化的查询操作符在编译时会被转化成扩展函数，因此本质上来说，它俩一样。

按照类型，标准化的查询操作符可以分成以下几类


| Classification | Standard Query Operators |
| :--- | :--- |
| Filtering | Where, OfType |
| Sorting | OrderBy, OrderByDescending, ThenBy, ThenByDescending, Reverse |
| Grouping | GroupBy, ToLookup |
| Join | GroupJoin, Join |
| Projection | Select, SelectMany |
| Aggregation | Aggregate, Average, Count, LongCount, Max, Min, Sum |
| Quantifiers | All, Any, Contains |
| Elements | ElementAt, ElementAtOrDefault, First, FirstOrDefault, Last, LastOrDefault, Single, SingleOrDefault |
| Set | Distinct, Except, Intersect, Union |
| Partitioning | Skip, SkipWhile, Take, TakeWhile |
| Concatenation | Concat |
| Equality | SequenceEqual |
| Generation | DefaultEmpty, Empty, Range, Repeat |
| Conversion | AsEnumerable, AsQueryable, Cast, ToArray, ToDictionary, ToList |



