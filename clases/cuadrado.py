class Cuadrado :
	def __init__ (self, lado):
		self.__lado = lado
#	def get_lado(self):
#		return self.__lado
	def set_lado(self, nuevo_lado):
		if nuevo_lado > 0:
			self.lado = nuevo_lado

		else:
			pass

	def area(self):
		return self.__lado**2
	def perimetro(self):
		return	4*self.__lado

lado_cuadrado = 8
mi_cuadrado = Cuadrado(lado_cuadrado)
print(f"Area del cuadrado : {mi_cuadrado.area()}")
print(f"perimetro del cuadrado  {mi_cuadrado.perimetro()}")
mi_cuadrado.set_lado(5)
print(f"perimetro del cuadrado {mi_cuadrado.perimetro()}")
print(f"Area del cuadrado {mi_cuadrado.area()}")



