"""来源：72 函数的类型注解.py；配套：72 函数的类型注解-优化版.md。
整理日期：2026-11-24；原始文件保留。
"""

# 函数类型注解 
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)


# 原名al合法但缩写难懂；area_and_perimeter明确是面积、周长组成的元组。
# 仅改变量名，仍调用一次并打印整个tuple，不改变格式和计算精度。
area_and_perimeter = circle_area_len(8.5)
print(area_and_perimeter)
