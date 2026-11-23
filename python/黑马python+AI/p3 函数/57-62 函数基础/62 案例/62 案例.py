# # 案例1
# def Triangle_area(l, h):
#     """
#     用来计算三角形的面积

#     :param l: 三角形的底
#     :param h: 三角形的高
#     :return: 三角形的面积
#     """
#     return l * h / 2

# help(Triangle_area)

# area = Triangle_area(1, 2)
# print(area)

# # 案例2
# def alpha_count(str):
#     """
#     计算传入的字符串中元音字母的个数

#     :param str: 传入的字符串
#     :return num: 元音字母的个数
#     """
#     num = 0
#     for i in str:
#         if i in "aeiouAEIOU":
#             num += 1
#     return num

# print(f"传入的字符串中元音字母的个数{alpha_count(input("请输入字符串"))}")

# # 案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。
# def score_analyse(score_list:list[float]):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。

#     :param score_list: 成绩列表
#     :return: 成绩的最高分、最低分、平均分
#     """
#     max_score = max(score_list)
#     min_score = min(score_list)
#     avg_score = round(sum(score_list) / len(score_list), 1)

#     return max_score, min_score, avg_score

# score_list = []

# while 1:
#     op = input("请输入高考成绩(输入'end'结束): ")
#     match op:
#         case 'end':
#             a, b, c = score_analyse(score_list)
#             print(f"最高分{a} 最低分{b} 平均分{c}")
#             break
#         case _:
#             try:
#                 score = float(op)  # 尝试将字符串转换成浮点数
#             except ValueError:
#                 print("请输入有效的数字，或输入 end 结束")
#             else:
#                 score_list.append(score)  # 转换成功才加入列表
            




