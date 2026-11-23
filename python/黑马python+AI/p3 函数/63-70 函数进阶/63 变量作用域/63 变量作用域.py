# ------------------------------------ 函数 - 变量的作用域 ------------------------------------

# 全局变量
num = 100

# 定义函数
def circle_area(r):
    # 局部变量 : 只能在函数内部使用

    pi = 3.14
    area = pi * r * r

    # 局部变量num
    # num = 10000

    # global 关键字
    global num
    num = 10000
    print("num =", num)
    return area



# 调用函数
c_area = circle_area(10)
print(c_area)

print("num =", num)