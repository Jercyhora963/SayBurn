f = input('Enter filename     :.')
fname = open(f)

box = dict()
for line in fname :
	line = line.rstrip()
	words = line.split()
	for word in words :
		box[word] = box.get(word, 0) + 1
		print(box)
print('Last :', box)
