def Sumar():
    Numero1 = int(input("Escriba un número: "))
    Numero2 = int(input("Escriba un número: "))
    resultado = Numero1+Numero2
    print("El resultado de la suma es: ", resultado)
    
def Restar():
    Numero1 = int(input("Escriba un número: "))
    Numero2 = int(input("Escriba un número: "))
    resultado = Numero1-Numero2
    print("El resultado de la resta es: ", resultado)
     
def Multiplicar():
    Numero1 = int(input("Escriba un número: "))    
    Numero2 = int(input("Escriba un número: "))
    resultado = Numero1*Numero2
    print("El resultado de la multiplicación es: ", resultado)

def Division():
    Numero1 = int(input("Escriba un número: "))        
    Numero2 = int(input("Escriba un número: "))
    resultado = Numero1/Numero2
    print("El resultado de la división es ", resultado)
    
def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Escoja una opción: "))
        if(opc == 1):
            Sumar()
        elif(opc == 2):
            Restar()
        elif(opc == 3):
            Division()
        elif(opc == 4):
            Multiplicar()
        elif(opc == 5):
            fin = True   

print("""CALCULADORA
*********************
MENU  
1) Suma
2) Resta
3) División
4) Multiplicación
5) Finalizar programa""")

Calculadora()                
            
                