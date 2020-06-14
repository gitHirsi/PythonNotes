"""
@Author:Hirsi
@Time:2020/6/14
"""
import time

"""
1.尝试只读的方式打开test.txt，如果文件存在就读取文件内容，文件不存在就提示用户即可
2.循环读取内容时，读取的过程中检测到用户意外终止则捕获异常，并提示用户
"""

try:
    f = open('test.txt', 'r')
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            time.sleep(2)
            print(con)
    except:
        # 在命令提示符中按下ctrl+c就是意外终止程序
        print('程序被意外终止!')
    finally:
        f.close()
        print('程序关闭')

except Exception as result:
    print('文件不存在')
