# # 案例1

# # 1.定义列表
# num_list = []

# # 2.存入列表
# for i in range(10):
#     num = int(input(f"请输入第{i + 1}数字： "))
#     num_list.append(num)

# print("数字列表：", num_list)

# # 3.排序
# num_list.sort()

# print("排序后的数字列表：", num_list)

# # 4.输出最小值，最大值，平均值
# print(f"最小值是：{num_list[0]}")
# print(f"最小值是：{min(num_list)}")
# print(f"最大值是：{num_list[-1]}")
# print(f"最大值是：{max(num_list)}")

# # sum()用来求和,len()用来获取长度
# print(f"平均值是：{sum(num_list) / len(num_list)}")

# 案例2
# 案例2：合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）

# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 1.合并列表

# 法1

# for i in range(len(num_list2)):
#     num_list1.append(num_list2[i])

# print(num_list1)

# # 法2 优化法1

# for num in num_list2:
#     num_list1.append(num)

# print("合并后的原始列表", num_list1)

# # 2.去除重复记录
# new_list = []# 去除重复记录后的列表

# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)

# print("去重后的列表为：", new_list)

# # 法3 简化法2

# # 解包操作： 将列表这一类容器，解开成一个个独立的元素
# # 组包操作： 将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]

# print("合并后的原始列表", num_list)

# # 2.去除重复记录
# new_list = []# 去除重复记录后的列表

# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)

# print("去重后的列表为：", new_list)

# # 法4 
# # 通过 + 直接合并
# num_list = num_list1 + num_list2

# print("合并后的原始列表", num_list)

# # 2.去除重复记录
# new_list = []# 去除重复记录后的列表

# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)

# print("去重后的列表为：", new_list)

# 案例3:生成1-20的平方表

# # 法1:传统方式
# num_list = []

# for i in range(1, 21):
#     num_list.append(i ** 2)
# print(num_list)

# # 法2:简化(使用列表推导式:就是按照一定规则,快速生成一个列表的方法)--->语法格式:[要插入的值 for i in 序列/列表]
# num_list2 = [i ** 2 for i in range(1, 21)]
# print(num_list2)

# 案例4：从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表。[要插入的值 for i in 序列/列表 if 条件]
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i ** 2 for i in num_list if i % 2 == 0]
print(new_list)