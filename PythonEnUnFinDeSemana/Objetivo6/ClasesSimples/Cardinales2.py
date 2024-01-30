class Cardinales2:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")



p1 = Cardinales2(4,6)
p1.MostrarPunto()

p2 = Cardinales2(-5,9)
p2.MostrarPunto()

p3 = Cardinales2(3,-7)
p3.MostrarPunto()

p4 = Cardinales2(0,4)
p4.MostrarPunto()