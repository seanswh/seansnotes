LINQ 查询使用了C#的扩展函数技术，对IEnumerable和IQueryable两个接口的实现类进行了功能扩展。
IEnumerable<T>主要包含了内存中的数据集合，比如List\Dictionary等。
Enumerable静态类实现了IEnumerable接口的扩展，Queryable静态类实现了对 IQueryable的扩展，如下图所示：
![](/CSharp/LINQ/images/Enumerable.png)![](/CSharp/LINQ/images/queryable.png)
