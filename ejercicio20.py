#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

mes = int(input("Escribe un número entre 1 y 12: "))

if mes == 2:
    print("28 o 29 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 días")
elif mes >= 1 and mes <= 12:
    print("31 días")
else:
    print("Error: número incorrecto")