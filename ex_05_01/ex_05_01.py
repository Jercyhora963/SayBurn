num = 0
tot = 0
while True :
	sval = input('Input a number : ')
	if sval == 'done' :
		break
	try :
		fval = float(sval)
		num = num + 1
		tot = tot + fval
	except :
		print('invalid input')
		continue
print('ALL DONE!')
print('total ', tot)
print('average ', tot/num)
