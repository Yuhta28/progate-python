class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ": ¥" + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price

menu_item1 = MenuItem("サンドイッチ",500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)

print("合計は" + str(result) + "円です")
