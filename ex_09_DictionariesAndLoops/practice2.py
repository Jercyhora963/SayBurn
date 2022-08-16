fh = input('Input filename :')
fname = open(fh)

di = dict()
for line in fname :
	line = line.rstrip()
	words = line.split()
	for word in words :
		di[word] = di.get(word, 0) + 1

lst = list()
for k, v in di.items() :
	lst.append( (v, k) )

lst = sorted(lst, reverse=True)

for v, k in lst[:10] :
	print(v, k)
