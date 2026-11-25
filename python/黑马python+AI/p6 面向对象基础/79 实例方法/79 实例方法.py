class car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类型的对象初始化完毕,对象属性已经添加完毕")

    # 定义示例方法
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
        total_cost = self.price * discount + self.price * rate
        return total_cost

# 测试
c1 = car("red", "BWM", "X5", 500000)

# 调用对象中的方法
c1.running()

total1 = c1.total_cost(0.9, 0.1)
print(f"提车的总费用为:, {total1: .0f}")

# 设置默认值之后可以不用设置参数
total2 = c1.total_cost(0.9)
print(f"提车的总费用为:, {total2: .0f}")
