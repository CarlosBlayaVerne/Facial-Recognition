import json
import datetime

with open('search.json', 'r', encoding= "utf-8") as archivo:
    data = json.load(archivo)
    #print("archivo obtenido con exito")

for books in data['response']['docs']:
    print('ID:', books['id'])
    print('Revista:', books['journal'])
    #print('Fecha de publicación: ', books['publication_date'][8:10],'/',books['publication_date'][5:7],'/', books['publication_date'][0:4])
    
    fecha = books['publication_date'][0:10]
    fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    print("Fecha:", fecha.strftime("%d de %b de %Y"))    
    print('Tipo de artículo:', books['article_type'])

    print('Autores:', end=" ")

    aux=0       #auxiliar utilizado para que al seleccionar el ultimo autor cambiemos el patron de print
    for autores in books['author_display']:     #contador de todos los autores del libro seleccionado
        aux=aux+1
        if  aux < len(books['author_display']):
            print(autores, end=", ")
        else:
            print('y ', autores)
    print('Titulo: ', books['title_display'])
    print('Nota: ', round(books['score'],2))
    print('\n')


