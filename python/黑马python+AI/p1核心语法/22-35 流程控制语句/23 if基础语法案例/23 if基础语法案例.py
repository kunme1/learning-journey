# 案例1
correct_account = 18888888888
correct_password = 666888
account = int(input("请输入您的账号： "))
password = int(input("请输入您的密码： "))

if account == correct_account and password == correct_password:
    print("登陆成功")
    print("进入B站首页")
else:
    print("登录失败")
    print("账号或密码错误")