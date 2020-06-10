"""
@Author:Hirsi
@Time:2020/6/10 22:30
"""

# r 表示只读，没有文件会报错

# w 表示只写，没有文件会新建 ，执行写入，会覆盖原有内容

# a 表示追加，没有文件会新建,会在原有内容上，追加新内容
# f = open('test.txt', 'a')
# f.write('boom')
# f.close()

# 访问模式可以省略，省略了默认 r
f1 = open('test.txt')
f1.close()