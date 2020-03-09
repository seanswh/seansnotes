在M4的Python工具箱中，关于格点类数据的处理，需要将MICAPS4中的GridData转换成Python中的ndarray数组。

通常做法是调用函数floatArray = M4.GetFloatArrayFromGridData\(griddata\) 获取到一维数组，然后通过ndarray=np.fromiter\(floatArray,dtype=np.float32\) 将float数组转化成ndarray对象，这个ndarray对象是一维数组，如果需要转换成二维数组，使用ndarray.reshape\(griddata.YSize,griddata.XSize\)，注意，这里一定**是行数在前，列数在后，**如下例**：**

```
a = numpy.arange(1,101,1)
a.reshape(4,25)
array([[  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,
         14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25],
       [ 26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50],
       [ 51,  52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,
         64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75],
       [ 76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,
         89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99, 100]])
```

可以看出，上面代码执行后生成一个4行，每行25个元素的二维矩阵。

当二维数组操作完后，需要再将ndarray数组返回，如果数组是二维矩阵，则需要使用

floatArray = ndarray.flatten\(\)函数重新生成float数组，再将该数组传递回MICAPS4即可。

