#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Triángulo rectángulo")
elif a == b == c:
    print("Triángulo equilátero")
elif a == b or a == c or b == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")