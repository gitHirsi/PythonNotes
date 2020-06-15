"""
@Author:Hirsi
@Time:2020/6/14
"""
"""
1.捕获异常
2.else和finally
"""

# # 捕获指定异常类型
# try:
#     print(i)
#     # print(1/0)
# except NameError:
#     print('捕获指定异常显示有错误!')
#
# # 捕获多个指定异常
# try:
#     print(1/0)
# except (NameError,ZeroDivisionError):
#     print('捕获多个指定异常显示有错误！')
#
# # 捕获异常描述信息
# try:
#     print(num)
# except (NameError,ZeroDivisionError) as result:
#     print('有错误')
#     print(f'错误信息:{result}')
#
# # 捕获所有异常
# try:
#     print(1/0)
# except Exception as result:
#     print(f'错误信息：{result}')
#
#
# # else  :没有异常时要执行的代码
# try:
#     print('Python')
# except Exception as result:
#     print(result)
# else:
#     print('我是else，是没有异常的时候执行的代码')

# finally  :无论是否异常都要执行的代码
try:
    f=open('test.txt', 'r')
    print('r')
except Exception as result:
    f=open('test.txt', 'w')
    print('w')
else:
    print('这是else里面，表示没有错误!')
finally:
    print('最后的finally')
    f.close()








