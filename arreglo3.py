array_str = ["uno", "dos", "tres", "cuatro", "cinco"]
print("Array de cadenas: ", array_str)

#Insertar un elemento al inicio del arreglo
array_str.insert(3, "cero")
print("Array de cadenas después de insertar 'cero' al inicio", array_str)

#Contar cuantos elementos hay en el arreglo
cantidad = len(array_str)
print("Cantidad de elementos en el arreglo", cantidad)

#Eliminar un elemento del arreglo
array_str.remove("tres")
print("Array de cadenas después de eliminar 'tres': ", array_str)

#Otra forma de eliminar un elemento del arreglo
array_str.pop(2)
print("Array de elementos eliminados: ", array_str)