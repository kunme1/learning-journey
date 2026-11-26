class goods:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"

    def update_goods(self, price, num):
        self.price = price
        self.num = num

class ShoppingCart:
    cart_version = "1.0"

    def __init__(self):
        self.goods_list = []

    def add_goods(self):
        name = input("请输入要添加的商品名称: ")

        for g in self.goods_list:
            if g.name == name:
                print("该商品已存在,无法重复添加!")
                return
        
        price = int(input("请输入商品价格: "))
        num = int(input("请输入商品数量: "))

        if price > 0 and num > 0:
            good = goods(name, price, num)
            self.goods_list.append(good)


        else:
            print("请输入正确范围内的价格和数量!")

    def update_goods(self):
        name = input("请输入要修改的商品名称: ")
        
        for g in self.goods_list:
            if g.name == name:
                price = int(input("请输入商品价格: "))
                num = int(input("请输入商品数量: "))

                '''
                try:
                    price = int(input("请输入商品价格: "))
                    num = int(input("请输入商品数量: "))
                except ValueError:
                    print("价格和数量必须是整数!")
                    return
                '''
                
                if price > 0 and num > 0:
                    g.update_goods(price, num)
                    return

                else:
                    print("请输入正确范围内的价格和数量!")
                    return

        print("未找到该商品!")

    def del_goods(self):
        name = input("请输入要删除的商品名称: ")
                
        for g in self.goods_list:
            if g.name == name:
                self.goods_list.remove(g)
                print("删除成功 ~")
                return

        print("未找到该商品!")

    def query_goods(self):
        for g in self.goods_list:
            print(g)

    def run(self):
        print(f"欢迎使用购物车管理系统 V{self.cart_version}")

        while True:

            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("#  1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车 5.退出购物车  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

            print()

            choice = input("请选择要执行的操作,输入 1-5: ")

            match choice:
                case "1":
                    self.add_goods()
                case "2":
                    self.update_goods()
                case "3":
                    self.del_goods()
                case "4":
                    self.query_goods()
                case "5":
                    break
                case _:
                    print("输入错误,请在1-5之间选择菜单功能")

shopping_Cart = ShoppingCart()
shopping_Cart.run()


