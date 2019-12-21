环境配置

1.MICAPS4Python工具箱支持MICAPS4.5及以上版本  
2.新增：  
  （1）扩展库：CMA.MICAPS.ExtentTool,放在MICAPS.exe同级目录下，用来对Python、JSP等后续其他语言支持进行扩展，主要包含：Python-Engine的运行时加载，以及对一些常用功能进行封装，方便Python脚本调用。  
  （2）模块 PythonEditor，该模块主要封装了一个代码输入、加载、执行的界面化窗口，后续如果该为NoteBook实现，应修改此处，包括viewmodels\views\相关界面代码。  
  （4）配置：  
      Python运行环境配置：config\extenttool\python.ini配置文件，包含了Python运行环境，conda 管理环境。其中已经安装好matplotlib包、numpy包等，可通过conda list查看具体细节。配置文件中指向的文件夹建议完整拷贝。  
      Python脚本存放路径：Script\Python目录下  
      默认初始化的时候是会ImportNumpy库和ImportMatplotlib库的，所以不需要在python  
 代码中再次加载。  
      与此同时，模块启动时会加载Scripts\Python\preLoad.py脚本，这个脚本主要是把CMA.MICAPS.ExtentTool.dll加载进Python环境中，并简写为M4.  
  此时，MICAPS4与Python运行时连接搭建完成。

注：Pythonnet解决方案为一个开源方案，可以让C\#调用Python解析器程序，原本的程序对中文支持不好，所以修改了一下原来的代码，可以让它支持中文。修改后的工程文件为Surface笔记本下的D:\Projects\pythonnet-master目录



MICAPS4需要的Python环境：

