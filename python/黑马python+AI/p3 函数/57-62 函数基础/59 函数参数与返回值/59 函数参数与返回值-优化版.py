"""来源：59 函数参数与返回值.py；配套：59 函数参数与返回值-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

# 函数的参数与返回值

# 函数1：计算圆的面积 -- 半径
def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)


# 函数2：计算长方形的面积 -- 长、宽
def rectangle_area(l, w):
    area = l * w
    return area

print(rectangle_area(l=20, w=10))

# 函数3：计算圆的面积、周长 -- 半径 ---> 如果返回值有多个，多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)


# 原al含义不清；新名说明元组中同时保存面积与周长，结果不变。
area_and_perimeter = circle_area_len(10)
print(area_and_perimeter)
print(type(area_and_perimeter))


# 原len遮蔽内置len，改perimeter（周长）；保留再次调用与解包教学。
area, perimeter = circle_area_len(10)  # 解包
print(area)
print(perimeter)
