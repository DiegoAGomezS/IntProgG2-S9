numeros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("Números en orden inverso:")
for numero in reversed(numeros):
    print(numero)
