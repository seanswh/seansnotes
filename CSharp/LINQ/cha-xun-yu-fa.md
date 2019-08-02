[https://www.tutorialsteacher.com/linq/linq-query-syntax](https://www.tutorialsteacher.com/linq/linq-query-syntax)  
使用LINQ进行查询主要有两种方式：  
1.Query Syntax or Query Expression Syntax  
2.Method Syntax or Method Extension Syntax or Fluent

### Query Syntax

这种语法类似于数据库中的SQL语句，只不过是在C\#或者VB代码中执行，语法为：

```
from <range variable> in <IEnumerable<T> or IQueryable<T> Collection>
<Standard Query Operators><lambda expression>
<select or groupBy operator><result formation>
```

上述语法以 `from`关键字开头，以`select`关键字结尾。下面是一个简单的例子，从一个字符串短语列表中查询带"Tutorials"的短语

```
// string collection
IList<string> stringList = new List<string>() { 
"C# Tutorials",    
"VB.NET Tutorials",  
"Learn C++",    
"MVC Tutorials" , 
"Java" };
// LINQ Query Syntax
var result = from s in stringList            
where s.Contains("Tutorials")             
select s;
```

上述代码的语法分析如下图所示：![](/CSharp/LINQ/images/linq-query-syntax.png)查询语句以from开头，后面跟着集合

