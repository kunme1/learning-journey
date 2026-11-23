# 练习1
"""
1. 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
    分数 >= 90：A
    分数 >= 75：B
    分数 >= 60：C
    分数 < 60：D
"""
def score_grade(score:float):
    """
    1. 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
    分数 >= 90：A
    分数 >= 75：B
    分数 >= 60：C
    分数 < 60：D

    :param score: 传入的分数
    :return: 对应的分数等级
    """
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

print(score_grade(90))
print(score_grade(80))
print(score_grade(65))
print(score_grade(45))

print("--------------------------------------")

"""
2. 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
    把字符串反转，如果和原字符串相同，就是回文串。
    如："level"、"radar"、"黄山落叶松叶落山黄"
"""
# def Palindrome(str: str):
#     str_list = list(str)
#     re_str_list = str_list
#     str_list.reverse()
#     if re_str_list == str_list:
#         return "是回文串"
#     else: 
#         return "不是回文串"

"""
字符串反转使用字符串切片
"""
def Palindrome(str: str):
    re_str = str[::-1]
    if re_str == str:
        return "是回文串"
    else: 
        return "不是回文串"

print(Palindrome("level"))
print(Palindrome("radar"))
print(Palindrome("黄山落叶松叶落山黄"))

print("----------------------------------------")


# 3. 定义一个函数，完成时间转换功能，将传入的秒数转换为小时、分钟、秒。

def time_trans(seconds:int):
    """
    将传入的秒数转换为小时、分钟、秒。
    
    :param secondes: 传入的秒数
    :return: 转换为小时、分钟、秒的时间
    """
    if seconds <=59:
        return f"{seconds}秒"
    elif seconds <= 59 *60 + 59:
        return f"{seconds // 60}分{seconds % 60}秒"
    else:
        hour = seconds // 3600
        minute = (seconds - hour * 60) // 60
        return f"{hour}时 {minute}分 {seconds % (60 * 60)}秒"

print(time_trans(50))
print(time_trans(80))
print(time_trans(4536345))
print(time_trans(34243))

"""
4. 定义一个函数，根据传入的三角形三个边的边长，
    判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
"""

def Triangle_judge(a, b, c):
    if a + b <= c:
        return "不能构成三角形"

    if a == b == c:
        return "等边三角形"
    elif a == b or a == c or b == c:# 只能用or,不能用|
        return "等腰三角形"
    else: 
        return "普通三角形"

print(Triangle_judge(1,1,2))
print(Triangle_judge(0.2,0.3,1))
print(Triangle_judge(2,2,3))
print(Triangle_judge(2,2,2))