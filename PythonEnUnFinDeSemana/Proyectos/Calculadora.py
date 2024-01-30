fin = False
print("""CALCULADORA
*********************
MENU  
1) Suma
2) Resta
3) División
4) Multiplicación
5) Fin""")
while not(fin):
    opc = int(input("Opción: "))    
    if(opc == 1):
        Numero1 = int(input("Número 1: "))
        Numero2 = int(input("Número 2: "))
        print("Resultado = ", Numero1+Numero2)
    elif(opc == 2):
        Numero1 = int(input("Número 1: "))
        Numero2 = int(input("Número 2: "))
        print("Resultado = ", Numero1-Numero2)
    elif(opc == 3):
        Numero1 = int(input("Número 1: "))
        Numero2 = int(input("Número 2: "))
        print("Resultado = ", Numero1/Numero2)
    elif(opc == 4):
        Numero1 = int(input("Número 1: "))
        Numero2 = int(input("Número 2: "))
        print("Resultado = ", Numero1*Numero2)
    elif(opc == 5):
        fin = True