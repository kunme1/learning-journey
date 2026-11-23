"""来源：70 案例2.py；配套：70 案例2-优化版.md。
整理日期：2026-11-24；原始练习不修改。
相关改写的原因和行为差异见就近中文说明。
"""

# 同步原文件本轮默认值0→0.0；未传运费且总价全为整数时，返回值由int变float，数值不变。
def calc_order_cost(*args, coupon=0, score=0, express=0.0):
    """沿用课程顺序：扣券后余额再判断积分门槛；假定数值有限、非负，积分为整数。"""
    # 原先先建商品金额列表再sum；sum消费生成器，省去临时金额列表。
    # 解包使price/quantity含义明确。只改变表达式，保留课程扣减顺序与金额结果。
    total_cost = sum(price * quantity for name, price, quantity in args)
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    points_discount = score // 100  # 原重复score//100，命名说明单位是元而非积分。
    if total_cost >= 5000 and points_discount <= total_cost:
        total_cost -= points_discount
    return total_cost + express


def calc_order_cost_by_subtotal(*args, coupon=0, score=0, express=0.0):
    """前瞻口径示例：两次资格均按优惠前金额判断，不自动取代课程版本。"""
    # 行为变化：原价5000、券10、积分4000时，此版4950；课程顺序版4990。
    # 同时防止叠加抵扣为负：只有本次抵扣不超过当前余额才使用，与原“超额不使用”一致。
    subtotal = sum(price * quantity for name, price, quantity in args)
    remaining = subtotal
    if subtotal >= 5000 and coupon <= remaining:
        remaining -= coupon
    points_discount = score // 100
    if subtotal >= 5000 and points_discount <= remaining:
        remaining -= points_discount
    return remaining + express


if __name__ == "__main__":
    print(calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=4000,express=9.9))
    print(calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),coupon=10,score=4000,express=9.9))
    print(calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),express=9.9))
