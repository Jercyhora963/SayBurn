fhand  = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	wds = line.split()
	print(wds[0])
