matplotlib是Python中的一个很重要的绘图工具，MICAPS4的Python工具箱中也加入了matplotlib的加持。

但是有一个问题，就是每次matplotlib中，每次调用show函数的时候，都会弹出一个对话框，看起来有点不协调。

Jupyter Notebook中，在使用了“神奇的"%matplotlib inline以后，所有的图片都是直接在“输出”栏中进行显示的，查询相关资料以后，发现这条语句是IPython 环境中定义的内置函数，由于我们M4中的Python编辑器是自定义的网页，所以暂时不考虑IPython特制的这个内置函数

换一个思路解决问题，是使用PyDic Local变量。首先改变matplotlib的输出图片类型，![](/assets/1.PNG)这个与PyDic Local变量无关.

下面修改PythonConnection类，增加了一个局部变量 PyDict local\_dic，这个是一个很有意思的功能，搭配类中的PopLocal和PushLocal函数使用，另外，注意下面这个函数：



