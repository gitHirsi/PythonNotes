"""
@Author:Hirsi
@Time:2020/6/11 23:44
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '《独门煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '《乾坤煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 子类重写父类的同名属性和方法  结论: 如果子类和父类有同名属性和方法，子类创建对象调
#                                      用属性和方法的时候，调用的是子类里面的
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '《独创煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


hirsi = Prentice()

hirsi.make_cake()
