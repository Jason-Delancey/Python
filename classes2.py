#The program is just used as practice problems in chapter 9 of 
#Python Crash Course, Eric Matthes
#classes
#by Jason Delancey
from classes import Dog, HotDog

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
print()
your_dog = Dog('Jamie', 4)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
print()

my_hotdog = HotDog("Simon", 5)
my_hotdog.sit()
my_hotdog.roll_over()