# # # 法1

# # mail = input("请输入邮箱账号： ")
# # if mail.count("@") == 1 and mail.count(".") >= 1:
# #     print("邮箱格式正确")
# # else:
# #     print("邮箱格式错误")

# # 法2 in 运算符 ---> 判断子串是否存在字符串中，存在， 返回True； 否则， 返回Flase

# mail = input("请输入邮箱账号： ")
# if mail.count("@") == 1 and "." in mail:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

# # 练习1
# sen = input("请输入字符串，以判断是否回文： ")

# # rsen = sen[-1:-len(sen) - 1:-1]

# rsen = sen[::-1]

# if sen == rsen:
#     print("该字符串回文！")
# else:
#     print("该字符串不回文")

# 练习2
strings = []

for i in range(10):
    s = input("请输入字符串")
    # rs = s[::-1]
    # us = rs.upper()
    # strings.append(us)
    strings.append(s[::-1].upper())
# print(list) 错误 非遍历输出
for item in strings:
    print(item)