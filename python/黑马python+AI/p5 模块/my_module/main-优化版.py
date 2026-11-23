"""来源：main.py；配套：学习笔记-优化版.md。
整理日期：2026-11-24；原始文件保留。
"""

# 原main.py调用circle_area却没有导入，第一处调用即NameError。
# 显式导入同目录原circle_fun.py的函数；不改3.14近似与round语义。
from circle_fun import circle_area

# 原来小、中、大各复制一段计算与输出；循环统一规则，新增尺寸时只需改数据。
# 新知识：列表装(label, radius)二元组，for解包；输出顺序仍是小、中、大。
# 单价0.05是元/平方厘米，名字明确单位；不是测得速度优化。
def main():
    print("======= 计算披萨成本 ========")
    cost_per_square_cm = 0.05
    for label, radius_cm in [("小", 10), ("中", 15), ("大", 20)]:
        area = circle_area(radius_cm)
        cost = area * cost_per_square_cm
        print(f"{label}披萨面积：{area} cm²，成本：{cost:.1f} 元")


# 原顶层输出移入函数；直接执行会运行，导入本入口不再打印。
if __name__ == "__main__":
    main()
