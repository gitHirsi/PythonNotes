"""
@Author:Hirsi
@Time:2020/6/12
"""
"""
使用场景
    1.当方法中既不需要使用实例对象（如实例对象、实例属性）,也不需要使用类对象（如类属性、类方法、创建实例等）时，定义静态方法
    2.取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
"""
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')

ww=Dog()
ww.info_print()

Dog.info_print()