面向Python开发的M4扩展函数，在MICAPS4 Python工具箱启动的时候已经预先加载，并且模块名称为M4，因此在使用的时候要注意以M4.开头

1. 基础函数类

   1. `ILayerAddFileToM4(string rawpath,string filepattern = "", string stylekey = "")：`MICAPS中打开数据，rawpath为数据路径，支持文件绝对路径以及MDFS路径。filepattern\(可选\)，如果rawpath为全局路径，则该项不起作用，如果rawpath指向目录，则filepatter打开的文件名格式\(\*.000或\*.024\);stylekey\(可选\)，文件打开样式
   2. `ILayer GetILayerFromURI(string raw_path, string filepattern = "")`~~:根据路径加载数据，并返回新增加的图层。参数含义与AddFileToM4相同。（考虑删除）~~
   3. IDataProvider GetProviderFromILayer\(ILayer layer\)：根据ILayer，返回数据源DataProvider
   4. DisposeLayer\(ILayer layer\)：删除某一图层并释放其资源
   5. DisplayLayerInMICAPS\(ILayer layer\)：添加某一图层并显示
   6. string GetAllLayersName\(\)：获取M4当前窗口的所有图层名称

   7. ILayer GetLayerAccdLayerName\(string name\)：根据图层名称获得当前激活窗口中的图层。

   8. ~~ILayer DisplayFileinMICAPS\(string filePath\)：显示指定路径下的文件，并返回对应的图层。~~

   9. string GetLayerType\(ILayer layer\)：获得图层类型。包含；feature/grid/raster/coposite/unknown

   10. string GetProviderType\(IDataProvider provider\):获得provider的类型。包含：feature/grid/raster。

2. 站点数据类

   1. string ElementListConvert\(string rawList, string database\)：把MDFS中的站点属性列表转换成CIMISS对应的属性列表.rawlist：站点属性列表，以”，“分隔，如”温度，海平面气压“；database：站点所在的CIMISS表名称。详细可查看mdfs\_obselems\_pair.json文件中的说明信息。
   2. string GetElemsFromOBSTable\(string tablename\)：返回指定CIMISS站点表中全部的要素名称，以“CIMISS编码:中文属性名;CIMISS编码:中文属性名;"方式排列
   3. string GetObsSerialFromMDFS\(string stationID, string table\_name, string elementList, string startTime, string endTime, int interval\)：获取观测时序。stationID:站点ID。\_table\_name：表名称，可参考mdfs\_obselems\_pair.json文件；elementList：要素列表；startTime:时序起始时间；endTime：时序结束时间。interval：时序间隔时间（小时）
   4. CreateStationLayer\(string name,string content\)：创建站点图层。name：图层名称。content：图层信息（格式：name@lon:lat:alt:value;）

3. 格点数据类

   1. string GetModelTlnpFromMDFS\(string modelType,
       string fileDesc, int duration, float lontitude, float latitude\)：返回模式TLNP结果。modelType：模式类型\(ecmwf、\);fileDesc:8.3格式文件名，YYMMDDHH代表起报时间；duration：预报时效；lontitude，latitude：站点经纬度
   2. string GetModelSerialFromMDFS\(float lon, float lat, string path,
       string str\_fcstTime, int duration, int interval, int start\_duration = 0\)：获取模式时序结果（只支持MICAPS分布式数据路径）。lon,lat:经纬度信息。path：MDFS中该模式的路径。str\_fcstTime：起报时间\(yyyyMMddHH格式\)；duration：预报时效；interval：时序时间间隔；start\_duration：时序起始时效。
   3. GridData\[\] GetGridsFromGridLayer\(ILayer layer\)：获取图层中的格点值。
   4. float\[\] GetFloatArrayFromGridData\(GridData griddata\)：从GridData中返回float数组。
   5. float\[\] GetGridInfoFromLayer\(IGridDataLayer layer,
       out int xsize,out int ysize, out float startlon, out float endlon, 
      out float startlat, out float endlat,out float lon\_interval,out float lat\_interval,
       int index = 0\)：获取图层中的格点值，同时返回格点信息。
   6. float\[\] GetFloatFromPath\(string gridPath\)：从格点数据中返回float\[\]数组

   7. IGridDataLayer CreateNewLayerAcrdFloatArray\(float\[\] float\_array,int xsize,  
                  int ysize,float startlon,float endlon,float startlat,float endlat,string description\)：利用一个float数组创造一个格点数据图层。

   8. static void UpdateLayerWithAnalysisValue\(IGridDataLayer layer,string analysisvalue\)：设置格点图层的等值线分析值。analysisvalue：等值线值以逗号分隔。

   9. UpdateLayerWithAnalysisRange\(IGridDataLayer layer, string analysisvalue\)：设置格点图层的等值线分析值。analysisvalue格式为“起始分析值，终止分析值:间隔"



