#The program is just used as practice problems in chapter 9 of 
#Python Crash Course, Eric Matthes
#classes
#by Jason Delancey
"""A class used to describe a Dog"""

class Dog():
	"""A simple attempt to model a dog."""
	
	#every method associated with a class passes 'self' to reference itself
	#the init method returns an instance of the class
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
	
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

#using inheritance with classes
#the name of the parent class must be in parentheses
class HotDog(Dog):
	"""Represents aspects of the Dog class"""
	
	def __init__(self, name, age):
		"""Initialize attributes of the parent class"""
		
		super().__init__(name, age)
		#now you can create new attributes unique to the HotDog class
		self.weight = 20
		
	#you can override a method from the parent class
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over AND OVER!")
		
		