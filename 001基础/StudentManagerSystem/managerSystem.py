"""
@Author:Hirsi
@Time:2020/6/15
"""
from student import *

class StudentManager(object):
    # 初始化学生列表，用来存储学生对象
    def __init__(self):
        self.stu_list = []

    # 程序入口函数
    def run(self):
        # 加载数据
        self.load_stu()

        while True:
            # 显示功能菜单   类里面调用实例方法，前面加self
            self.show_menu()
            # 用户输入功能序号
            menu_num = int(input('请输入选择的功能序号：'))
            # 根据用户输入的序号，执行不同功能
            if menu_num == 1:
                self.add_stu()
            elif menu_num == 2:
                self.del_stu()
            elif menu_num == 3:
                self.modify_stu()
            elif menu_num == 4:
                self.search_stu()
            elif menu_num == 5:
                self.show_stu()
            elif menu_num == 6:
                self.save_stu()
            elif menu_num == 7:
                break

    # 显示功能函数  定义为静态
    @staticmethod
    def show_menu():
        print('*' * 20)
        print('请选择如下功能：')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')

    # 添加学员
    def add_stu(self):
        print('正在添加学员信息👇>>>')
        name = input('请输入姓名:')
        gander = input('请输入性别:')
        tel = input('请输入手机:')
        stu = Student(name,gander,tel)
        self.stu_list.append(stu)
        print('>>>添加学员成功!')


    # 删除学员
    def del_stu(self):
        print('正在删除学员信息👇>>>')
        del_name = input('请输入姓名：')
        for i in self.stu_list:
            if del_name==i.name:
                self.stu_list.remove(i)
                print('>>>删除学员信息成功!')
                break
        else:
            print('没有此学员信息！')

    # 修改学员信息
    def modify_stu(self):
        print('正在修改学员信息👇>>>')
        modify_name = input('请输入要修改学员的姓名：')
        for i in self.stu_list:
            if modify_name==i.name:
                i.gander=input('性别修改为：')
                i.tel=input('手机修改为：')
                print('>>>修改学员信息成功!')
                break
        else:
            print('没有此学员信息')

    # 查询学员信息
    def search_stu(self):
        print('正在查询学员信息👇>>>')
        search_name = input('请输入姓名：')
        for i in self.stu_list:
            if search_name==i.name:
                print(f'学员信息--姓名：{i.name},性别:{i.gander},手机：{i.tel}')
                break
        else:
            print('没有此学员信息！')

    # 显示所有学员信息
    def show_stu(self):
        if self.stu_list:
            print('姓名\t\t性别\t\t手机')
            for i in self.stu_list:
                print(f'{i.name}\t\t{i.gander}\t\t{i.tel}')
        else:
            print('---没有学员信息！---')

    # 保存学员信息到数据文件
    def save_stu(self):
        f=open('student.data', 'w')
        #列表里面的学员对象转换为字典
        new_list=[i.__dict__ for i in self.stu_list]
        #数据转换为字符串存入文件
        f.write(str(new_list))
        f.close()
        print('>>>保存学员信息成功!')

    # 加载学员信息
    def load_stu(self):
        try:
            f=open('student.data', 'r')
        except:
            f=open('student.data', 'w')
        else:
            data = f.read()
            # eval把字符串数据，转成原型(还原)
            new_list = eval(data)
            # 推导式把元素是字典形式的列表的值，转换给stu_list
            self.stu_list=[Student(i['name'],i['gander'],i['tel']) for i in new_list]

        finally:
            f.close()
