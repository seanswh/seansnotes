类的定义

```
#类定义
class PartyAnimal:
    x = 0
    def party(self):      函数定义
        self.x = self.x+1
        print('so far',self.x)
    def __del__(self):    析构函数
        print('I am destructed',self.x)
    def __init__(self):   构造函数
        print('I am constructed')
an = PartyAnimal()
an.party()
an.party()
an = 42
```

```
class FootballFan(PartyAnimal): 子类
    points= 0                    子类的属性
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print("points",self.points)
```

![](/assets/6.png)

