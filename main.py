from grafo import Grafo
from bfs import camino_mas_corto

aeropuertos = Grafo(True)
with open("vuelos.txt", "r") as archivo:
	fuente = archivo.readline()
	sumidero = archivo.readline()
	for linea in archivo:
		info = linea.replace("\r\n","").split(',')
		aeropuertos.agregar_vertice(info[0])
		aeropuertos.agregar_vertice(info[1])
		aeropuertos.agregar_arista(info[0],info[1],int(info[2]))

