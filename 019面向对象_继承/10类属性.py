"""
@Author:Hirsi
@Time:2020/6/12
"""
"""
类属性:
    1.设置  2.修改  3.获取
    结论:类属性只能通过类修改，不能通过对象修改，如果通过对象修改，就是创建了一个与类属性同名的实例属性
"""

class Dog(object):
    # 设置类里面属性的值
    tooth = 100


ww = Dog()
hh = Dog()


# 修改类属性
Dog.tooth=200
# ww.tooth=200
# hh.tooth=300

# 获取类属性
print(Dog.tooth)
print(ww.tooth)
print(hh.tooth)