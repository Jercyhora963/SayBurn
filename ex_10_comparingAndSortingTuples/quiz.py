#which does the same thing as following code :

lst = []
for key, val in counts.items() :
	newtup = (val, key)
	lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

print( sorted ( [ (v,k) for k,v in counts.items() ], reverse=True ) )
#print( [ (k,v) for k,v in counts.items().sorted() ] )
#print( sorted( [v,k) for k,v in counts.key() ] ) )
#print( [ (k,v) for k,v in counts.values().sort() ] )

