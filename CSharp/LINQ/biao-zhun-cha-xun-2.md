### 过滤操作符

过滤操作符会将原始序列\(集合\)中的要素进行按条件过滤

| Filtering Operators | Description |
| :--- | :--- |
| [Where](https://www.tutorialsteacher.com/linq/linq-filtering-operators-where#where) | Returns values from the collection based on a predicate function |
| [OfType](https://www.tutorialsteacher.com/linq/linq-filtering-operators-oftype) | Returns values from the collection based on a specified type. However, it will depend on their ability to cast to a specified type. |

Where 操作符

#### Query Syntax

可以使用任何符合Func type 的委托，注意该委托的返回值为false如下段代码所示：

```
Func<Student,bool> isTeenAger = delegate(Student s) {      
return s.Age > 12&& s.Age< 20;
                  };
var  filteredResult = from s in studentList                 
                   where  isTeenAger(s)
                select s;
```

#### Method Syntax

与Query Syntax不同，Method Syntax需要传入完整的lambda函数体，Where函数支持一个重载函数，参数可以使用集合的索引var

```
 filteredResult = studentList.Where((s, i) => { 
            if(i % 2 ==  0)// if it is even element
                return true;
                   return false;});
foreach (var std in filteredResult)
           Console.WriteLine(std.StudentName);
```



