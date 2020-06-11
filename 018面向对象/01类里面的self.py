"""
@Author:Hirsi
@Time:2020/6/11 16:15
"""

# 定义洗衣机类
class Washer():
    def wash(self):
        print(self)
        print('洗衣服了！')

# 创建对象/类的实例
xiaotiane = Washer()

# 调用方法
xiaotiane.wash()


print(xiaotiane)

# 哪个对象调用类里面函数，self就是谁