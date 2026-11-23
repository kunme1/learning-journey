# 列表操作
# 定义
# 定义列表
s = [56, 90, 88, 65, 90, "A", "Hello", True]

print(type(s))  # 查看数据类型

# 访问列表元素
# 获取
print(s[0])   # 正向索引，从0开始，结果：56
print(s[-8])  # 反向索引，从-1开始，结果：56

print(s[2])   

# 修改
s[5] = "ABC"
print(s)

# 注意：如果指定的索引超出范围，将会报错 list assignment index out of range
# s[10] = "DEF"
# print(s)

# 删除
del s[6]
print(s)

# 遍历
for item in s:
    print(item)