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
		#if the key is not there the count is zero
		oldcount = di.get(w,0)
		print(w, 'Old', oldcount)
		newcount = oldcount +1
		di[w] = newcount
		print(w, 'New', newcount)


# ------------------------------------------------------------------
#		if w in di :
			#print('xxEXISTINGxx')
#			di[w] = di[w] + 1
#		else :
#			di[w] = 1
			#print('xxNEWxx')
#		print(w, di[w])
#
#print(di)
# --------------------------------------------------------------------------
#---------------------------------------------------------------------------
#dick = dict()
#for w in wds :
#	print(w)

#print('Type of wds :', type(wds))
#print('Type of w W', type(w))
#print(len(wds))
#print(len(w))
#----------------------------------------------------------------------------
print('https://www.youtube.com/watch?v=PrhZ9qwBDD8')
