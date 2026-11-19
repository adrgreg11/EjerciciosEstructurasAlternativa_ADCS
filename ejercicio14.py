precio = float(input("Precio inicial por kilo (€): "))
tipo = input("Tipo de uva (A o B): ").upper()
tamano = int(input("Tamaño (1 o 2): "))
kilos = float(input("Kilos entregados: "))

if tipo == "A" and tamano == 1:
    precio += 0.20
elif tipo == "A" and tamano == 2:
    precio += 0.30
elif tipo == "B" and tamano == 1:
    precio -= 0.30
elif tipo == "B" and tamano == 2:
    precio -= 0.50

ganancia = precio * kilos
print("El productor recibirá:", ganancia, "€")