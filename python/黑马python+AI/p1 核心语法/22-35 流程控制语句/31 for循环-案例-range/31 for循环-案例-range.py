# 案例1

# 1-2求和，1-100无法使用
i = 1
total = 0

for i in (1, 2):
    total += i
    i += 1
print(total)

# 求1-100所有奇数的和

total2 = 0
for j in range(1, 101, 2):
    total2 += j
print(total2)

# 100-500 间 3 的倍数之和

total2 = 0
for k in range(100, 501):
    if k % 3 == 0:
        total2 += k
        k += 3
print(total2)