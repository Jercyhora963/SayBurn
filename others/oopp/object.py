class PartyAnimal:
#class is a reserverd word
#This is the temple for making PartyAnimal objects.
	x = 0
	#Each PartyAnimal object has a bit of data.
	#Each PartyAnimal object has a bit of code.
	def party(self):
		self.x = self.x + 1
		print("So far",self.x)
		#Each PartyAnimal object has a bit of code.
an = PartyAnimal()
#Construct a PartyAnimal object and store in an

an.party()
an.party()
an.party()
#Tell the an object to run the party() code within it.
#Similar to  " PartyAnimal.party(an)
print('Dir ', dir(an))
