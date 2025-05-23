#Matriz
matriz = [["Luis", "Nicolas", "Andres"], ["Diego", "Oscar", "Gabriel"], ["Jose", "Alex", "Pedro"]]
matriz_2 = []

for fila in matriz:
    nueva_fila = []
    for columna in fila:
        letras = len(columna)
        nueva_fila.append(letras)
    matriz_2.append(nueva_fila)

print("-"*31)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>8}", end = " ")
    print("|")
    print("-"*31)

print("-"*31)
for fila in matriz_2:
    for columna in fila:
        print(f"|{columna:>8}", end = " ")
    print("|")
    print("-"*31)