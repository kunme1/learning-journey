"""来源：71 介绍.py；配套：71 介绍-优化版.md。
整理日期：2026-11-24；原始文件保留。
"""

# 变量定义 - 未指定类型注解 ---> 类型推断
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count": 2, "total": 10}
goods = ("手机", 6999, 1)

names.append("X")
names.append(10023)
names.append(10023.0)

# python 是动态语言
print(names)



# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A", "C", "E"]# or 根据真值选择并返回操作数
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count": 2, "total": 10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)

names2.append("X")
names2.append(10023)
# 教学对照：这一行故意违反list[str | int]的静态约定。
# 运行时仍可append；不擅自把联合类型加float来掩盖检查点。
names2.append(10023.0)

def calc_order_cost(*args: tuple[str, float, int], coupon: int = 0, score:int = 0, express:float = 0.0) -> float:
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额

    :param args: 商品信息（商品名、价格、数量） ---> 如：（"鼠标", 188, 2）（"键盘", 388, 1）
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """

    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费

    # 1. 计算商品总金额
    # 原先先建total_price列表再sum；改为生成器并解包，字段含义清楚，省临时列表。
    # 新知识：生成器逐项交给sum；对本课有限数值的商品三元组保持总额与执行顺序。
    total_cost = sum(price * quantity for name, price, quantity in args)

    # 2. 加载优惠券
    if total_cost >=5000 and total_cost >= coupon:
        total_cost -= coupon

    # 原写法两次score // 100；缓存抵扣金额，避免把“积分数”和“元”混淆。
    points_discount = score // 100
    # 3. 加载积分抵扣
    if total_cost >= 5000 and points_discount <= total_cost:
        total_cost -= points_discount 

    # 4. 添加运费
    total_cost += express

    return total_cost

# 测试
total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 3999, 1), coupon=10, score=4000, express=9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), coupon=10, score=4000, express=9.9)
print(total)
total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), express=9.9)
print(total)
