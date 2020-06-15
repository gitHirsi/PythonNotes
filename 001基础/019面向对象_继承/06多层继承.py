"""
@Author:Hirsi
@Time:2020/6/12 21:36
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
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_Master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_School_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 徒孙类
class TuSun(Prentice):
    pass

QQ=TuSun()
QQ.make_cake()
QQ.make_Master_cake()
QQ.make_School_cake()