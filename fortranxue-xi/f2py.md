如果说 Python 能够让你就此起飞的话，那么使用 f2py 能让你在一定程度上飞的更高更远。

f2py 是用来连接 fortran 和 python 的 python 包，可以将 fortran 源程序转换为 python 可用的程序（windows下转换为_.pyd格式文件，linux下转换为_.so文件）。编译好后，使用时直接在python中导入即可。f2py 是 numpy 的一部分，当你安装了 numpy 时就已经包含 f2py 了，其可以被用来构建 Python C/API 扩展模块，从而更容易调用 FORTRAN77/90/95 子程序，FORTRAN77 common 数据块 或 FORTRAN90/95 module 模块。

将 fortran 程序转换为 python 可用的程序是非常必要的，尤其是在进行复杂数值计算和处理大量数据时，调用 fortran 程序比使用 python 要高效的多。更为重要的是，如果已经有了 fortran 程序，可以省下很多编写相应的 python 程序的时间。

f2py是numpy自带的一个工具,只要安装了numpy,一般都会安装f2py.exe和f2py.py两个文件.f2py.exe适合在命令行中使用,而f2py.py则一般在python代码中使用.

