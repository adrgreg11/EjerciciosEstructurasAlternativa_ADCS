#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num2 == 0:
    print("No se puede dividir entre cero")
else:
    print(num1 / num2)