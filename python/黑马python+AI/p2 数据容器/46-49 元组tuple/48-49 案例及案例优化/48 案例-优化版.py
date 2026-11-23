"""来源：48 案例.py；配套：48 案例-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

students = (
    ('S001', '王林', 85, 92, 78),
    ('S002', '李慕婉', 92, 88, 95),
    ('S003', '十三', 78, 85, 82),
    ('S004', '曾牛', 88, 79, 91),
    ('S005', '周佚', 95, 96, 89),
    ('S006', '王卓', 76, 82, 77),
    ('S007', '红蝶', 89, 91, 94),
    ('S008', '徐立国', 75, 69, 82),
    ('S009', '许木', 86, 89, 98),
    ('S010', '遁天', 66, 59, 72),
)

from unicodedata import east_asian_width

# 原制表符依赖终端制表位；按本题中文／ASCII等宽显示估算列宽。
# 改变排版并补表头，不保证表情、组合字符或比例字体的视觉宽度。
def display_cell(value, width, right=False):
    text = str(value)
    used = sum(2 if east_asian_width(char) in "WF" else 1 for char in text)
    padding = " " * max(0, width - used)
    return padding + text if right else text + padding

widths = (8, 8, 6, 6, 6, 8, 8)
headers = ("学号", "姓名", "语文", "数学", "英语", "总分", "平均分")
print("".join(display_cell(value, width) for value, width in zip(headers, widths)))
# 原id改student_id，避免内置名遮蔽；解包顺序和成绩数值不变。
for student_id, name, chinese, math, english in students:
    total = chinese + math + english
    average = total / 3
    row = (student_id, name, chinese, math, english, total, f"{average:.1f}")
    print("".join(display_cell(value, width) for value, width in zip(row, widths)))

print()
# 原三科统计复制三份；改用科目／索引对照循环，减少维护重复，未测性能。
for subject, index in (("语文", 2), ("数学", 3), ("英语", 4)):
    scores = [student[index] for student in students]
    print(f"{subject}最低分：{min(scores)}，最高分：{max(scores)}，平均分：{sum(scores) / len(scores):.1f}")

print("优秀学生（平均分 > 90）：")
for student_id, name, *scores in students:
    average = sum(scores) / len(scores)
    if average > 90:
        print(f"学号：{student_id}，姓名：{name}，平均分：{average:.1f}")
