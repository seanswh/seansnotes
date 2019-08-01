LINQ（[https://www.tutorialsteacher.com/linq/linq-api](https://www.tutorialsteacher.com/linq/linq-api)）

只要是实现了[IEnumerable&lt;T&gt;](http://msdn.microsoft.com/en-us/library/9eekhta0%28v=vs.110%29.aspx)或者[IQueryable&lt;T&gt;](https://docs.microsoft.com/en-us/dotnet/api/system.linq.iqueryable-1)接口的类，都可以使用LINQ进行查询。

C\#使用**扩展函数**的方式对IEnumerable和IQueryable的接口实现扩展，Enumerable类和Queryable两个静态类实现了对上述接口的LINQ查询扩展。

Enumerable类

该类实现了对IEnumerable接口的扩展，下图绘制了所有被扩展的内置IEnumerable&lt;T&gt;的类

![](/CSharp/LINQ/images/Enumerable-extension-methods.png)

下图显示了所有扩展函数



