#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido. • Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2 5 y 3-4. • Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.

numero = int(input("Resultado del dado (1-6): "))

if numero == 1:
    print("Seis")
elif numero == 2:
    print("Cinco")
elif numero == 3:
    print("Cuatro")
elif numero == 4:
    print("Tres")
elif numero == 5:
    print("Dos")
elif numero == 6:
    print("Uno")
else:
    print("ERROR: número incorrecto.")