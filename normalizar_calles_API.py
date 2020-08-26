import requests
import json
import pprint

direccion = input("Ingresa una direccion: ")
localidad = input("Ingresa una localidad: ")


citar = requests.utils.quote(direccion + ',' + localidad) 
#Te lo pasa a Rivadavia%20y%20Donato%20Alvarez%2CCABA
print(citar)
#Le agrego geocodificar=True a la url le agrego un & porque despues va otro parametro

url = 'http://servicios.usig.buenosaires.gob.ar/normalizar/?geocodificar=True&direccion=' + citar 
print(url)

respuesta = json.loads(requests.get(url).text)
pprint.pprint(respuesta)



#for i in respuesta['direccionesNormalizadas']: ERROR PORQUE i NO ES INT
for i in range(len(respuesta['direccionesNormalizadas'])):
    direccion = respuesta['direccionesNormalizadas'][i]['direccion']
    coordenadas_x = respuesta['direccionesNormalizadas'][i]['coordenadas']['x']
    coordenadas_y = respuesta['direccionesNormalizadas'][i]['coordenadas']['y']
    nombre_calle = respuesta['direccionesNormalizadas'][i]['nombre_calle']
    nombre_calle_cruce = respuesta['direccionesNormalizadas'][i]['nombre_calle_cruce']
    nombre_partido = respuesta['direccionesNormalizadas'][i]['nombre_partido'] 
    
print("direccion: ", direccion)
print("coordenadas: ", coordenadas_x + coordenadas_y)
print("nombre de calle: ", nombre_calle)
print("nombre de calle con la que cruza: ", nombre_calle_cruce)
print("nombre del partido: ", nombre_partido)
