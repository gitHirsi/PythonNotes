"""
@Author:Hirsi
@Time:2020/6/11 22:06
"""

"""
1.定义类，初始化属性，被烤和添加调料的方法，显示对象信息的str
2.创建对象，调用实例方法
"""


# 1
class SweetPotato():
    def __init__(self):
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []

    def cook(self, time):
        """烤地瓜的函数"""
        # 计算地瓜整体烤过的时间
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'

    def add_condiments(self,condiments):
        """加调料的函数"""
        self.condiments.append(condiments)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟,它是{self.cook_static}，它的调料有{self.condiments}'

# 创建对象,调用烤地瓜方法，看地瓜状态
digua1=SweetPotato()
digua1.cook(2)
print(digua1)

digua1.cook(2)
digua1.add_condiments('孜然')
print(digua1)

digua1.cook(2)
digua1.add_condiments('胡椒粉')
print(digua1)

digua1.cook(2)
print(digua1)


