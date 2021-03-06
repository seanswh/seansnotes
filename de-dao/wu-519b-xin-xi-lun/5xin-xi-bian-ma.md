本文介绍人类是如何用信息编码创造数字和文字的

早期人类了解和需要传播的信息是很少的，因此并不需要语言和数字，只需要发出不同的叫声或者做些不同的手势和肢体接触即可。再往后，需要传递的信息逐渐增加，因此使用语言，同时还有对简单数字的编码，如5个手指就代表数字5.历史上一些文明使用20进制，如玛雅文明。当数字再增加以后，就有了对数字的高级编码——用有限的数字组合表示更多的数。

比如要表达100个数字，一种方式是对每一个数字都进行独一的编码，让他们一一对应；另一种方式是只设计几种编号，然后通过组合来表达。这两种方法在信息论中是**等价的，计算如下：**

从100个数中挑出一个，不确定性是100选一，用上节的公式算出，结果为ln100=6.65,也就是说需要6.65比特信息就能确定100个数中的一个。如果我们**使用十进制编码**，每个符号所代表的信息量是ln10=3.325比特，但是十进制代表100个数字，需要两两组合，就是说这种方式下，一个符号无法消除不确定性，因此需要2个符号，加起来还是6.65比特。如果使用2进制，它所包含的信息只有ln2=1比特，但是需要他表达100个数，需要7位码长（其实是6.65）位。

符号越少，意味着码长越长，所以，**对数字的各种编码其实是等价的，无非是平衡编码复杂性和编码长度之间的关系**。编码越复杂，码长会变短，但是编码系统会很复杂，学习门槛会很高。

由于码长必须为整数，因此可以得到如下公式：

**编码长度&gt;= 信息熵\(信息量\)/每一个码的信息量**

上面提到的二进制就是一个列子，二进制的码长为7，是取整的结果。香农证明了，如果我们的编码系统足够巧妙，上面的等号是可以成立的。

文字的产生与数字一样，也是随着需要编码的物品逐渐增加造成的。

今天虽然大家都能识文断字，但是有的人掌握信息多，有的人掌握信息量少，这就造成了很大的不平等。对于个体来说，改变自身获取信息的能力要比改变整个社会的不平等容易的多。

