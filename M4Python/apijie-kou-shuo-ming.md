面向Python开发的M4扩展函数，在MICAPS4 Python工具箱启动的时候已经预先加载，并且模块名称为M4，因此在使用的时候要注意以M4.开头

1. 基础函数类

   1. `AddFileToM4(string rawpath,string filepattern = "", string stylekey = "")：`MICAPS中打开数据，rawpath为数据路径，支持文件绝对路径以及MDFS路径。filepattern\(可选\)，如果rawpath为全局路径，则该项不起作用，如果rawpath指向目录，则filepatter打开的文件名格式\(\*.000或\*.024\);stylekey\(可选\)，文件打开样式
   2. `ILayer GetILayerFromURI(string raw_path, string filepattern = "")`:根据路径加载数据，并返回新增加的图层。参数含义与AddFileToM4相同。（考虑删除）
   3. IDataProvider GetProviderFromILayer\(ILayer layer\)：根据ILayer，返回数据源DataProvider
   4. DisposeLayer\(ILayer layer\)：删除某一图层并释放其资源
   5. DisplayLayerInMICAPS\(ILayer layer\)：添加某一图层并显示
   6. 

2. 站点数据类

   1. string ElementListConvert\(string rawList, string database\)：把MDFS中的站点属性列表转换成CIMISS对应的属性列表.rawlist：站点属性列表，以”，“分隔，如”温度，海平面气压“；database：站点所在的CIMISS表名称。详细可查看mdfs\_obselems\_pair.json文件中的说明信息。

3. 格点数据类



