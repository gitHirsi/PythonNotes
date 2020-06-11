"""
@Author:Hirsi
@Time:2020/6/11 21:53
"""
'''
_del_()  :当删除对象时，python解释器也会默认调用_del_()方法
'''

class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __del__(self):
        print('对象已经删除！')


haier = Washer(450, 500)

