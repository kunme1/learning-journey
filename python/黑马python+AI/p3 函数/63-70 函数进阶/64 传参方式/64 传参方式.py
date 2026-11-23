# ------------------------------------ 函数 - 传参方式 ------------------------------------

# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 传参方式一：位置参数
stu = reg_stu("张三", 18, "男", "北京" )
print(stu)

# 传参方式二：关键字参数
stu = reg_stu(name = "张三", age = 18, city = "北京", gender = "男" )
print(stu)

# 传参方式三：位置参数 + 关键字参数 ---> 位置参数在前,关键字参数在后
stu = reg_stu("张三", 18, city = "北京",gender =  "男" )
print(stu)
