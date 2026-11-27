"""来源：练习.Py；配套：85 运行测试-优化版.md。
复盘归属：2026-11-26；整理日期：2026-11-27（北京时间）。原始文件保留。
"""

# 原goods合法；类名按大驼峰改为Goods，构造位置同步。
class Goods:
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

    def _read_price_quantity(self):
        """前瞻：try/except捕获ValueError；此练习继续只允许正整数价格与数量。"""
        try:
            price = int(input("请输入商品价格: "))
            num = int(input("请输入商品数量: "))
        except ValueError:
            print("价格和数量必须是整数，本次操作取消。")
            return None
        return price, num

    def add_goods(self):
        name = input("请输入要添加的商品名称: ")

        for g in self.goods_list:
            if g.name == name:
                print("该商品已存在,无法重复添加!")
                return
        
        # 原直接转换，非整数会结束菜单；先统一读取、捕获错误，再追加商品对象。
        values = self._read_price_quantity()
        if values is None:
            return
        price, num = values

        if price > 0 and num > 0:
            good = Goods(name, price, num)
            self.goods_list.append(good)


        else:
            print("请输入正确范围内的价格和数量!")

    def update_goods(self):
        name = input("请输入要修改的商品名称: ")
        
        for g in self.goods_list:
            if g.name == name:
                values = self._read_price_quantity()
                if values is None:
                    return
                price, num = values

                if price > 0 and num > 0:
                    # 此前原版两次直接赋值正确；本轮原文件已采用g.update_goods，保留这项改进。
                    # 复用商品对象已有方法，把更新规则集中在一处。
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

# 原shopping_Cart混用大小写；改为shopping_cart。
# 原顶层直接启动菜单；加入口保护后，导入本文件不会要求输入。
if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart.run()
