#Arreglos de tipo entero
array_init = [5, 4, 9, 2, 1]
print("Array de enteros: ", array_init)

#Ordenar el arreglo de menor a mayor
array_init.sort()
print("Array de enteros ordenado: ")

#Ordenar el arreglo de mayor a menor
array_init.sort(reverse = True)
print("Array de enteros ordenados de Mayor a Menor: ", array_init)

#Buscar un elemento en el arreglo
elemento = 4
if elemento in array_init:
    print(f"El elemento {elemento} se encuentra en el arreglo.")
else:
    print(f"El elemento {elemento} no se encuentra en el arreglo")

#Insertar un elemento en el arreglo
array_init.append(6)
print("Array de enteros después de insertar 6: ", array_init)