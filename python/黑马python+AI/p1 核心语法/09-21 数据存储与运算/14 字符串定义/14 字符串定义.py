# 字符串
# 三种方式
s1 = "Hello"
s2 = 'Python'
# 单双引号不能直接换行
# 三引号可以' "，官方推荐"""
s3 = """
Hello:
    111
    222
"""
# 三引号内部的注释会以内容形式呈现

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

# 定义字符串 It's very good
msg = 'It\'s very good'
# 字符串中想要使用引号要使用转义字符\，或者使用另一种引号
# 转义字符 \' \" \n \t

print(msg)

msg = "It's very good"
print(msg)

# msg2 = "Hello 的意思就是 "您好""
msg2 = "Hello 的意思就是 \"您好\""
print(msg2)

msg3 = 'Hello 的意思就是 "您好"'
print(msg3)

msg4 = "111 222"
print(msg4)

msg5 = "111\n222"
print(msg5)

msg6 = "111\t222"
print(msg6)
# \n换行 \t相当于按了tab缩进
