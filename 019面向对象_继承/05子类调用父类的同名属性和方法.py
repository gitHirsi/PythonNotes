"""
@Author:Hirsi
@Time:2020/6/12 9:54
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '《师傅煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '《学校煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '《独创煎饼果子大法》'

    def make_cake(self):
        # 加自己初始化的原因：如果不加，kongfu的值是上一次调用init内的kongfu的属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_Master_cake(self):
        # 父类类名.函数
        # 再次调用初始化原因:这里要调用父类的同名方法和属性，而属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_School_cake(self):
        School.__init__(self)
        School.make_cake(self)


hirsi = Prentice()
# hirsi.make_cake()
hirsi.make_Master_cake()
hirsi.make_School_cake()
hirsi.make_cake()
