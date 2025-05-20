import os
import random
import time

participantes = list()
while True:
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())

os.system("cls||clear")
print("Lista de participantes:")
print(participantes)

cont = 10
while cont > 0:
    os.system("cls||clear")
    print(cont)
    time.sleep(1)

os.system("cls || clear")
fin = len(participantes) - 1
ganador = random.randint(0, fin)
print(f"Ganador {participantes[ganador]}")