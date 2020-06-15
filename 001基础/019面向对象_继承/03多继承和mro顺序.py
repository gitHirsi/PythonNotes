"""
@Author:Hirsi
@Time:2020/6/11 23:29
"""

"""
多继承：一个子类同时继承多个父类
_mro_：子类所继承的父类的顺序
"""
# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu='《独门煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '《乾坤煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 徒弟类继承师傅类和学校类    结论:如果一个类继承多个父类，如果多个父类有同名属性和方法，则优先继承第一个父类的
class Prentice(School,Master):
    pass

hirsi=Prentice()

hirsi.make_cake()

print(Prentice.__mro__)