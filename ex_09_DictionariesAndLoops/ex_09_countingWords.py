fname = input('Enter File : ')
if len(fname) < 1 : fname = 'clown.txt'
finam = open(fname)

di = dict()
for line in finam :
	line = line.rstrip()
	#print(line)
	wds = line.split()
	#print(wds)
	for w in wds :
		if w in di :
			di[w] = di[w] + 1
		else :
			di[w] = 1
			print('xxNEWxx')
		print(w, di[w])
#dick = dict()
#for w in wds :
#	print(w)

#print('Type of wds :', type(wds))
#print('Type of w W', type(w))
#print(len(wds))
#print(len(w))

