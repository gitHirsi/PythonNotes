"""
@Author:Hirsi
@Time:2020/6/11 21:47
"""

"""
_str_()  :定义_str_方法后，打印对象时，就会打印容这个方法中return的数据
"""


class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return '冰箱说明书'


haier = Washer(450, 500)
print(haier)
