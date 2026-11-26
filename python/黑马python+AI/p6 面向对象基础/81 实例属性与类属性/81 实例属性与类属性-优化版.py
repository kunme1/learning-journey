"""来源：81 实例属性与类属性.py；配套：81 实例属性与类属性-优化版.md。
复盘归属：2026-11-26；整理日期：2026-11-27（北京时间）。原始文件保留。
"""

# ---------------------------- 实例属性 与 类属性 ----------------------------

class Car:
    # 类属性(所有实例对象共享的)
    wheel = 4# 轮胎数量
    tax_rate = 0.1# 购置税税率


    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2# 通过实例对象,在查找属性时,会先查找实例属性;不存在再查找类属性

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")

    def total_cost(self, discount, rate=0.1):
        # 原先临时变量total_cost赋值后立即返回；直接return表达式，含义不变。
        # 保留两次乘法和相加顺序，不改成price*(discount+rate)，避免浮点舍入差异。
        return self.price * discount + rate * self.price


# 原演示在顶层；入口保护使导入不再创建对象或打印，直接执行保留演示。
if __name__ == "__main__":
    # 测试
    c1 = Car("白色", "BYD", "汉", 180000)
    print(c1.wheel)

    # 通过类名访问类属性
    print(Car.wheel)

    c2 = Car("黑色", "Tesla", "Model Y", 260000)
    print(c2)
