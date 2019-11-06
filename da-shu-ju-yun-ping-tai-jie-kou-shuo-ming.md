大数据云平台提供了一个同一的综合数据信息获取方式，可以根据信息逐层得到需要访问的内容：

1. [http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomTypeList](http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomTypeList)

这个接口提供了云平台数据环境中所有的数据种类，包括地面、高空、海洋、农气等，而且还提供了数据种类的dataclassid

2.[http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getDataListByClassIdAndLimit&dataClassId=UPAR&apiUserId=NMIC\_XTS\_nixl](http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getDataListByClassIdAndLimit&dataClassId=RADA&apiUserId=NMIC_XTS_nixl)

这个接口提供了根据ClassID，获取某一类资料下的全部数据子类，比如上述接口可以获取“高空”类下的数据子类信息，包括闪电定位\(AI专题库\)、全球高空定时值资料等，而且每一个子类还提供了对应的dataCode值。

3.[http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomapiListByDataCode&dataCode=SURF\_CHN\_MUL\_HOR](http://10.40.17.34:8009/cmadaas/music/api?interfaceId=getCustomapiListByDataCode&dataCode=SURF_CHN_MUL_HOR)

最后，通过上述的dataCode值，可以获取某一个子类数据下所有要素信息。其中，dataCode为数据格式编码，如：SURFCHN\_MUL\_HOR是中国地面逐小时资料

