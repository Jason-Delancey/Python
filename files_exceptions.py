#The program is just used as practice problems in chapter 10 of 
#Python Crash Course, Eric Matthes
#files and exception handling using try/except/else
#using JSON to load/store data
#by Jason Delancey

import json

#open a text file located in the same directory and print out it's contents
#the keyword 'with' closes the file outside the 'with' block
#always returns and empty string at the end of the file

file_name = 'pi.txt'

#print the contents of the file in it's entirety
with open(file_name) as file_object:
	contents = file_object.read()
	print(contents)
	print()

#print the contents one line at a time, removing the newline chars
with open(file_name) as file_object:
	for line in file_object:
		print(line.strip())
	print()

#retain the data from a file by storing each line in a list
with open(file_name) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.strip())
	print()

#retain the data in a list and print out the data as one string
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#write to the file, append
with open(file_name, 'a') as file_object:
	file_object.write('Adding a new line to the file\n')

with open(file_name) as file_object:
	contents = file_object.read()
	print(contents)
	print()

#exception handling using try/except/else
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)

#use JSON file to store/load Python data structures
#simple way to share data between 2 programs
numbers = [2, 3, 5, 7, 56, 256]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
	json.dump(numbers, file_object)
