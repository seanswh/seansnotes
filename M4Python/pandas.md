Python中用来做科学计算，难免使用Pandas、matplotlib、Numpy等库，其中，Pandas库用来做数据规整以及计算，考虑从MICAPS4库中导出字符串使用pandas易于处理的格式。

目前来看，pandas可以处理的数据为两种，一种是一个一维数组格式的：Series，另一种是一个数据表格形式的Dateframe。

定义：[`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series)is a one-dimensional labeled array capable of holding any data type \(integers, strings, floating point numbers, Python objects, etc.\). The axis labels are collectively referred to as the **index**.

[**DataFrame**](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dsintro)** **is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.

为了能对数据有更多的描述，同时也为了能在一次访问中返回更多的结果，我们尽量使用Dateframe格式来使用M4返回的字符串结果。

为了直接使用M4返回的字符串结果，我们一般使用pandas.read\_csv方法来构造DataFrame。传入参数如果为字符串，需要注意的是每一行之间必须由“\n”分隔\(不知这么理解是否正确，目前看到的结果如此\)，每一列的分隔符可以为任意字符，在read\_csv函数中有一个参数可以指定。有关read\_csv函数的具体说明，可以参考这个[帖子](https://www.cnblogs.com/datablog/p/6127000.html)。在具体的工程中，主要使用到了如何将一个字符串转化成DataFrame所需要的结构，参考了上述帖子后发现，有2个参数可以实现：sep=":"以及lineterminator=";"

另外一个问题，是返回的字符串index需要转化成datetime格式，pandas内置了to\_datetime函数可以实现上述结构，但同时又有另一个问题，就是默认返回的字符串如果没有“表头”，那pandas就会默认让第一行作为表头，这个与实际数值不匹配，因此改造了M4的返回结构，增加了一个表头，返回结果如下面示意所示：

“time:value;19082408:12.27;19082411:11.12;19082414:11.22;19082417:11.91;19082420:13.84;19082423:13.04....."其中，time:value就是表头，代表后面的每一组都是"时间:值"格式

最终：使用如下函数：

df=pd.read\_csv\(sio,sep=":",lineterminator=";",dtype={'time':str,'value':float},index\_col=0\)

read\_csv函数中,dtype的作用是指定表头的每一列的类型，如果不设置这个参数，那么上面的19082408就会被识别成int型

index\_col=0就是说要让time列作为索引，否则pandas就会强制安排一个从0开始的索引值了

