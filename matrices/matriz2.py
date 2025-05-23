#Matriz
matriz = [[10.5, 13.4], [5.56,4.2], [1.5, 0.67], [2.5, 3.5]]
print("-"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6.1f}", end = " ")
    print("|")
    print("-"*17)