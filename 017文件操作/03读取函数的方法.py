"""
@Author:Hirsi
@Time:2020/6/10 22:42
"""

"""
1.read(num)
    不写num参数表示读取所有
"""
# f1=open('test.txt','r')
# print(f1.read(16))
# f1.close()

"""
2.readlines()
    按照行的方式把整个文件中的内容进行一次性读取，并且返回一个列表，其中每行数据为一个元素
"""
# f2=open('test.txt','r')
# readlines = f2.readlines(20)
# print(readlines)
# f2.close()

"""
3.readline()
    一次性读取一行内容
"""
f3=open('test.txt','r')
r = f3.readline()
print(f'第一行：{r}')

r = f3.readline()
print(f'第二行：{r}')

r = f3.readline()
print(f'第三行：{r}')

f3.close()