#The program is just used as practice problems in chapter 7 of 
#Python Crash Course, Eric Matthes
#User input, while loops, flags, break, continue
#by Jason Delancey

#user input is saved in a string
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#use the int() class to cast a string to an int, if needed
height = input("\nHow tall are you, in inches? ")
if height.isdigit():
	height = int(height)
	if height >= 36:
		print("\nYou're tall enough to ride!")
	else:
		print("\nYou'll be able to ride when you're a little older.")
else:
	print("That's not a digit.")

#modular arithmetic practice
number = input("\nEnter a number, and I'll tell you if it's even or odd: ")
if number.isdigit():
	number = int(number)
	if number % 2 == 0:
		print("\nThe number " + str(number) + " is even.")
	else:
		print("\nThe number " + str(number) + " is odd.")
else:
	print("That's not a digit.\n")

#while loops
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

#using flags to control while loops
#you can also use 'break' to break any loop or 'continue' to return the 
#beginning of a loop
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'q' to end the program. "

active = True
while active:
	message = input(prompt)
	if message == 'q':
		active = False
	else:
		print(message)
	
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
print()

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
print()

#use a while loop to edit a list and a for loop to query a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)
