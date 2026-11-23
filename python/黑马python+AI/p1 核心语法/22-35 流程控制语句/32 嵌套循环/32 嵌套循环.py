# 案例
m = int(input("请输入长度："))
n = int(input("请输入宽度："))

# print自带换行，不符合预期
# for j in range(0, n):
#     for i in range(0,m):
#         print("* ")
#     print("\n")

for j in range(n):# 控制行
    for i in range(m):# 控制列
        print("* ",end = "")
    print()