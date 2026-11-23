"""来源：62 案例.py；配套：62 案例-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

from math import isfinite


def triangle_area(base, height):
    """根据底和高返回三角形面积。"""
    # 原Triangle_area首字母大写；改snake_case，base比字母l更说明底的含义。
    return base * height / 2


def alpha_count(text):
    """统计本题限定的英语元音a/e/i/o/u，包含大写。"""
    # 原str遮蔽内置类型；原for/if累加改sum消费生成器，True算1，False算0。
    # 这是单次遍历的简洁写法，不声称比原循环实测更快。
    return sum(character in "aeiouAEIOU" for character in text)


def score_analyse(score_list: list[float]):
    """返回最高分、最低分、舍入一位小数的平均分。类型注解不自动验证。"""
    # 原max/min空表会ValueError；给出明确前置条件，不伪造空表平均数。
    if not score_list:
        raise ValueError("成绩列表不能为空")
    return max(score_list), min(score_list), round(sum(score_list) / len(score_list), 1)


def main():
    # 原文件全部注释，当前不会执行；本优化版启用三个课堂案例，属于行为变化。
    print(triangle_area(1, 2))
    print(f"传入的字符串中元音字母的个数{alpha_count(input('请输入字符串: '))}")
    scores = []
    while True:
        value = input("请输入高考成绩(输入'end'结束): ")
        if value == "end":
            if not scores:
                print("尚未录入成绩，请先输入至少一项")
                continue
            highest, lowest, average = score_analyse(scores)
            print(f"最高分{highest} 最低分{lowest} 平均分{average:.1f}")
            break
        try:
            score = float(value)
        except ValueError:
            print("请输入有效的数字，或输入 end 结束")
        else:
            # 新边界：拒绝nan/inf；没有擅自把高考成绩上限设为100。
            if isfinite(score):
                scores.append(score)
            else:
                print("成绩必须是有限数字")


if __name__ == "__main__":
    main()
