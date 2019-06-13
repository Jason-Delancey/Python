#use if conditional
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
print()
		
#inequality testing
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")
print()

#checking multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
print()

#compare a value with elements in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")
else: 
	print()
	
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

#check to ensure the list is not empty first
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
		print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
print()

#compare multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")