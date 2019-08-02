# LINQ Method Syntax\([https://www.tutorialsteacher.com/linq/linq-method-syntax](https://www.tutorialsteacher.com/linq/linq-method-syntax)\)

Method 语法使用扩展方法来进行查询，如下是示例代码程序：

```
// string collection
IList<string> stringList = new List<string>() {
  "C# Tutorials",    
  "VB.NET Tutorials",    
  "Learn C++",   
  "MVC Tutorials" ,    
  "Java" 
  };
  // LINQ Query Syntax
  var result = stringList.Where(s => s.Contains("Tutorials"));
```

上述代码解析为：

![](/CSharp/LINQ/images/linq-method-syntax.png)

method syntax comprises of extension methods and Lambda expression. The extension method **Where\(\) **is defined in the Enumerable class.

If you check the signature of the Where extension method, you will find the Where method accepts a [predicate](https://www.tutorialsteacher.com/csharp/csharp-predicate) delegate as Func&lt;Student, bool&gt;. This means you can pass any delegate function that accepts a Student object as an input parameter and returns a Boolean value as shown in the below figure. The lambda expression works as a delegate passed in the Where clause.

