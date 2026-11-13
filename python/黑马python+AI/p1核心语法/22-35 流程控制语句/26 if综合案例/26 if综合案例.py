# # 案例1
# # 1. 接收输入的三角形三个边的边长
# a = int(input("请输入第一个边的边长："))
# b = int(input("请输入第二个边的边长："))
# c = int(input("请输入第三个边的边长："))

# # 2. 判断三角形的类型 - pass 是一个空语句，起到一个语法占位的作用

# if a + b > c and a + c > b and b + c > a:  # 条件成立，构成三角形
#     if a == b and b == c:
#         print(f"{a} {b} {c} 这三个边长构成等边三角形 ~")
#     elif a == b or b == c or a == c:
#         print(f"{a} {b} {c} 这三个边长构成等腰三角形 ~")
#     else:
#         print(f"{a} {b} {c} 这三个边长构成普通三角形 ~")
# else:
#     print(f"{a} {b} {c} 这三个边长不能构成三角形 !!!")

# 案例2
dianliang = int(input("请输入电量："))

if dianliang <2880:
    print(f"电费是 {dianliang * 0.4883}")
elif 2880 <= dianliang <= 4800:
    print(f"电费是 {2880 * 0.4883 + (dianliang - 2880) * 0.5383}")
elif 4800 < dianliang:
    print(f"电费是 {2880 * 0.4883 + (4800 - 2880) * 0.5383 +(dianliang - 4800) * 0.7883}")
else:
    print("输入的电量不合理")