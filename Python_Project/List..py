from typing import List

Z = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101]
print(Z[5])
Y = list(Z[3:9:2])
print(Y)
print(Z == Y)

X = [2, 3, 3, 4, 5, 6, 7, 7, 9, 6, 3]
print(X[3:9:2])

print(Z)

del Z[11]
print(Z)

Z.append(120)
print(Z)

Z.extend([110, 130, 150, 140])
print(Z)

Z.sort()
print(Z)

print(Z[::-1])

Foods = ['Beans', 'Bread', 'Wheat', 'Pastry']
Drinks = ['Water', 'Lemonade', 'Fruit Juice']
Meal: list[str] = Foods+Drinks
print('Meal=', Meal)
Meal.sort()
print('Dish=', Meal)
