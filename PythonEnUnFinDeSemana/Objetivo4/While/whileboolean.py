continuar = True

while continuar:
    valor = int(input("Escribe un valor mayor a 100: "))
    if valor >= 100:
        print("El valor es mayor a 100")
    else:
        continuar = False
print("Programa acabado") 