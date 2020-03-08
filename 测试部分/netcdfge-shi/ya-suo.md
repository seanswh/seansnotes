来源：[https://www.unidata.ucar.edu/software/netcdf/workshops/2010/bestpractices/Packing.html](https://www.unidata.ucar.edu/software/netcdf/workshops/2010/bestpractices/Packing.html)

原来不明白为什么NetCDF格式数据中会有offset和scale\_facor，看了上面网址的介绍才明白，原来是为了压缩数据：

Packed Data Values

Packed data is stored in a netCDF file using a smaller data type than the original data, for example, packing doubles into shorts.

```
unpacked_value = packed_value * scale_factor + add_offset
```



