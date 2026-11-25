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

    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == self.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price
# 测试
c1 = car("白色", "BYD", "汉", 180000)
print(c1)

c2 = car("白色", "BYD", "汉", 180000)
print(c2)

print( c1 == c2 )

print( c1 > c2 )# 比大小会自动调用

