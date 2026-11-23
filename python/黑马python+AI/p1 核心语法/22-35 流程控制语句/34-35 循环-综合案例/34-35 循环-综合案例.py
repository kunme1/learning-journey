# 法1

# state = 0

# while (state == 0):
#     user_name = input("请输入用户名： ")
#     password = input("请输入密码: ")

#     if user_name == "" or password == "":
#         print("输入的用户名和密码不能为空！")
#     elif user_name == "admin" and password == "666888":
#         print("登陆成功，进入B站首页~")
#         state = 1
#     elif user_name == "root" and password == "123123":
#         print("登陆成功，进入B站首页~")
#         state = 1
#     elif user_name == "zhangsan" and password == "123456":
#         print("登陆成功，进入B站首页~")
#         state = 1
#     else:
#         print("用户名或密码错误，请重新输入")

# # 法2

# while True:
#     user_name = input("请输入用户名： ")
#     password = input("请输入密码: ")

#     if user_name == "" or password == "":
#         print("输入的用户名和密码不能为空！")
#         continue
    
#     if user_name == "admin" and password == "666888":
#         print("登陆成功，进入B站首页~")
#         break
#     elif user_name == "root" and password == "123123":
#         print("登陆成功，进入B站首页~")
#         break
#     elif user_name == "zhangsan" and password == "123456":
#         print("登陆成功，进入B站首页~")
#         break
#     else:
#         print("用户名或密码错误，请重新输入")

# # 练习

# count = 0

# while count < 5:
#     user_name = input("请输入用户名： ")
#     password = input("请输入密码: ")

#     if user_name == "" or password == "":
#         print("输入的用户名和密码不能为空！")
#         continue

#     count += 1
    
#     if user_name == "admin" and password == "666888":
#         print("登陆成功，进入B站首页~")
#         break
#     elif user_name == "root" and password == "123123":
#         print("登陆成功，进入B站首页~")
#         break
#     elif user_name == "zhangsan" and password == "123456":
#         print("登陆成功，进入B站首页~")
#         break
#     else:
#         print("用户名或密码错误，请重新输入")

# if count == 5:
#     print("您已达到操作上限")

# """
# 案例2：猜数字游戏

# 1. 系统随机生成一个随机数
# 2. 用户根据提示猜数字，并将所猜的数字输入系统
# 3. 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 4. 如果猜对，系统自动退出，游戏结束
# """

# import random
# random_num = random.randint(1, 100)# 生成1-100的随机数

# while True:
#     guess = int(input("请输入您猜测的数字："))

#     if guess == random_num:
#         break
#     elif guess < random_num:
#         print("猜小了")
#     else:
#         print("猜大了")

# print(f"猜对了，随机生成的数字是：{random_num}")

# # 练习1
# sumi = 0

# for i in range(1, 1001):
#     if i % 5 == 0:
#         sumi += i

# print("1-1000之间5的倍数之和为" , sumi)

# 练习2
num_a = 0
num_k = 0

for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
    if i == "a":
        num_a += 1
        continue# 该处不能用 break 会直接跳出循环，continue 是继续下一次循环
    if i == "k":
        num_k += 1

print(f"该字符串中有 {num_a} 个 a, {num_k} 个 k")