def SumarValores(*valores):
    resultado = 0
    for item in valores:
        resultado = resultado + item
    return resultado

resultado = SumarValores(23,54,3,76,2)
print("El resultado de la suma de valores es: ", resultado)