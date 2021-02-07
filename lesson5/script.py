from food import Food
from drink import Drink
import random

food1 = Food("サンドイッチ",500,330)
food2 = Food("チョコケーキ",400,450)
food3 = Food("シュークリーム",200,180)

foods = [food1,food2,food3]

drink1 = Drink("コーヒー",300,180)
drink2 = Drink("オレンジジュース",200,350)
drink3 = Drink("エスプレッソ",500,30)

drinks = [drink1,drink2,drink3]

print("食べ物メニュー")
index = 0
for food in foods:
    print(str(index) + ". " + food.info())
    index += 1

print ("飲み物メニュー")
index = 0
for drink in drinks:
    print(str(index) + ". " + drink.info())
    index += 1

print("--------------------")

#food_order = int(input("食べ物の番号を選択してください: "))
food_order = random.randint(0,2)
selected_food = foods[food_order]

#drink_order = int(input("飲み物の番号を選択してください: "))
drink_order = random.randint(0,2)
selected_drink = drinks[drink_order]

#count = int(input("何セット買いますか？(3つ以上で1割引): "))
count_food  = random.randint(1,5)
count_drink = random.randint(1,5)
result = selected_food.get_total_price(count_food) + selected_drink.get_total_price(count_drink)
print("選んだ食べ物：" + selected_food.info())
print("選んだ飲み物：" + selected_drink.info())
print("個数：食べ物 " + str(count_food) + " 飲み物 " + str(count_drink))
print("合計は" + str(result) + "円です")
