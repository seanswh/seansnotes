环境配置

1.MICAPS4Python工具箱支持MICAPS4.5及以上版本
2.新增：
  扩展库：CMA.MICAPS.ExtentTool,放在MICAPS.exe同级目录下，用来对Python、JSP等后续其他语言支持进行扩展，主要包含：Python-Engine的运行时，以及对一些常用功能进行封装，方便Python脚本调用。
  模块 PythonEditor，该模块主要封装了一个代码输入、加载、执行的界面化窗口，后续如果该为NoteBook实现，应修改此处，包括viewmodels\views\相关界面代码。
 Python运行环境：
 