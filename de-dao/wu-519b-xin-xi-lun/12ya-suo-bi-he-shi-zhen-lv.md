压缩过的图片，恢复回来似乎没有原图清晰了，这是怎么回事？信息的压缩是否都会让一部分信息丢失掉？

信息压缩是要考虑失真率的，而这种取舍平衡的原则，其实是我们都应该学习和了解的。

香农第一定律指出，任何编码的长度都不会小于信息熵，也就是通常会大于等于信息熵，当然最理想的就是能等于。如果编码长度太短，小于信息熵，就会出现损失信息的现象。

因此，信息熵是告诉信息处理的人，做事情的边界，就如同不能试图逾越热力学第二定律发明永动机一样，大家在压缩信息时，如果想要无损，就不能逾越香农给的这个边界。

理解了这一点以后，我们就知道无论是语音，还是图像、视频，都有两类的压缩方式，一类就是无损压缩。比如我们昨天说的通过傅里叶变换和离散余弦变换将音频和图像信息变成频率信息，再用类似哈夫曼编码进行压缩，这是不会丢失信息的。

其实我们生活中大量应用到的都是有损压缩，只不过我们感受不到，这就说明压缩很好地考虑到了失真率。

世界上很多时候没有最好的技术方案，只能根据场景找到合适的，因此做事的目的性很重要。这是第一个原则。我们还知道信息的作用是消除不确定性，那么反过来，丢失了一部分信息，一定会增加不确定性。用的信息少，永远不可能做得和原来一样好，这是第二个原则，大家一定要记清楚。

除了要考虑目的，考虑到信息数量之外，第三个原则是，在压缩信息时，有时要看应用场景。还是以语音压缩为例，在语音通话时，牺牲一定的讲话人的口音，问题不大，因为它的目的是传递话音中的信息。但是，在进行声纹识别时，情况就正好相反，那个人说了一句什么话不重要，重要的是知道他是谁。

那么高比例的信息压缩到底是压缩掉了什么信息？简单地讲，就是压缩掉了高频信息。进一步说，人通常能够听到20赫兹到2万赫兹的声音，但是人发音的范围只有300赫兹到4000赫兹左右，因此任何高于4000赫兹的语音信号，就被过滤了。

2012年，约翰·霍普金斯大学的科学家们发表了一种遗传压缩算法，在不丢失任何信息的情况下，压缩比达到了1000倍。这件事对于普及基因测序很有意义。约翰·霍普金斯大学的科学家们是怎么做的呢？简单地讲，他们的方法和视频压缩的方法很相似——考虑到人的很多基因是相同的， 只需要存储有差异的基因即可。
