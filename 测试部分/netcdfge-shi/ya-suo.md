来源：[https://www.unidata.ucar.edu/software/netcdf/workshops/2010/bestpractices/Packing.html](https://www.unidata.ucar.edu/software/netcdf/workshops/2010/bestpractices/Packing.html)

原来不明白为什么NetCDF格式数据中会有offset和scale\_facor，看了上面网址的介绍才明白，原来是为了压缩数据：

Packed Data Values

Packed data is stored in a netCDF file using a smaller data type than the original data, for example, packing doubles into shorts.

```
unpacked_value = packed_value * scale_factor + add_offset
```

* The type of the stored variable is the type of the packed data type, typically byte, short, or int.

* The type of the`scale_factor`and`add_offset`attributes should be the type that you want the unpacked data to be, typically float or double.
* To compute the scale and offset for maximum precision packing of a set of numbers, use:
  ```
    add_offset = dataMin
    scale_factor = (dataMax - dataMin) / (2^n - 1)
  ```

  where
  `n`
  is the number of bits of the packed \(integer\) data type



