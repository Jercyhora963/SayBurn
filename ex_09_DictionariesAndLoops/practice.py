fnam = input('Enter filename:')
fname = open(fnam)

di = dict()
for line in fname :
	words = line.split()
	for word in words :
		di[word] = di.get(word, 0) + 1

lst = list()
for key, val in di.items() :
	newtup = (val, key)
	lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
	print(key, val)