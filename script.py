from food import Food
from drink import Drink

food1 = Food('Sandwich', 500, 330)
food2 = Food('Chocolate cake', 400, 450)
food3 = Food('Rice ball', 200, 180)

foods = [food1, food2, food3]

drink1 = Drink('Coffee', 300, 180)
drink2 = Drink('Orange juice', 200, 350)
drink3 = Drink('Green tea', 180, 150)

drinks = [drink1, drink2, drink3]

print('Food Menu')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drink Menu')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Plese select the number of food you want to order: '))
selected_food = foods[food_order]

drink_order = int(input('Plese select the number of drink you want to order: '))
selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
count = int(input('How many combos do you want?(10% discount with more than 2 orders): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください

result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
print('That is ' + str(result) + ' yen altogether!')
