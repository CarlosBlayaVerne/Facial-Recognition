import json

print("hola")


with open('search.json', 'r') as archivo:
    busquedas = json.load(archivo)
    print("archivo obtenido con exito")

