代码分析

所有工程的入口当然还是在full\_gui.py中

------------SPCWindow.py

所有的启动窗口的界面相关设置，包括设置菜单、右键菜单、快捷键关联等

------------profile.py

所有的物理量计算函数

--------------------------执行顺序-------------------------------

1）full\_gui.py是入口文件，启动后会初始化界面，界面初始化时，会调用datasource.py的loadDataSources方法\(full\_gui.py 99行\)，加载出来所有默认的数据源地址。datasource.py是一个处理数据源的功能集合，包括读取相应配置生成数据源信息，对数据源进行ping已测试是否可以连接等

2）打开文件后会进入到skewApp函数。decoder.py是所有decoder类的父类，在读取文件后会依次判断解析器，其中，spcdecoder、buf\_decoder、pecan\_decoder都是decoder的一个子类。

spc_decoder.py_中的parse函数会对解码后的文件内容进行规整，然后调用profile.py中的create\_profile函数创建一个profile对象（此时还没有进行计算，只是创建了一个对象\)

随后会调用spcwindow.py中的addprofilecollection，进而调用spc\_widget的addprofilecollection函数。

在spc\_widget的addprofilecollection函数中，利用更新的profile进行updateProfs函数操作

计算**气压log值**：profile.py:301行,计算虚温：302行

