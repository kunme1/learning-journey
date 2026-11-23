# # -------------------- 函数 - 不定长参数(位置参数 *args --> 元组) --------------------

# # 需求：根据传入的这些数据，计算这些数据的最小值，最大值，平均值
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data, 1)


# # 调用函数
# print(calc_data(2, 7, 9, 10, 45))
# print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))



# -------------------- 函数 - 不定长参数(关键字参数 *kwargs --> 字典) --------------------

# 需求：根据传入的这些数据，计算这些数据的最小值，最大值，平均值
def calc_data(*args, **kwargs):
    """
    根据传入的这些数据，计算这些数据的最小值、最大值、平均值

    :param args: 不定长位置参数，需要计算的这些数据
    :param kwargs: 不定长关键字参数
        round: 保留的小数位个数
        print: 是否打印输出
    :return: 最小值、最大值、平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(sum(args) / len(args), kwargs.get("round"))

    if kwargs.get("print"):# 本身就是bool类型,不用再判断
    
        print(f"计算出来的最大值:{max_data}, 最小值:{min_data}, 平均值:{avg_data}")

    return min_data, max_data, avg_data


# 调用函数
print(calc_data(2, 7, 9, 10, 45, round = 3, print = True))
print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222,round = 2))