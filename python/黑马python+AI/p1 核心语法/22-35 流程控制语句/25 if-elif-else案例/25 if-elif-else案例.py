# # if...elif...else 案例：根据用户输入的数字，判断数字是正数、负数，还是0

# num = int(input("请输入数字："))

# if num > 0:
#     print(f"{num} 是一个正数")
# elif num < 0:
#     print(f"{num} 是一个负数")
# else:
#     print(f"{num} 是0")

# 案例1
# user_name = input("请输入用户名： ")
# password = input("请输入密码: ")

# account1 = "admin" 
# password1 = "666888"
# account2 = "root"
# password2 = "123123"
# account3 = "zhangsan"
# password3 = "123456"

# if (
#     (user_name == account1 and password == password1)
#     or
#     (user_name == account2 and password == password2)
#     or
#     (user_name == account3 and password == password3)
# ):
#     print("登陆成功")
# else:
#     print("登陆失败")

# 法2
user_name = input("请输入用户名： ")
password = input("请输入密码: ")

if user_name == "admin" and password == "666888":
    print("登陆成功")
elif user_name == "root" and password == "123123":
    print("登陆成功")
elif user_name == "zhangsan" and password == "123456":
    print("登陆成功")
else:
    print("登陆失败")