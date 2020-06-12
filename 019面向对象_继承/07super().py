"""
@Author:Hirsi
@Time:2020/6/12 21:53
"""
"""使用super()可以自动查找父类，调用顺序遵循_mro_类属性的顺序，比较适合单继承使用"""

# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '《师傅煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 学校类
class School(Master):
    def __init__(self):
        self.kongfu = '《学校煎饼果子大法》'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
        super().__init__()
        super().make_cake()


# 徒弟类
class Prentice(School):
    def __init__(self):
        self.kongfu = '《独创煎饼果子大法》'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # def make_Master_cake(self):
    #     Master.__init__(self)
    #     Master.make_cake(self)
    #
    # def make_School_cake(self):
    #     School.__init__(self)
    #     School.make_cake(self)

    # 一次性调用父类School和Master的方法
    def make_old_cake(self):
        #方法一
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        #方法二
        super().__init__()
        super().make_cake()

hirsi=Prentice()
hirsi.make_old_cake()

