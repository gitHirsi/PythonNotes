"""
@Author:Hirsi
@Time:2020/6/15
"""


class Student(object):
    def __init__(self, name, gander, tel):
        self.name = name
        self.gander = gander
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gander},{self.tel}'

# hh=Student('hh','男','123456')
# print(hh)