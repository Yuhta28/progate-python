class MenuItem:
    def info(self):
        print("メニューの名前と値段が表示されます")

menu_item1 = MenuItem()
menu_item1.name = "サンドイッチ"
print(menu_item1.name)

menu_item1.price = 500
print(menu_item1.price)

menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = "チョコケーキ"
print(menu_item2.name)

menu_item2.price = 400
print(menu_item2.price)

menu_item2.info()
