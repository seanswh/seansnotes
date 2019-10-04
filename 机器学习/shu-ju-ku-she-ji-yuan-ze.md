1.避免字符串重复出现在多行之中

2.使用INT作为表格的主键

3.使用主键-外键来确定表格之间的一对多关系。

4.如果表格A与表格B之间有多对多关系，可以用增加一个表格C来破解。A的主键与C的外键关联，B的主键也与C的外键关联，C中的两个外键UNION可以作为主键。

5.So, why did we do all this?Why did we do all of these things?Why did we make these little integers? Why did we take you about JOIN?Why did we teach about many-to-many?Why did we make your data look so crazy? And that is all about **speed.**



