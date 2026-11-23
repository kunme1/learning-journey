"""来源：53 常用操作.py；配套：53 常用操作-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

# 字典常规操作
dict1 = {"王林": 670, "李慕婉": 608, "徐立国": 508, "韩立": 688}
print(dict1)

# 添加 - key值不存在就是添加
dict1["涛哥"] = 550
print(dict1)

# 修改 - key值存在就是修改
dict1["涛哥"] = 620
print(dict1)

# 查询
print(dict1["涛哥"])# 根据key获取value
print(dict1.get("涛哥"))# 根据key获取value

print(dict1.keys())# 获取所有的key
print(dict1.values())# 获取所有的value
print(dict1.items())# 获取所有的键值对key:value

# 删除
score = dict1.pop("徐立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)

# 遍历
# 原keys()可省略：普通字典默认迭代键；输出和插入顺序不变。
# 后两种items遍历保留用于比较语法，不把教学对照当作冗余。
for k in dict1:
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

for k, v in dict1.items():
    print(f"{k} : {v}")
