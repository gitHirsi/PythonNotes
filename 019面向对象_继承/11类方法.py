"""
@Author:Hirsi
@Time:2020/6/12
"""

"""
1.当方法中需要使用类对象（如访问私有类属性）时，定义类方法
2.类方法一般和类属性配合使用
"""

class Dog(object):
    __tooth=100

    # 创建类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

ww=Dog()
tooth = ww.get_tooth()
print(tooth)
