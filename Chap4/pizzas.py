pizzas = ['margherita','pepperoni','hawaiian','cheese']

for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I love pizza!")

#4-11

friends_pizzas = pizzas[:]

friends_pizzas.append('mushrooms')

print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza.title())

print("My friends favourite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza.title())