calificacion = []

for i in range(8):
    nota = float(input(f"Ingrese la nota #{i + 1}: "))
    calificacion.append(nota)

promedio = sum(calificacion) / len(calificacion)
print(f"El promedio de las 8 materias es {calificacion} es {promedio:2f}")