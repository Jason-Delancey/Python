names = ['Jane', 'John', 'Jill']
print(names[0])
print(names[1])
print(names[2])

message = names[2] + ' found out that ' + names[0] + ' has a brother named ' + names[1]
print(message)

absent = 'Jane'
message = 'It looks like ' + absent + " can't make it."
print(names)
print(message)

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

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)