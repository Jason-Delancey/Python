#The program is just used as practice for using string methods
#by Jason Delancey

user_name = "Jason"
message = "Hello " + user_name + ", would you like to learn some Python today?"
print(message)

print(user_name.upper())
print(user_name.lower())
print(user_name.title())
print()

famous_person = "Albert Einstein" 
message = famous_person + ' once said,'
message = message + " 'A person who never made a mistake never tried anything "
message = message + "new.'"
print(message)
print()

aName = '\tJason'
print(aName)
print(aName.lstrip())
print(aName.rstrip())
print(aName.strip())