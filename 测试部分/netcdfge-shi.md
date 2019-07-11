原文地址：https://cslocumwx.github.io/blog/2015/01/19/python-netcdf-part1/
netCDF数据格式的定义初衷是为了尽可能的使用一种通用的格式涵盖所有的数据种类，尤其是对于气象和气候科研用户来说更为便捷。总的来说，这个数据格式有以下的优点：
1）Self-Describing. A NetCDF file includes information about the data it contains.
2）Portable. A NetCDF file can be accessed by computers with different ways of storing integers, characters, and floating-point numbers.
3）Scalable. A small subset of a large dataset may be accessed efficiently.
4）Appendable. Data may be appended to a properly structured NetCDF file without copying the dataset or redefining its structure.
5）Sharable. One writer and multiple readers may simultaneously access the same NetCDF file.
6）Archivable. Access to all earlier forms of NetCDF data will be supported by current and future versions of the software.
