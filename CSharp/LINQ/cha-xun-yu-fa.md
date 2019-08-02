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

上述代码的语法分析如下图所示：![](/CSharp/LINQ/images/linq-query-syntax.png)Query syntax starts with a **From**clause followed by a **Range **variable. The **From **clause is structured like `"`**`From`**`rangeVariableName`**`in`**`IEnumerablecollection"`. In English, this means, from each object in the collection. It is similar to a foreach loop:`foreach(Student s in studentList)`.

After the From clause, you can use different Standard Query Operators to filter, group, join elements of the collection.There are around 50 Standard Query Operators available in LINQ. In the above figure, we have used "where" operator \(aka clause\) followed by a condition. This condition is generally expressed using[lambda expression](https://www.tutorialsteacher.com/linq/linq-lambda-expression).

LINQ query syntax always ends with a Select or Group clause. The Select clause is used to shape the data. You can select the whole object as it is or only some properties of it. In the above example, we selected the each resulted string elements.

