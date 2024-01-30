class Cardinalatrib:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

p1 = Cardinalatrib(4,6)
p1.MostrarPunto()

p2 = Cardinalatrib(3,8)
p2.MostrarPunto()

p1 = p2
p1.MostrarPunto()
