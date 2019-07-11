原文地址：https://cslocumwx.github.io/blog/2015/01/19/python-netcdf-part1/
netCDF数据格式的定义初衷是为了尽可能的使用一种通用的格式涵盖所有的数据种类，尤其是对于气象和气候科研用户来说更为便捷。总的来说，这个数据格式有以下的优点：
1）Self-Describing. A NetCDF file includes information about the data it contains.
2）Portable. A NetCDF file can be accessed by computers with different ways of storing integers, characters, and floating-point numbers.
3）Scalable. A small subset of a large dataset may be accessed efficiently.
4）Appendable. Data may be appended to a properly structured NetCDF file without copying the dataset or redefining its structure.
5）Sharable. One writer and multiple readers may simultaneously access the same NetCDF file.
6）Archivable. Access to all earlier forms of NetCDF data will be supported by current and future versions of the software.

# 自描述
netcdf文件内包含了元信息，可分为变量、纬度、属性：
1)Variables. Variables contain data stored in the NetCDF file. This data is typically in the form of a multidimensional array. Scalar values are stored as 0-dimension arrays.
2)Dimensions. Dimensions can be used to describe physical space (latitude, longitude, height, and time) or indices of other quantities (e.g. weather station identifiers).
3)Attributes. Attributes are modifiers for variables and dimensions. Attributes act as ancillary data to help provide context. An example of an attribute would be a variable's units or fill/missing values.
## 公约
过度的开放和灵活性必然会带来自定义的无序，从而造成发展和使用的无序，因此许多机构和组织建立了NetCDF的应用公约，目前主要应用的公约是 CF Conventions (Climate and Forecast：http://cfconventions.org/)

## 自描述的描述什么样的？
