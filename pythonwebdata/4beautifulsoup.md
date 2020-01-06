对于Socket信息获取来说，python有以下几种方式，根据从底层到上层的排列：

1. import socket
   socket.Send  socket.Recv
这种方法最为初级，但是可以很好地学习网络编程，这个操作类似于Telnet
2.urllib
import urllib.request
   fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
这种方式相对于socket来说，屏蔽了header,而且可以把返回的网页内容作为一个文件句柄(file handle)来使用
3. beautifulsoup