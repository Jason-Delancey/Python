#The program is just used as practice problems in chapter 8 of 
#Python Crash Course, Eric Matthes
#functions, modules
#by Jason Delancey

#function definition with docstring that is used to generate documentation
def greet_user(username):
	"""Prints a simple Hello message"""
	print("Hello, " + username)
	
greet_user('Lucifer')

#defining a function using a default value for the parameter
#default value can be an empty string so it's optional
def describe_pet(pet_name, animal_type='dog', animal_age=''):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet(pet_name='willie')
describe_pet(pet_name='milo', animal_type='cat')
print()

#making a funtion with a return value
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print()

#making a function with an arbitrary number of arguments for a list
#the function puts the arguments in a Tuple, not a List
def make_pizza(size, *toppings):
	"""Print the list of toppings that have been requested."""
	print('Here are the toppings: ')
	for topping in toppings:
		print('- ' + topping)

make_pizza(12, 'pepperoni')
print()
make_pizza(3, 'mushrooms', 'green peppers', 'extra cheese')
print()

#making a function with arbitrary number of arguments for a dictionary
#need to explicitly define a empty dictionary
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
		return profile

user_profile = build_profile('albert', 'einstein',
	location='princeton',
	field='physics')
print(user_profile)
print()
