# ------------------------------------ 函数 - 默认参数 ------------------------------------

# 定义函数
def reg_stu(name, age, gender = "男", city = "北京"):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu("王林", 20)
print(stu)

stu = reg_stu("李慕婉", 18, gender = "女")
print(stu)

stu = reg_stu("韩立", 22, city = "上海")
print(stu)