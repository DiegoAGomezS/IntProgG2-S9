palabras = ["Alo", "Hey", "Hello", "Huh", "ExtraHUEVOrdinario"]

busqueda = input("Ingrese la palabra a buscar: ")
if busqueda in palabras:
    print(f"Su palabra {busqueda} esta en la lista")
else:
    print(f"Lo siento su {busqueda} no se encuentra presente")