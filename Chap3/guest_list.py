guest_list = ['Freud','Jung','James',]

# this is so much is easier with a loop!
message = guest_list[0] + ", You are invited for dinner tonight"
print(message)

message = guest_list[1] + ", You are invited for dinner tonight"
print(message)

message = guest_list[2] + ", You are invited for dinner tonight"
print(message)


message = guest_list[0] + " can't make it."
print(message)

guest_list[0] = 'Peterson'

message = guest_list[0] + ", You are invited for dinner tonight"
print(message)

message = guest_list[1] + ", You are invited for dinner tonight"
print(message)

message = guest_list[2] + ", You are invited for dinner tonight"
print(message)

print("I found a bigger table bitches!")
guest_list.insert(0, 'Pavlov')
guest_list.insert(2, 'Kahneman')
guest_list.append('Ekman')

message = guest_list[0] + ", You are invited for dinner tonight"
print(message)

message = guest_list[1] + ", You are invited for dinner tonight"
print(message)

message = guest_list[2] + ", You are invited for dinner tonight"
print(message)
message = guest_list[3] + ", You are invited for dinner tonight"
print(message)
message = guest_list[4] + ", You are invited for dinner tonight"
print(message)
message = guest_list[5] + ", You are invited for dinner tonight"
print(message)

number_of_guests = len(guest_list)
message = str(number_of_guests) + " guests are invited."
print(message)

print("Sorry guys, I can only invite two people")

person = guest_list.pop()
message = person + ", your invitation has been cancelled"
print(message)

person = guest_list.pop()
message = person + ", your invitation has been cancelled"
print(message)

person = guest_list.pop()
message = person + ", your invitation has been cancelled"
print(message)

person = guest_list.pop()
message = person + ", your invitation has been cancelled"
print(message)

number_of_guests = len(guest_list)
message = str(number_of_guests) + " guests are invited."
print(message)

message = guest_list[0] + ", You're still invited"
print(message)

message = guest_list[1] + ", You're still invited"
print(message)


del guest_list[-1]
del guest_list[-1]
print(guest_list)

number_of_guests = len(guest_list)
message = str(number_of_guests) + " guests are invited."
print(message)