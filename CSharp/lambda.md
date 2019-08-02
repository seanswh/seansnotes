[https://www.tutorialsteacher.com/linq/linq-lambda-expression](https://www.tutorialsteacher.com/linq/linq-lambda-expression)

Lambda表达式是C\# 3.0版本引入的一个功能，它是一种匿名函数的简短写法。

下图展示了匿名函数和lambda表达式的对比关系

![](/CSharp/LINQ/images/lambda-expression-1.png)

![](/CSharp/LINQ/images/lambda-expression-2.png)

一般lambda表达式不需要提供参数类型，不过如果怕参数混淆，也可以提供

```
(Student s,int youngAge) => s.Age >= youngage;
```

如果表达式中有多个语句，可以把它们用大括号括起来。

Lambda表达式可以赋值给内嵌的委托类型，如Func，Action，Predicate等。

