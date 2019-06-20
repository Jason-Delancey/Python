#The program is just used as practice problems in chapter 5 of 
#Python Crash Course, Eric Matthes
#COnditionals, Lists, Range
#by Jason Delancey

#if chain
alien_color = 'red'
if alien_color.lower() == 'red':
	print("Congrats! You just earned 5 points!")
	
alien_color = 'yellow'
if alien_color.lower() == 'red':
	print("Congrats! You just earned 5 points!")
	
#if/else chain
alien_color = 'red'
if alien_color.lower() == 'green':
	print("Congrats! You just earned 5 points!")
else:
	print("Congrats! You just earned 10 points!")
	
#if/elif/else chain
alien_color = 'red'
if alien_color.lower() == 'green':
	print("Congrats! You just earned 5 points!")
elif alien_color.lower() == 'yellow':
	print("Congrats! You just earned 10 points!")
elif alien_color.lower() == 'red':
	print("Congrats! You just earned 15 points!")
	
print()

#make sure the list is not empty before running the for loop
ages = [1,3,10,15,25,70]
if ages:
	for age in ages:
		if age < 2:
			print("You're a baby!")
		elif age >= 2 and age < 4:
			print("You're just a toddler.")
		elif age >=4 and age < 13:
			print("You're a kid.")
		elif age >= 13 and age <20:
			print("You're a teenager.")
		elif age >= 20 and age < 65:
			print("You're an adult.")
		elif age >= 65:
			print("You're an elder")
print()

userNames = ['admin', 'john', 'jane', 'joe', 'carol', 'dean']
#userNames = []
if userNames:
	for user in userNames:
		user = user.title()
		if user == 'admin':
			print("Hello " + user + ", would you like to see a status report?")
		else:
			print("Hello " + user + ", thank you for logging in again.")
else:
	print("We need to find some users!")
print()

#make sure new usernames are unique
new_users = ['john', 'kakorat', 'goku', 'vegeta', 'broly', 'dean']
if userNames and new_users:
	for user in new_users:
		user = user.lower()
		if user in userNames:
			print("Sorry but " + user + " is taken. Pick a new username.")
		else:
			print(user + " is available.")
print()

#storing ordinal numbers
ordinal = list(range(1,10))
if ordinal:
	for number in ordinal:
		if number == 1:
			print(str(number) + 'st')
		elif number == 2:
			print(str(number) + 'nd')
		elif number == 3:
			print(str(number) + 'rd')
		else:
			print(str(number) + 'th')
	
		
