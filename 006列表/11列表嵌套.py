"""
@author:Hirsi
@time:2020/5/26 19:49
"""

nameList = [['Hirsi', 'Tom', 'Bill'], ['小红','小白','小黄'],['张三','李四','王五']]

i=0
while i<len(nameList):
    j=0
    while j<len(nameList[i]):
        print(nameList[i][j])
        j+=1

    i+=1
