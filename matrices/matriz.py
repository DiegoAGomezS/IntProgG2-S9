#Matriz
matriz = [[10, 2], [300,4]]
print("-"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6.1f}", end = " ")
    print("|")
    print("-"*17)