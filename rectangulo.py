class Rectangulo:
    def __init__(self, longitud, altura):
        self.longitud = longitud
        self.altura = altura 

    def area(self):
        return self.longitud * self.altura
    
    def perimetro(self):
        return 2 * (self.longitud + self.altura)
