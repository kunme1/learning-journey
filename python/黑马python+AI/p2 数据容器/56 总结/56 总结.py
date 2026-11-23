# 1.设计菜单
menu = """
# # # # # # # # # # # # # # # # # # # # # # # # #  【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # #
#     1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

# 2.数据结构 scores = {"name": {"chi": chinsese_score, "mat": math_score, "eng": english_score}}
score = {}

while True:
    print(menu)
    choice = input("请选择要执行的操作(1-7): ")

    match choice:
        case "1":# 添加学生信息
            name = input("请输入要添加的学生姓名")
            if name in score:
                print(f"学生{name}已存在")
            else:
                chi_score = float(input("请输入语文成绩: "))
                mat_score = float(input("请输入数学成绩: "))
                eng_score = float(input("请输入英语成绩: "))
                score[name] = {"chi": chi_score, "mat": mat_score, "eng": eng_score}
                print(f"学生{name}的成绩已录入")

        case "2":
            name = input("请输入要修改的学生姓名")
            if name not in score:
                print(f"学生{name}不存在")
            else:
                chi_score = float(input("请输入语文成绩: "))
                mat_score = float(input("请输入数学成绩: "))
                eng_score = float(input("请输入英语成绩: "))
                score[name] = {"chi": chi_score, "mat": mat_score, "eng": eng_score}
                print(f"学生{name}的成绩已修改")
        case "3":
            name = input("请输入要删除的学生姓名")
            if name not in score:
                print(f"学生{name}不存在")
            else:
                del score[name]
                print(f"学生{name}的成绩已删除")
        case "4":
            name = input("请输入要查询学生姓名")
            if name not in score:
                print(f"学生{name}不存在")
            else:
                print(f"{name}的语文成绩:{score[name]["chi"]},数学成绩:{score[name]["mat"]},英语成绩:{score[name]["eng"]}")
        case "5":
            for s in score.keys():
                s_info = score[s]
                print(f"学生姓名: {s} 语文成绩: {s_info["chi"]} 数学成绩: {s_info["mat"]} 英语成绩: {s_info["eng"]}")
        case "6":
            if not score:
                print("暂无学生信息，无法统计。")
                continue

            all_chi = []
            all_mat = []
            all_eng = []
            for s in score.keys():
                s_info = score[s]
                all_chi.append(s_info["chi"])
                all_mat.append(s_info["mat"])
                all_eng.append(s_info["eng"])
            print(f"班级语文最高分:{max( all_chi)}, 学生姓名: {[s for s in score.keys() if score[s]["chi"] == max(all_chi)]}")
            print(f"班级数学最高分:{max( all_mat)}, 学生姓名: {[s for s in score.keys() if score[s]["mat"] == max(all_mat)]}")
            print(f"班级英语最高分:{max( all_eng)}, 学生姓名: {[s for s in score.keys() if score[s]["eng"] == max(all_eng)]}")
            print(f"班级语文最低分:{min( all_chi)}, 学生姓名: {[s for s in score.keys() if score[s]["chi"] == min(all_chi)]}")
            print(f"班级数学最低分:{min( all_mat)}, 学生姓名: {[s for s in score.keys() if score[s]["mat"] == min(all_mat)]}")
            print(f"班级英语最低分:{min( all_eng)}, 学生姓名: {[s for s in score.keys() if score[s]["eng"] == min(all_eng)]}")
            print(f"班级语文平均分:{sum( all_chi) / len(all_chi):.1f}")
            print(f"班级数学平均分:{sum( all_mat) / len(all_mat):.1f}")
            print(f"班级英语平均分:{sum( all_eng) / len(all_eng):.1f}")
        case "7":
            break
        case _:
            print("非法操作!!")