# # 算术运算符： +  -  *  /  //  %  **

# print("10 + 4 = ", 10 + 4)    # 加
# print("10 - 4 = ", 10 - 4)    # 减
# print("10 * 4 = ", 10 * 4)    # 乘
# print("10 / 4 = ", 10 / 4)    # 除
# print("10 // 4 = ", 10 // 4)  # 整除(结果为整数)
# print("10 % 4 = ", 10 % 4)    # 取余/求模
# print("10 ** 4 = ", 10 ** 4)  # 幂指数，10的4次方

# # 算术运算符的优先级：** > * / // % > + -,括号优先级最高
# print("0.1 + 10 / 4**2 =  ", 0.1 + 10 / 4 ** 2)

# # 案例
# # x = input("请输入x:")
# # y = input("请输入y:")

# # print(f"x + y = {int(x) + int(y)}, x - y = {int(x) - int(y)}")
# # 这个方法麻烦了，可以直接使用print( part1 , part2)
# # x = int(input("请输入x:"))
# # y = int(input("请输入y:"))

# # print("x + y =", x + y)
# # print("x - y =", x - y)

# # x = 0.5 y = 0.4,会出现精度损失
# # 0.09999999999999998, 由于计算机底层是基于二进制进行数据的存储与处理，二进制是无法准确地表示所有的小数，因此涉及到浮点数的运算，可能会损失精度
# x = float(input("请输入x:"))
# y = float(input("请输入y:"))

# print("x + y =", x + y)
# print("x - y =", x - y)


# # 练习1
# num1 = int(input("请输入第一个整数："))
# num2 = int(input("请输入第二个整数："))
# num3 = int(input("请输入第三个整数："))

# print("输入的三个整数的平均数是：" , (num1 + num2 + num3) / 3)

# # 练习2
# upper_length = float(input("请输入上底的长度："))
# under_length = float(input("请输入下底的长度：")) 
# heigth = float(input("请输入梯形的高：")) 

# space = ((upper_length + under_length) * heigth)/2

# print("梯形的面积是："  , space)

# # 练习3
# r = float(input("请输入圆的半径："))

# c = 2 * 3.14 *r
# s = 3.14 * r**2

# print("圆的周长是：" , c , "\n" , "圆的面积是：" , s)

# 练习4
weight = float(input("请输入你的体重（单位 kg）:"))
height = float(input("请输入你的身高（单位 m）："))

print("你的身体质量指数BMI为：" , weight / height ** 2)