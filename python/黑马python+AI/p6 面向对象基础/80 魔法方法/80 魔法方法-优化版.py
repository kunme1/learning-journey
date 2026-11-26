"""来源：80 魔法方法.py；配套：80 魔法方法-优化版.md。
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

    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        # 错误修复：原self.name == self.name自比较，没比较另一辆车的型号。
        # 新知识：异类对象返回NotImplemented，让解释器尝试对方的比较协议。
        if not isinstance(other, Car):
            return NotImplemented
        return (self.color == other.color
                and self.brand == other.brand
                and self.name == other.name
                and self.price == other.price)

    def __lt__(self, other):
        # 原写法直接取other.price，对异类对象可能AttributeError。
        # 返回NotImplemented不是抛NotImplementedError；最终不支持的排序仍会TypeError。
        if not isinstance(other, Car):
            return NotImplemented
        return self.price < other.price
# 原演示在顶层；入口保护使导入不再创建对象或打印，直接执行保留演示。
if __name__ == "__main__":
    # 测试
    c1 = Car("白色", "BYD", "汉", 180000)
    print(c1)

    c2 = Car("白色", "BYD", "汉", 180000)
    print(c2)

    print( c1 == c2 )

    print( c1 > c2 )# 比大小会自动调用
