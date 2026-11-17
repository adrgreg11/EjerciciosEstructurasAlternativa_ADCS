#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados: exteriores tangentes exteriores secantes tangentes interiores interiores concéntricas

import math

x1 = float(input("x del centro de la primera: "))
y1 = float(input("y del centro de la primera: "))
r1 = float(input("Radio de la primera: "))

x2 = float(input("x del centro de la segunda: "))
y2 = float(input("y del centro de la segunda: "))
r2 = float(input("Radio de la segunda: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distancia == 0:
    print("Concéntricas")
elif distancia > r1 + r2:
    print("Exteriores")
elif distancia == r1 + r2:
    print("Tangentes exteriores")
elif distancia == abs(r1 - r2):
    print("Tangentes interiores")
elif distancia < abs(r1 - r2):
    print("Interiores")
else:
    print("Secantes")