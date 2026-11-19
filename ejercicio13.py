#

dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if mes == 2:
    max_dias = 28
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        max_dias = 29
elif mes in [4, 6, 9, 11]:
    max_dias = 30
else:
    max_dias = 31

if 1 <= mes <= 12 and 1 <= dia <= max_dias:
    print("Fecha correcta")
else:
    print("Fecha incorrecta")