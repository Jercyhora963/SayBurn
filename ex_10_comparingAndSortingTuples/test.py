f = input('Enter filename     :.')
fname = open(f)

box = dict()
for line in fname :
	line = line.rstrip()
	words = line.split()
	for word in words :
		box[word] = box.get(word, 0) + 1

largest = -1
for a, b in box.items() :
	if b > largest :
		largest = b
		print(largest)
