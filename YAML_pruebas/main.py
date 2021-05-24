import yaml
import os
from urllib.request import urlopen


with open('lovelace.yml', "r") as file:
    data = yaml.safe_load(file)


print("mode: ", data['mode'])
print("resources: ")

for direcciones in data['resources']:
    print(" - url: ", direcciones['url'])
    print(" - type: ", direcciones['type'])
    print("\n")

'''
r = urlopen(data['resources'][7]['url']) #abrir url
print(r.read())
'''

#r = open(data['resources'][6]['url']) #abrir directorio




'''
cwd = os.getcwd()

print("Current working directory: {0}".format(cwd))
'''