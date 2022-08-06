xfile =open('../ex_05_01/ex_05_01.py')
count = 0
for cheese in xfile :
	cheese = cheese.rstrip()
	print(cheese)
	count += 1
	# print(count)
print('Line Count :', count)
print(cheese)
