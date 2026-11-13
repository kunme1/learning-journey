# # 字面量的写法
# print(100)# 整数（int）
# print(3.14)# 浮点数/小数（float）
# print(True)# 必须大写 布尔（bool）
# print(False)# 必须大写 布尔（bool）
# print("Hello World")# 字符串（str）
# print("------------------")# ''也可以 字符串（str）
# print(None)# 空值（NoneType） 代表没有值

# # 布尔类型本质也是整数类型（True = 1, False = 0）
# print(True + 1) # 2
# print(False - 1) # -1

# 变量 -->Python是动态类型语言，变量的类型是根据赋值来决定的
# 项目开发中推荐变量只存储一种类型数据
# num = 1114.1
# print(num) # 1114.1

# num = num + 1
# print(num) # 1115.1

# num = "OK"
# print(num) # OK

# num = True
# print(num) # True

# a = True 
# print(a)

# 案例
base = 20.7# 基础播放量
incr = 50 #新增播放量
print("未来第一个月总播放量：", base + incr)
print("未来第二个月总播放量：", base + 2 * incr)


# 案例 - 一次定义多个变量
base, incr = 20.7, 50
print("未来第一个月总播放量：", base + incr)
print("未来第二个月总播放量：", base + 2 * incr)
