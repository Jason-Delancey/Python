#create a list
names = ['Jane', 'John', 'Jill']
print(names[0])
print(names[1])
print(names[2])

message = names[2] + ' found out that ' + names[0] 
message = message + ' has a brother named ' + names[1]
print(message)

absent = 'Jane'
message = 'It looks like ' + absent + " can't make it."
print(names)
print(message)

#add/remove elements of a list
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
places = ['aruba', 'jamaica', 'canada', 'california', 'japan']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
places.reverse()
print(places)
places.reverse()
print(places)
print(len(places))
print()

#using a for-loop to print from a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print("This magician's name is: " + magician)
print("Those are all of the magicians.\n")

#print a range of numbers
for value in range(1,5):
	print(value)
print()

#print a range of numbers	
even_numbers = list(range(2,11,2))
print(even_numbers)
print()

#print the squares of a range of numbers
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

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
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
print(players[2:])
print(players[0:2])
print(players[-3:])
print()

#copy a list
all_stars = players[:]
all_stars.append('lucifer')
print(all_stars)
print(players)
print()

#create an immutable tuple. tuples are immutable but reassigning values 
#for a variable is a valid operation
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)