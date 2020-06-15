"""
@Author:Hirsi
@Time:2020/6/11 11:50
"""

"""
步骤:
    1.接受用户输入的文件名
    2.规划处备份文件的名字
    3.备份文件写入数据
"""

# 1
oldName = input('请输入你要备份的文件名：')

# 2
index = oldName.rfind('.')
if index>0:
    postfix=oldName[index:]
# 切片，组合备份的新文件名
newName = oldName[:index] + '[备份]' + postfix
print(newName)

# 3
old_f = open(oldName, 'rb')
new_f = open(newName, 'wb')

# 读取旧文件的内容，写入新文件
while True:
    con = old_f.read(1024)
    if len(con)==0:
        break
    new_f.write(con)

old_f.close()
new_f.close()
