"""来源：79 实例方法.py；配套：79 实例方法-优化版.md。
复盘归属：2026-11-26；整理日期：2026-11-27（北京时间）。原始文件保留。
"""

# 原类名car合法；按类名大驼峰约定改为Car，并同步构造调用。
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类型的对象初始化完毕,对象属性已经添加完毕")

    # 定义实例方法
    def running(self):
        print(f"{self.brand}{self.name} 正在高速行驶中....")

    def total_cost(self,discount, rate = 0.1):
        """
        计算提车的总费用, 包含了两个部分: 车的价格, 税费
        
        :param self: 
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        # 原先临时变量total_cost赋值后立即返回；直接return表达式，含义不变。
        # 保留两次乘法和相加顺序，不改成price*(discount+rate)，避免浮点舍入差异。
        return self.price * discount + self.price * rate

# 原演示在顶层；入口保护使导入不再创建对象或打印，直接执行保留演示。
if __name__ == "__main__":
    # 测试
    c1 = Car("red", "BWM", "X5", 500000)

    # 调用对象中的方法
    c1.running()

    total1 = c1.total_cost(0.9, 0.1)
    # 原格式含多余逗号和正数前空格；改为:.0f，只调整展示，不改费用数值。
    print(f"提车的总费用为：{total1:.0f}")

    # 设置默认值之后可以不用设置参数
    total2 = c1.total_cost(0.9)
    print(f"提车的总费用为：{total2:.0f}")
