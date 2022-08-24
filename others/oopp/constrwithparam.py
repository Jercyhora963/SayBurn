class PartyAnimal:
	x = 0
	name = ""
	def __init__(self, pandesal):
		self.name = pandesal
		print(self.name,"constructed")

	def party(self):
		self.x = self.x + 1
		print(self.name,"party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
jh = PartyAnimal('Jercy')
jh.party()
j.party()
s.party()
j.party()
jh.party()
jh.party()
e = PartyAnimal('Eva')
e.party()
e.party()
t = PartyAnimal("Theoz")
t.party()
jh.party()
e.party()
j.party()
s.party()
e.party()
j.party()

