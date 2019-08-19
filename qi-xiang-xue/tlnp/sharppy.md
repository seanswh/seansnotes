sharppy 是近期美国NWS开源的一个探空应用程序，使用Python语言开发，已在github上开源，地址为[https://github.com/sharppy](https://github.com/sharppy)

另外，[http://sharp.weather.ou.edu/dev/](http://sharp.weather.ou.edu/dev/) 这个网址也有sharppy的简单功能介绍  
首先，需要在本机环境下安装sharppy

从github上下载sharppy以后是无法执行的，需要首先安装PySide，这个是一个QTPython的界面库，这个库目前只支持Python2.6\2.7\3.3\3.4 一开始安装了3.4，但是由于一些原因没办法安装成功，所以卸载

依赖关系：  
sharppy-&gt;PySide-&gt;Numpy  
打开数据依赖： NetCDF4-&gt;HDF5

一开始还打算自己安装Python环境，后来一上午查找各种匹配的依赖库，所以放弃，还是使用anaconda来进行安装

装好所有需要的环境以后，在sharppy的目录下执行python setup.py install报错，推断是全局路径下有中文字符串的原因，把该目录切换另外一个文件夹，再次执行python setup.py install，安装正常

--------------------后续---------------------

使用anaconda安装以后，通过VS CODE运行sharppy代码提示运行不起来，后来查看网上提供的方法，提示用pip uninstall numpy 以及 netcdf这两个包以后，再重新安装即可

-----------------再后续---------------------

调试了很多次依然有问题，后来决定从github上下载一个master代码，启动成功~~哎 看来代码还是要从github上下载呀~

-----------------------------------------------

可以打开数据，但是看不懂界面，考虑从MICAPS5类数据格式转化成OAX格式数据打开试试

但是转换完以后一直提示“arange: cannot compute length”

