"""来源：54 案例实现.py；配套：54 案例实现-优化版.md。
整理日期：2026-11-23；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

from math import isfinite


def read_product():
    """读取价格、数量；新增规则：价格有限且非负，数量为正整数。"""
    # 原float/int直接转换会因文字输入退出。新try/except提示重输，成功才返回。
    # 行为变化：拒绝负价、非有限价和非正数量；无业务持久化或网络副作用。
    while True:
        try:
            price = float(input("请输入商品价格: "))
            quantity = int(input("请输入商品数量: "))
        except ValueError:
            print("价格须为数字，数量须为整数，请重新输入")
            continue
        if isfinite(price) and price >= 0 and quantity > 0:
            return {"price": price, "num": quantity}
        print("价格须有限且非负，数量须为正整数")


shopping_cart = {}
menu = "1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车  5.退出购物车"
print("欢迎使用购物车管理系统 ~")
while True:
    # 原54菜单只在循环前显示；现在每轮显示，改变提示时机，方便继续选择。
    print(menu)
    choice = input("请选择要执行的操作(1-5):")
    match choice:
        case "1":
            goods_name = input("请输入商品名称: ")
            # 原先先读价格数量才查重复；现在提前判断，重复时少两次无效输入。
            if goods_name in shopping_cart:
                print("商品已存在,请重新选择")
                continue
            shopping_cart[goods_name] = read_product()
            print("商品已添加完毕 ~")
        case "2":
            goods_name = input("请输入要修改的商品名称: ")
            # 先确认存在，再读取新值；continue回菜单，不是退出整个系统。
            if goods_name not in shopping_cart:
                print("商品不存在,请重新选择")
                continue
            shopping_cart[goods_name] = read_product()
            print("商品已修改完毕 ~")
        case "3":
            goods_name = input("请输入要删除的商品名称: ")
            if goods_name not in shopping_cart:
                print("商品不存在,请重新选择")
            else:
                del shopping_cart[goods_name]
                print("商品已删除完毕 ~")
        case "4":
            # 原54遍历shopping_cart.keys（方法对象）会TypeError；55已补()。
            # items一次取得名称与信息，替代keys()+下标；等价于55的合法查询。
            if not shopping_cart:
                print("购物车为空")
            for goods_name, goods_info in shopping_cart.items():
                # 外双内单，兼容Python3.10/3.11；原同引号在3.12+本来合法。
                print(f"商品名称: {goods_name}, 商品价格:{goods_info['price']}, 商品数量: {goods_info['num']}")
        case "5":
            print("Bye ~")
            break
        case _:
            print("非法操作,不支持")
