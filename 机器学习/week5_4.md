1.Unrolling Parameters
In order to use optimizing functions such as "fminunc()", we will want to "unroll" all the elements and put them into one long vector:


```
thetaVector = [ Theta1(:); Theta2(:); Theta3(:); ]
deltaVector = [ D1(:); D2(:); D3(:) ]
```



If the dimensions of Theta1 is 10x11, Theta2 is 10x11 and Theta3 is 1x11, then we can get back our original matrices from the "unrolled" versions as follows:


```
Theta1 = reshape(thetaVector(1:110),10,11)
Theta2 = reshape(thetaVector(111:220),10,11)
Theta3 = reshape(thetaVector(221:231),1,11)

```

总之，就是为了使用现成的函数而将Matrix转化成Vector，计算出结果后再反算回来的技巧

2.Gradient Checking