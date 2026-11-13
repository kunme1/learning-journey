# %s
# 案例 ---> str(int数字) --->转为字符串
name = "kunme1"
age = 21 # 需要转为字符串
pro = "人工智能"
hobby = "python"
print("大家好，我是" + name + "，今年" + str(age) + "岁，专业是" + pro + "，爱好是" + hobby)
print("大家好，我是%s，今年%s岁，专业是%s，爱好是%s" % (name, age, pro, hobby))


#f"内容{变量/表达式}"
print(f"大家好，我是{name}，今年{age}岁，专业是{pro}，爱好是{hobby}")
