PythonTool工具箱问题记录  
8月22日

~~1.ipynb文件可以打开，但是无法保存，使用压缩包内的html以及Module.PythonTool.dll全部替换可以保存，但是dll用本地代码覆盖之后就无法保存了，需要调试解决（已解决）~~

8月23日，上述无法保存的问题已解决，通过使用发现如下问题：

1. ~~执行完一个code section后，再添加code section，就会出错，所有的section添加都应该放在当前激活section的下面，而不是覆盖~~
2. 没有办法在当前激活的section下增加代码或markdown，只能加在最后面
3. ~~返回结果里也没有回车换行显示~~
4. 窗口大小水平方向调整后，控件大小不变，留白会越来越大
5. ~~保存ipynb文件后再打开，所有回车换行丢失\(已解决\)~~
6. ~~左侧树形图里没有当前正在编辑的激活状态信息~~
7. markdown目前不支持markdown语法
8. ~~所有的markdown section在加载的时候就应该被执行~~
9. ~~Ctrl+S保存快捷键~~
10. 每一个section执行的时候，要先把原来的输出清空，然后执行，最后把结果填上
11. ~~如果使用的是IPython的javascript实现，考虑把%matplotlib inline也实现（用的是其他办法）~~
12. ~~支持image对象的显示~~
13. ~~Image对象会被拉伸，建议保留原始尺寸~~
14. ~~同一代码修改后输出不同的Image，执行脚本后，界面不更新~~
15. ~~ipynb加载以后只执行Markdown中的部分，python脚本先不执行~~
16. ~~无法在markdown section下面再添加markdown section~~
17. ~~markdown中\# 与\#\# 字体大小一样了，实际是有区别的~~

2020.2.13

