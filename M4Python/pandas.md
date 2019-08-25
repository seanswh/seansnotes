Python中用来做科学计算，难免使用Pandas、matplotlib、Numpy等库，其中，Pandas库用来做数据规整以及计算，考虑从MICAPS4库中导出字符串使用pandas易于处理的格式。

目前来看，pandas可以处理的数据为两种，一种是一个一维数组格式的：Series，另一种是一个数据表格形式的Dateframe。

定义：[`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series)is a one-dimensional labeled array capable of holding any data type \(integers, strings, floating point numbers, Python objects, etc.\). The axis labels are collectively referred to as the **index**.

[**DataFrame**](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dsintro)** **is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.

为了能对数据有更多的描述，同时也为了能在一次访问中返回更多的结果，我们尽量使用Dateframe格式来使用M4返回的字符串结果。

为了直接使用M4返回的字符串结果，我们一般使用pandas.read\_csv方法来构造DataFrame。传入参数如果为字符串，需要注意的是每一行之间必须由“\n”分隔

