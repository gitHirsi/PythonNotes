"""
@Author:Hirsi
@Time:2020/6/1 22:06
"""

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 提取数量大于200的品牌
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)
