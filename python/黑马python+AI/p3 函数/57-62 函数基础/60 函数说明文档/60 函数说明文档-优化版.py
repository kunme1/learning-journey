"""来源：60 函数说明文档.py；配套：60 函数说明文档-优化版.md。

保留原有圆面积、长方形面积、多返回值和解包练习。
当前 VS Code 无标题工作区的 settings 已配置新终端 PAGER/MANPAGER=type，
因此恢复课程的普通 help() 写法，不再逐个函数调用 pydoc.doc()。
同时将 len、al 这些接收结果的变量改为含义明确的名称。
原始练习文件不修改。
"""


def circle_area(r):
    """根据半径计算圆的面积，沿用本课的圆周率近似值 3.14。"""
    area = 3.14 * r ** 2
    return area


area = circle_area(10)
print(area)


def rectangle_area(l, w):
    """根据长方形的长度和宽度，计算长方形的面积。

    :param l: 长度。
    :param w: 宽度。
    :return: 长方形的面积。
    """
    area = l * w
    return area


# 原写法：两次 help(rectangle_area)，外加 __doc__ 和文件路径的排查输出。
# 改后：保留一次普通 help()，省去重复帮助和定位日志。
# 已保存新终端分页配置；用户现有终端是否生效仍未确认，不声称界面修复。
# 需重载 VS Code 并新建终端，已有终端不会自动更新 PAGER/MANPAGER。
# 行为差异：输出次数减少；函数计算、文档内容与 help() 的教学用法不变。
help(rectangle_area)

print(rectangle_area(l=20, w=10))


def circle_area_len(r):
    """根据圆的半径，计算圆的面积和周长。

    :param r: 半径。
    :return: 第一个值是圆的面积，第二个值是圆的周长。
    """
    # 沿用课程的 3.14 与 round(..., 1)，不改变本练习的计算结果。
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)


# 与长方形函数相同，使用课程的普通 help() 写法。
help(circle_area_len)

# 原写法：al = circle_area_len(10)。
# 改后名称表示“面积和周长”，便于识别元组内容；不改变计算或打印结果。
area_and_perimeter = circle_area_len(10)
print(area_and_perimeter)
print(type(area_and_perimeter))

# 原写法：area, len = circle_area_len(10)。
# 改后：用 perimeter（周长）接收第二项，避免遮蔽 Python 的内置 len()。
# 只更改变量名，保留再次调用函数和解包的教学步骤。
area, perimeter = circle_area_len(10)
print(area)
print(perimeter)
