class Punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def printPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

class Triangulo:
    def __init__(self, v1, v2, v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
    def printAngulos(self):
        self.V1.printPunto()      
        self.V2.printPunto()      
        self.V3.printPunto()

v1 = Punto(1,2)              
v2 = Punto(3,4)              
v3 = Punto(5,6)

triangulo = Triangulo(v1,v2,v3)
triangulo.printAngulos()              