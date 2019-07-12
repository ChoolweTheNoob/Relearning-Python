my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("My firends favourite foods are:")
print(friend_foods)

# Exercise 4-12

print("My favourite foods are: ")
for food in my_foods:
    print(food)

print("My friends favourite foods are: ")
for food in friend_foods:
    print(food)