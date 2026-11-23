# 常见数据类型 ---> type() 获取指定的字面量或变量的类型

a = 10
a_type = type(a)
print("a =", a, "类型为：", a_type)

print(type("Hello"))
print(type(10))
print(type(3.14))

num = 5.0
print(num)
print(type(num))

print(type(True))
print(type(False))
print(type(None))

# 检查数据是否属于指定的类型
num = 5.0 
print (num)
print (isinstance(num, int))
print (isinstance(num, float))
print (isinstance(num, bool))
