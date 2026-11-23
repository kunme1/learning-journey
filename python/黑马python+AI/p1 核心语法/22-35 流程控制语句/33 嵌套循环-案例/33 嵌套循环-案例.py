# # 案例
# for i in range(1, 10):# 控制行
#     for j in range(1, i + 1):# 控制列
#         print(f"{j} * {i} = {j * i}", end = "\t")# \t - tab
#     print()

# 练习1
# a = int(input("请输入直角边的边长： "))

# for i in range(a):
#     for j in range (i + 1):
#         print ("*", end = " ")
#     print("")

# # 练习2
# num = int(input("请输入数字： "))

# for i in range (num):# 控制行
#     for j in range (1, i + 2):
#         print(j, end = " ")
#     print()

# 练习3
# ▢■
# 8行 8列

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()