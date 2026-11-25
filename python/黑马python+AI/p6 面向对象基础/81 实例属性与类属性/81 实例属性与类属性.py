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
        total_cost = self.price * discount + rate * self.price
        return total_cost


# 测试
c1 = Car("白色", "BYD", "汉", 180000)
print(c1.wheel)

# 通过类名访问类属性
print(Car.wheel)

c2 = Car("黑色", "Tesla", "Model Y", 260000)
print(c2)