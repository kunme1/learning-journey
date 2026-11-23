"""来源：练习.py；配套：62 案例-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

from math import isfinite


def score_grade(score: float):
    """按题目90/75/60三个阈值分类；题目未规定上下限。"""
    # 原elif/else均在前一个return之后；早返回可去掉额外嵌套，阈值和顺序不变。
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "D"


def is_palindrome(text: str) -> bool:
    """直接比较反转串；空串按该定义为True，不忽略标点。"""
    # 原Palindrome(str)遮蔽str，且返回文字，与题目bool要求不符。
    # return text == text[::-1]消除可由比较直接得到的if/else，返回类型改为bool。
    return text == text[::-1]


def time_trans(seconds: int):
    """将非负整数秒转换为时／分／秒；保留原来的分段显示风格。"""
    if type(seconds) is not int or seconds < 0:
        raise ValueError("秒数须为非负整数")
    # 原hour*60混用了小时和分钟单位，尾部%3600也不能得到秒字段。
    # 新divmod(a,b)同时返回商与余数：先分出小时，再从余秒分出分钟和秒。
    hour, remaining_seconds = divmod(seconds, 3600)
    minute, second = divmod(remaining_seconds, 60)
    if hour:
        return f"{hour}时 {minute}分 {second}秒"
    if minute:
        return f"{minute}分{second}秒"
    return f"{second}秒"


def triangle_judge(a, b, c):
    """有限正边长且任意两边之和大于第三边；等边优先于等腰。"""
    # 原or已修正，不能再称当前用了|；仍只检查a+b<=c，漏其他排列与非正数。
    if not all(isfinite(side) and side > 0 for side in (a, b, c)):
        return "不能构成三角形"
    if a + b <= c or a + c <= b or b + c <= a:
        return "不能构成三角形"
    if a == b == c:
        return "等边三角形"
    if a == b or a == c or b == c:
        return "等腰三角形"
    return "普通三角形"


if __name__ == "__main__":
    for value in (90, 80, 65, 45):
        print(score_grade(value))
    print("--------------------------------------")
    for text in ("level", "radar", "黄山落叶松叶落山黄"):
        print(is_palindrome(text))  # 行为变化：按题目返回／打印bool。
    print("----------------------------------------")
    for seconds in (50, 80, 4536345, 34243):
        print(time_trans(seconds))
    for sides in ((1, 1, 2), (0.2, 0.3, 1), (2, 2, 3), (2, 2, 2)):
        print(triangle_judge(*sides))
