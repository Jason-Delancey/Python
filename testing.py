#The program is just used as practice problems in chapter 10 of 
#Python Crash Course, Eric Matthes
#testing code using the unittest Python module
#by Jason Delancey

#must import the unittest module and then create a class that inherits
#from the module
import unittest

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def setUp(self):
		"""Create an instance/any variables to be used throughout the test."""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""

	def get_formatted_name(first, last):
		"""Generate a neatly formatted full name."""
		full_name = first + ' ' + last
		return full_name.title()

unittest.main()


