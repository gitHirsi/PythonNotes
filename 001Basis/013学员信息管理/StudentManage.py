"""
@Author:Hirsi
@Time:2020/6/7 20:26
"""

stuInfo = [{'id': '001', 'name': 'Hirsi', 'tel': '156234'}]

# 添加学员信息
def addStu():
    newId = input('请输入学号：')
    newName = input('请输入姓名：')
    newTel = input('请输入手机号：')

    for i in stuInfo:
        if newName==i['name']:
            print('该学员信息已存在！，跳转...')
            # 推出当前函数，后面添加信息代码不执行
            return

    stuDict={}
    stuDict['id']=newId
    stuDict['name']=newName
    stuDict['tel']=newTel
    stuInfo.append(stuDict)  #一个学员信息添加到列表
    print('***添加成功！***')

# 删除学员信息
def delStu():
    delName = input('请输入要删除的学员姓名:')
    for i in stuInfo:
        if delName==i['name']:
            stuInfo.remove(i)
            print('***删除成功！***')
            break
    else:  #循环结束，说明学员不存在
        print('该学员不存在！')

# 修改学员信息函数
def modifyStu():
    modifyName = input('请输入要修改学员的姓名:')
    for i in stuInfo:
        if modifyName==i['name']:
            i['tel']=input('请输入新的手机号：')
            print('***修改学员信息成功！***')
            break
    else:
        print('该学员不存在！')

# 查询学员信息函数
def findStu():
    findName = input('请输入要查询的学员姓名：')
    for i in stuInfo:
        if findName==i['name']:
            print('查询的学员信息如下：')
            print(f"学号：{i['id']}，姓名：{i['name']}，电话:{i['tel']}")
            break
    else:
        print('该学员不存在！')

# 显示全部学生信息函数
def viewInfo():
    print('学号\t姓名\t电话')
    for i in stuInfo:
        print(f"{i['id']}\t\t{i['name']}\t{i['tel']}")

# 运行入口，选择功能函数
def selectFun():
    """选择功能界面函数"""
    while True:
        print('---请选择功能👇---')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员')
        print('4:查询学员')
        print('5:显示所有学员')
        print('6:退出系统')
        print('-' * 20)
        userNum = int(input('请输入:'))
        if userNum == 1:
            addStu()
        elif userNum == 2:
            delStu()
        elif userNum == 3:
            modifyStu()
        elif userNum == 4:
            findStu()
        elif userNum == 5:
            viewInfo()
        elif userNum == 6:
            # exit()
            result = input('确定退出系统吗? y/n')
            if result=='y':
                break

        else:
            print('选择无效！')


# Action
selectFun()
