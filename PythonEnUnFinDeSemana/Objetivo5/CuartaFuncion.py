def SumarRestar(param1, param2):
    return param1 + param2, param1 - param2
    
numero1 = int(input("Escriba el primer número: ")) 
numero2 = int(input("Escriba el primer número: "))
resultadoSuma, resultadoResta = SumarRestar(numero1, numero2)

print("El resultado de la suma es: ", resultadoSuma)
print("El resultado de la resta es: ", resultadoResta)
    
     