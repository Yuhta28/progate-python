from menu_item import MenuItem

class Food(MenuItem):
    def calorie_info(self):
        print(str(self.calorie) + "kcalです")


    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

