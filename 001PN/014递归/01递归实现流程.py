"""
@Author:Hirsi
@Time:2020/6/9 16:36
"""
"""
4以内数字累加，4+3+2+1
3以内数字累加，3+2+1
2以内数字累加，2+1
1以内数字累加，1
"""
def sunNum(num):
    # 出口
    if num==1:
        return 1
           #当前数字+当前数字-1的数的累加和
    return num+sunNum(num-1)


sum = sunNum(4)
print(sum)
