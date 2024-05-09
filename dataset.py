from pandas import read_csv
from graph import Graph


data = read_csv('data/flights2.csv')

#Crea dos listas vacías para almacenar datos de aeropuertos y rutas.
airports = []
routes = []

for i, row in data.iterrows():

  source = {} #Diccionario para los datos de origen del aeropuerto.
  destination = {} #Diccionario para los datos de destino del aeropuerto.

  for item in dict(row):

    if 'Source' in item: source[ item.replace('Source Airport ', '') ] = row[item]
    elif 'Destination' in item: destination[ item.replace('Destination Airport ', '') ] = row[item]

  if not source in airports: airports.append( source ) #Si 'source' no está en 'airports', agrégalo a la lista de aeropuertos.
  if not destination in airports: airports.append( destination ) #Si 'destination' no está en 'airports', agrégalo a la lista de aeropuertos.

  #Crea una tupla 'route' que representa una ruta entre aeropuertos.

  route = (source['Code'],destination['Code'])
  if not ( route in routes or route[::-1] in routes ): routes.append(route)

  #Limita la cantidad de registros procesados a 500 para acelerar la ejecución.
  #if i > 500: break

#Ordena la lista de aeropuertos según el código del aeropuerto.
airports = sorted(airports, key=lambda x: x['Code'])

#Representar el grafo de rutas entre aeropuertos.
globe = Graph()

#Agrega cada aeropuerto como un vértice al grafo.
for airport in airports:
  globe.newVertex( airport )

#Itera sobre las rutas y agrega cada ruta como una arista con su distancia calculada.
for route in routes:
  source = globe.getVertex(route[0])
  destination = globe.getVertex(route[1])
  globe.newEdge( route[0], route[1], globe.distance(route[0], route[1]) )
