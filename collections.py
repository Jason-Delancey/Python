#The program is just used as practice for using lists
#by Jason Delancey

#create a list
names = ['Jane', 'John', 'Jill']
print('Names in the list:')
print(names[0])
print(names[1])
print(names[2])
print(names)
print(names[2] + ' found out that ' + names[0] + 
	' has a brother named ' + names[1])
absent = 'Jane'
print('It looks like ' + absent + " can't make it.\n")

#add/remove elements of a list
print('Adding and removing elements:')
newName = 'Batman'
names.remove(absent)
names.append(newName)
names.insert(0, newName)
print(names)
names.pop()
del names[0]
names.pop()
names.pop()
print(names)
print()

#sort the order of a list
print('Sorting a list:')
places = ['aruba', 'jamaica', 'canada', 'california', 'japan', 'canada']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))

#another way to reverse the sorted order
places.reverse()
print(places)
places.reverse()
print(places)

print(len(places))
print()

#can also print a sorted list and remove duplicate objects by using a Set
#all objects in a Set must be unique
print('Printing a sorted list with unique objects:')
print(sorted(set(places)))
print()

#using a for-loop to print from a list
print('Using a for-loop to print objects:')
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print("This magician's name is: " + magician)
print("Those are all of the magicians.\n")

#print a range of numbers (remember the range is NOT a stored list)
print('Printing a range of numbers:')
for value in range(1,5):
	print(value)
print()

#turn a range of numbers into a list and then print the range of numbers	
even_numbers = list(range(2,11,2))
print(even_numbers)
print()

#print the list of squares of a range of numbers
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#print the list of squares of a range of numbers using list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
print()

#print the numbers from 1-20, using list comprehension
numbers = [print(value) for value in range(1,21)]
print()

#make list of numbers from 1-a million
numbers = list(range(1,1000001))
#print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()

#print out odd numbers from 1-20
numbers = [print(value) for value in range(1,21,2)]
print()

#print out the mulitples of 3, from 3-30
numbers = [print(value) for value in range(3,31,3)]
print()

#print out the first 10 cubes
numbers = [print(value**3) for value in range(1,11)]
print()

#print a slice of a list
print('Printing a slice of a list:')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
print(players[2:])
print(players[0:2])
print(players[-3:])
print()

#copy a list
print('Printing an independent copy of a list and appending to it:')
all_stars = players[:]
all_stars.append('lucifer')
print(all_stars)
print(players)
print()

#create a tuple. tuples are immutable but reassigning values 
#for a variable is a valid operation
print('Using Tuples:')
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
print()

#create a dictionary
print('Using Dictionaries:')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.
alien_0 = {
	'x_position': 0,
	'y_position': 25,
	'speed': 'medium',
	}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))