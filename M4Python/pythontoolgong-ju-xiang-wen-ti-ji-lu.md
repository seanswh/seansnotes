PythonTool工具箱问题记录  
8月22日

1.ipynb文件可以打开，但是无法保存，使用压缩包内的html以及Module.PythonTool.dll全部替换可以保存，但是dll用本地代码覆盖之后就无法保存了，需要调试解决

8月23日，上述无法保存的问题已解决，通过使用发现如下问题：

1.窗口大小水平方向调整后，控件大小不变，留白会越来越大

2.保存ipynb文件后再打开，所有回车换行丢失\(已解决\)

8.返回结果里也没有回车换行显示

3.左侧树形图里没有当前正在编辑的激活状态信息

4.没有办法在当前激活的section下增加代码或markdown，只能加在最后面

5.markdown目前不支持markdown语法

6.所有的markdown section在加载的时候就应该被执行

7.Ctrl+S保存快捷键

9.每一个section执行的时候，要先把原来的输出清空，然后执行，最后把结果填上

10.如果使用的是IPython的javascript实现，考虑把%matplotlib inline也实现

