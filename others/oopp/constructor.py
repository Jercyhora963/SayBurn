class PartyAnimal:
	x = 1

	def __init__(self):
		print('I am constructed')

	def party(self):
		self.x = self.x + 1
		print(self.x)

	def __del__(self):
		print('I am destructed')

an = PartyAnimal()

an.party()
an.party()
an = 5
print('an containts', an)
