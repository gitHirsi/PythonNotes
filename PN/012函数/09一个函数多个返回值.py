"""
@Author:Hirsi
@Time:2020/6/5 21:22
"""

def test1():
    # return 1,3
    return [1,3]
    # return {'name':'Hirsi','age':18}

result = test1()
print(result)
print(result[0])
print(result[1])


# for key,value in result.items():
#     print('-'*10)
#     print(key)
#     print(value)