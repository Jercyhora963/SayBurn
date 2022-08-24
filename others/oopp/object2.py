class PartyAnimal:
	x = 0
	name = ""
	def __init__(libag, z) :
	    libag.name = z
	    print(libag.name,'constructed')

	def party(libag) :
	    libag.x = libag.x + 1
	    print(libag.name, 'party count', libag.x)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
