#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("Número de alumnos: "))

if alumnos >= 100:
    precio_alumno = 65
elif alumnos >= 50:
    precio_alumno = 70
elif alumnos >= 30:
    precio_alumno = 95
else:
    precio_alumno = 4000 / alumnos

pago_compania = precio_alumno * alumnos

print("Paga cada alumno:", precio_alumno, "€")
print("Pago a la compañía:", pago_compania, "€")