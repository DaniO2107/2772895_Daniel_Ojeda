class Hexagono:
	def __init__(self, apotema, lado):
		self.apotema = apotema
		self.lado = lado
	def area(self):
		return(6*self.lado * self.apotema)/2
	def perimetro(self):
		return 6*self.lado 
