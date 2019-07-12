animals = ['lion','jaguar','tiger','cheetah','panther','leopard','wolf']

for animal in animals:
    print("A " + animal.title() + " would make a great pet")

print("Any of these animals would make a great pet!")

print("The first three items in the list are: ")
for animal in animals[:3]:
    print(animal.title())

print("The three items from the middle of the list are: ")
for animal in animals[2:5]:
    print(animal.title())

print("The last three items in the list are: ")
for animal in animals[-3:]:
    print(animal)