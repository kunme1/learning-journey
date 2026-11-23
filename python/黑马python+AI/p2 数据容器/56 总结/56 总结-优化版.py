"""来源：56 总结.py；配套：56 总结-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

from math import isfinite


def read_scores():
    """读取三科有限数值；不擅自限定各科满分。"""
    # 原添加、修改分支各复制三次float(input)；集中读取便于维护。
    # 新增非法数值重输；不限制0—100，因为题目没有给出各科分数范围。
    while True:
        try:
            values = [float(input(f"请输入{subject}成绩: ")) for subject in ("语文", "数学", "英语")]
        except ValueError:
            print("请输入有效数字，重新录入三科成绩")
            continue
        if all(isfinite(value) for value in values):
            return dict(zip(("chi", "mat", "eng"), values))
        print("成绩必须是有限数字，不能是nan或inf")


score = {}
menu = "1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统"
subjects = {"chi": "语文", "mat": "数学", "eng": "英语"}
while True:
    print(menu)
    choice = input("请选择要执行的操作(1-7): ")
    match choice:
        case "1" | "2":
            # 新语法：match或模式复用相同录入流程，不是if条件的按位或。
            name = input("请输入学生姓名: ")
            if choice == "1" and name in score:
                print(f"学生{name}已存在")
                continue
            if choice == "2" and name not in score:
                print(f"学生{name}不存在")
                continue
            score[name] = read_scores()
            print(f"学生{name}的成绩已" + ("录入" if choice == "1" else "修改"))
        case "3":
            name = input("请输入要删除的学生姓名")
            if name in score:
                del score[name]
                print(f"学生{name}的成绩已删除")
            else:
                print(f"学生{name}不存在")
        case "4":
            name = input("请输入要查询学生姓名")
            if name in score:
                info = score[name]
                print(f"{name}的语文成绩:{info['chi']},数学成绩:{info['mat']},英语成绩:{info['eng']}")
            else:
                print(f"学生{name}不存在")
        case "5":
            # 原keys()+再次按键查值，改items解包，不丢姓名，保留插入顺序。
            for name, info in score.items():
                print(f"学生姓名: {name} 语文成绩: {info['chi']} 数学成绩: {info['mat']} 英语成绩: {info['eng']}")
        case "6":
            if not score:
                print("暂无学生信息，无法统计。")
                continue
            # 原六条推导式每次循环又算max/min，学生增多时反复扫描。
            # 改后每科缓存极值，再筛选全部并列姓名；三科共O(n)级扫描，未计时。
            for subject_key, subject_name in subjects.items():
                values = [info[subject_key] for info in score.values()]
                highest, lowest = max(values), min(values)
                highest_names = [name for name, info in score.items() if info[subject_key] == highest]
                lowest_names = [name for name, info in score.items() if info[subject_key] == lowest]
                print(f"班级{subject_name}最高分:{highest}, 学生姓名: {highest_names}")
                print(f"班级{subject_name}最低分:{lowest}, 学生姓名: {lowest_names}")
                print(f"班级{subject_name}平均分:{sum(values) / len(values):.1f}")
                # 输出改为按科目分组；姓名仍列表形式，数字和并列名单不变。
        case "7":
            break
        case _:
            print("非法操作!!")
