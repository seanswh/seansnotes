信息中心提供了Python的二次开发环境，现部署在D:\Projects\Python\_Project\meteocloud路径下，通过Visual Studio Code 集成。

大数据云平台提供了一个同一的综合数据信息获取方式，可以根据信息逐层得到需要访问的内容：

1. [http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomTypeList](http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomTypeList)

这个接口提供了云平台数据环境中所有的数据种类，包括地面、高空、海洋、农气等，而且还提供了数据种类的dataclassid

2.http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getDataListByClassIdAndLimit&dataClassId=RADA&apiUserId=NMIC\_XTS\_nixl







[http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomapiListByDataCode&dataCode=SURF\_CHN\_MUL\_HOR](http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomapiListByDataCode&dataCode=SURF_CHN_MUL_HOR)

其中，dataCode为数据格式编码，如：SURFCHN\_MUL\_HOR是中国地面逐小时资料

