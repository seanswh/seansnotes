来源：[https://github.com/i5ting/node-debug-tutorial\#vscode%E9%85%8D%E7%BD%AE](https://github.com/i5ting/node-debug-tutorial#vscode配置)

javascript程序的调试有点意思，一般流行的做法是安装一个Node.js程序，这个服务使用了Google的V8强大的调试器，可以通过 TCP 协议从外部访问。Nodejs提供了一个内建调试器来帮助开发者调试应用程序。

我选择使用的调试方式是node inspector方式，作为前端开发人员，我们写JS代码调试的时候一般都用FireBug或Chrome浏览器内置的调试工具，其实nodejs程序也可以这样子来调试。最新版的Node.js都会默认安装 node-inspector，所以如果要调试某一个js文件，只需要在Node.js command prompt命令行中，切换到js文件所在路径，然后输入命令：

```
node --debug-brk {yourjsname}.js
```

即可，这样就默认为这个js文件创建了一个服务进程，包括端口号和URL地址，控制台会返回类似这样的内容：

```
Debugger listening on ws://127.0.0.1:9229/9675448d-7dd3-45e9-aecd-a8fb62e15143
```

此时，可以有2种方式进行调试：

1）打开Chrome浏览器，输入地址：

```
chrome://inspect/#devices
```

此时在页面下方会出现一个Remote Target ，在Target列表中会有js文件，点击进入即可

2）使用VSCODE,进入{yourjsname}.js文件所在目录，然后修改launch.json配置文件，把request改成attach，然后点击{yourjsname}.js文件，运行即可

