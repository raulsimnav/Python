cadenaisalnum1 = "Hola me gusta el pan"
print(cadenaisalnum1.isalnum())
print("---------------------------------------")
cadenaisalnum2 = "1234567890"
print(cadenaisalnum2.isalnum())
print("---------------------------------------")
cadenaisalnum3 = "Holanúmero123"
print(cadenaisalnum3.isalnum())
print("---------------------------------------")
cadenaisalnum3 = "Hola número 123"
print(cadenaisalnum3.isalnum())

# * .isalnum se utilza para que nos diga si hay números o no en la cadena
# ! OJO, .isalnum detecta que hay números si toda la sentencia de la cadena está junto, si nos, dará false