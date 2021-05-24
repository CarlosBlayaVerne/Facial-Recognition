import yaml
import os
from urllib.request import urlopen


with open('prueba.yml', "r") as file:
    data = yaml.safe_load(file)


#for pasos in data['steps']:
#    print (pasos, '\n')


aux=data['steps']


print('version', data['version'], '\n')
print('stages: ')
for etapas in data['stages']:
    print(' - ', etapas)

print('\n\nsteps:\n')



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

