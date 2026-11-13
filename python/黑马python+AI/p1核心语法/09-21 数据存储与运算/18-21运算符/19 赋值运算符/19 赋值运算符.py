# 赋值运算符：= += -= *= /= %= //= **=

num = 85

num += 10  # num = num + 10
print("num += 10 后，num = ", num)
print(type(num))

num -= 10  # num = num - 10
print("num -= 10 后，num = ", num)
print(type(num))

num *= 10  # num = num * 10
print("num *= 10 后，num = ", num)
print(type(num))

# num /= 10  # num = num / 10
# print("num /= 10 后，num = ", num)
# print(type(num))

num //= 10  # num = num // 10
print("num //= 10 后，num = ", num)
print(type(num))

num %= 3  # num = num % 3
print("num %= 3 后，num = ", num)
print(type(num))

num **= 3  # num = num ** 3
print("num **= 3 后，num = ", num)
print(type(num))