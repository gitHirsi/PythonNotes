"""
@Author:Hirsi
@Time:2020/6/14
"""

"""
1.自定义异常类,继承Exception
2.抛出异常 
3.捕获该异常 ——→  raise 异常类名    获取
    作用:可以帮助报错，报错的类型是不满足程序逻辑的错误
"""


# 1
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置异常描述信息   _str_里面要用return
    def __str__(self):
        return f'你输入的密码长度是：{self.length},密码不能少于{self.min_len}位'


def main():
    # 2  抛出异常
    try:
        pwd = input('请输入密码：')
        if len(pwd) < 4:
            # 3
            raise ShortInputError(len(pwd), 4)
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')


main()
