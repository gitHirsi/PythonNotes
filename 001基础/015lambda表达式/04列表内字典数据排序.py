"""
@Author:Hirsi
@Time:2020/6/9 20:49
"""

students = [
    {'name': 'DD', 'age': 20},
    {'name': 'CC', 'age': 30},
    {'name': 'BB', 'age': 18},
    {'name': 'AA', 'age': 21}
]

# sort(key=lambda... , reverse=bool)

# name key对应的值 升序排序
students.sort(key=lambda x: x['name'])
print(students)

# name key对应的值 降序排序
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

# age key对应的值 升序排序
students.sort(key=lambda x:x['age'])
print(students)

# age key对应的值 降序排序
students.sort(key=lambda x:x['age'],reverse=True)
print(students)