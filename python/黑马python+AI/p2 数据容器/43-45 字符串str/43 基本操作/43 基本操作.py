# 字符串 基本操作 ---> 不可变的（无法修改）,有序性，可迭代性
s = "Hello Python"

# 有序的
print(s[4])# 正向索引
print(s[-8])# 反向索引 

# s[4] = "X"
# print(s)
# 报错 'str' object does not support item assignment

# 可迭代性
for i in s:
    print(i)

# 切片
print(s[0: 5: 1])
print(s[: 5: 1])
print(s[: 5: ])
print(s[: 5])

print(s[6: 12: 1])
print(s[6:: 1])

# 步长 ---> 正数：从前往后截取； 负数： 从后往前截取
print(s[0: 5: 2])
print(s[0: 5: -1])# 方向冲突，没有截取
print(s[5: 0: -1])

# 反转字符串
print(s[::-1])
