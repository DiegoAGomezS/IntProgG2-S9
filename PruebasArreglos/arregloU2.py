arreglo_init = []

for i in range(10):
    num = int(input("Ingrese un número a sumar: "))
    arreglo_init.append(num)
    print(i)

print(f"ArregloEntero: {sum(arreglo_init)}")