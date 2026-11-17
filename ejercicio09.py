a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

numeros = [a, b, c]
numeros.sort(reverse=True)

print(numeros)