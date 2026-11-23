# 函数的参数与返回值

# 函数1：计算圆的面积 -- 半径
def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)


# 函数2：计算长方形的面积 -- 长、宽
def rectangle_area(l, w):
    """
    根据长方形的长度和宽度,计算长方形的面积

    :param l: 长度
    :param w: 宽度
    :return: 长方形的面积

    """
    area = l * w
    return area

# 查看函数功能
print(rectangle_area.__doc__)              # 当前函数实际保存的文档说明
print(rectangle_area.__code__.co_filename) # 当前函数定义所在的文件
help(rectangle_area)
help(rectangle_area)



print(rectangle_area(l=20, w=10))

# 函数3：计算圆的面积、周长 -- 半径 ---> 如果返回值有多个，多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    """
    根据圆的半径，计算圆的面积和周长

    :param r: 半径
    :return: 圆的面积，圆的周长
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

help(circle_area_len)

al = circle_area_len(10)
print(al)
print(type(al))


area, len = circle_area_len(10)  # 解包
print(area)
print(len)