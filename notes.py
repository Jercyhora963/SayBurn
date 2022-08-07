print('Concatenating lists using +')

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print('_______END_______')

print('Lists can be sliced using :')

t = [9, 41, 12, 3, 74, 15]
t[1:3]
print(t[1:3])
print('Answer [41, 12]')
print('__')
print(t[:4])
print('Answer[9, 41, 12, 3]')
print('__')
print(t[3:])
print('Answer: [3, 74, 15]')
print('__')
print(t[:])
print('Answer: [9, 41, 12, 3, 74 15]')
print('__')
print('Building a List from Scratch')
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)


item = ['sapatos', 'lunchbox', 'uniform', 'cap']
for items in item :
    soritem = item.sort()
    soritem = item.rstrip()
    print(soritem)