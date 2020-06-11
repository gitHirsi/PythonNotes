"""
@Author:Hirsi
@Time:2020/6/11 11:19
"""
"""
1.r+ 和 w+ 的区别
2.文件指针对数据读取的影响
"""
# r+ 文件指针在开头，所以能读取出来数据
f1=open('test.txt','r+')
f1.write('hirsiboom')
print(f1.read())
f1.close()

# w+ 指针在开头，用新内容覆盖原内容


# a+ 没有会新建文件，指针在结果，无法读取数据
f2=open('test.txt','a+')
con = f2.read()
print(con)

f2.close()