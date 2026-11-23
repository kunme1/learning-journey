# # 组包与解包
# # 组包操作
# t1 = (5, 7, 9, 10, 2, 23, 12)
# t2 = 5, 7, 9, 10, 2, 23, 12

# print(t1)
# print(t2)

# # 解包操作
# # 基础解包(变量数量与容器的元素个数一致)
# a, b, c, d, e, f, g = t1
# print(a, b, c, d, e, f, g)

# # *扩展解包（* 收集剩余的所有元素， 封装到列表list中）
# first, second, *other, last = t1
# print(first)
# print(second)
# print(other)
# print(last)

# *other, last2, last1 = t1
# print(other)
# print(last2)
# print(last1)

# 案例1
a = 10
b = 20

# 组包又解包
a, b = b, a

print(a)
print(b)

# 案例2
a = 100
b = 200
c = 300

c, a, b = a, b, c
print(a)
print(b)
print(c)