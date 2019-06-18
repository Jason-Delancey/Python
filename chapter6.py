#The program is just used as practice problems in chapter 5 of 
#Python Crash Course, Eric Matthes
#by Jason Delancey

#store user information
print('Creating a Dictionary:')
user_0 = {
	'first_name': 'lucifer',
	'last_name': 'morningstar',
	'age': 12,
	'city': 'Los Angeles',
}
print(user_0)
print()

users = {
	'beerus': 104,
	'kakorat': 39,
	'goku': 41, 
	'vegeta': 934, 
	'broly': 104, 
	'bulma': 39,
	'raditz': 435
}

#Print out dictionary information
print('Printing out keys and values in a Dictionary: ')
print(users)
for key,value in users.items():
	print("Key: " + key)
	print("Value: " + str(value))
print('List of keys sorted:')
print(sorted(users.keys()))
print('List of values sorted:')
print(sorted(users.values()))
print()

print('Nesting Dictionaries and Lists:')
#Make an empty list for storing aliens.
aliens = []

#Make 30 green aliens and then add them to the List.
if aliens:
	for alien_number in range(30):
		new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
		aliens.append(new_alien)

print('Show the first 5 aliens:')
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))