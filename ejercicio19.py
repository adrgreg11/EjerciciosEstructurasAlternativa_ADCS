#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

mes = int(input("Escribe un número entre 1 y 12: "))

if mes == 2:
    print("28 o 29 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 días")
elif mes >= 1 and mes <= 12:
    print("31 días")
else:
    print("Error: número incorrecto")