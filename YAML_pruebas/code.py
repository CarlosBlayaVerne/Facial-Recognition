import yaml
import os
from urllib.request import urlopen

#abrimos el documento prueba.yml
with open('prueba.yml', "r") as file:
    data = yaml.safe_load(file)


#imprimimos los primeros objetos de la lista
print('version', data['version'], '\n')
print('stages: ')
for etapas in data['stages']:
    print(' - ', etapas)

print('\n\nsteps:\n')


#creamos un indice para acumular todos los atributos que pueden haber en los objetos de 'steps'
index_1 = []
index_2 = []
for pasos in data['steps']:

    for atributo in aux[pasos]:
        if atributo in index_2:
            pass
        else:
            index_2.append(atributo)


for pasos in data['steps']:
    print(pasos, ':\n')

    for atributos in index_2:
        #recorremos toda la lista de los posibles valores de atributos y si existen en ese en concreto lo imprimimos
        try:
            if data['steps'][pasos][atributos]:
                print('  -',atributos, ':', data['steps'][pasos][atributos])
        except:
            pass
    print('\n\n')


'''
for pasos in data['steps']:

    print(pasos)

    try:
        if aux[pasos]['title']:
            print(' -title: ', aux[pasos]['title'])
    except:
        pass
    try:
        if aux[pasos]['type']:
            print(' -type: ', aux[pasos]['type'])
    except:
        pass
    try:
        if aux[pasos]['stage']:
            print(' -stage: ', aux[pasos]['stage'])
    except:
        pass
    try:
        if aux[pasos]['description']:
            print(' -description: ', aux[pasos]['description'])
    except:
        pass
    try:
        if aux[pasos]['repo']:
            print(' -repo: ', aux[pasos]['repo'])
    except:
        pass
    try:
        if aux[pasos]['git']:
            print(' -git: ', aux[pasos]['git'])
    except:
        pass
    try:
        if aux[pasos]['revision']:
            print(' -revision: ', aux[pasos]['revision'])
    except:
        pass
    try:
        if aux[pasos]['image_name']:
            print(' -image name: ', aux[pasos]['image_name'])
    except:
        pass
    try:
        if aux[pasos]['dokerfile']:
            print(' -doker file: ', aux[pasos]['dokerfile'])
    except:
        pass
    try:
        if aux[pasos]['candidate']:
            print(' -candidate: ', aux[pasos]['candidate'])
    except:
        pass
    try:
        if aux[pasos]['registry']:
            print(' -registry: ', aux[pasos]['registry'])
    except:
        pass
    try:
        if aux[pasos]['tags']:
            print(' -tags: ', aux[pasos]['tags'])
    except:
        pass
    try:
        if aux[pasos]['enviroment']:
            print(' -enviroment: ', aux[pasos]['enviroment'])
    except:
        pass
    try:
        if aux[pasos]['commands']:
            print(' -commands: ', aux[pasos]['commands'])
    except:
        pass
    print('\n')


print (index_2)
'''