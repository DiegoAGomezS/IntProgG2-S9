precios = [[30, 23, 45], [56, 87.5, 100], [15.7, 90, 67]]
precios_actuales = []

while True:
    try:
        incremento = float(input("Ingrese el aumento en porcentaje que desea darle: "))
        break
    except ValueError:
        print("\n Error. Ingrese un número valido")
        
for fila in precios:
    nueva_fila = []
    for precio in fila:
        nuevo_precio = precio * (1 + (incremento / 100))
        nueva_fila.append(round(nuevo_precio, 2))
    precios_actuales.append(nueva_fila)

print("-"*31)
for fila in precios:
    for columna in fila:
        print(f"|{columna:>8}", end = " ")
    print("|")
    print("-"*31)

print("-"*31)
for fila in precios_actuales:
    for columna in fila:
        print(f"|{columna:>8}", end = " ")
    print("|")
    print("-"*31)