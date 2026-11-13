# match...case 模式匹配：工作日程安排
# day = input("请输入星期(1-7)：")

# match day:
#     case "1":
#         print("周一：工作会议日")
#     case "2":
#         print("周二：学习培训日")
#     case "3":
#         print("周三：项目开发日")
#     case "4":
#         print("周四：代码审查日")
#     case "5":
#         print("周五：总结规划日")
#     case "6" | "7":
#         print("周末：休息放松")
#     case _:  # 匹配其他所有的情况
#         print("输入有误!!!")

# # 案例1
# num1 = float(input("请输入第一个数字： "))
# num2 = float(input("请输入第二个数字： "))
# oper = input("请输入运算符(+ _ * /)： ")

# match oper:
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#         print(num1 * num2)
#     case "/":
#         print(num1 / num2)
#     case _:
#         print("运算符输入错误")

# 练习
oper = input("请输入您的操作： ")

match oper:
    case "上" | 'w' | 'W':
        print("角色向上移动")
    case _:
        print("无响应")