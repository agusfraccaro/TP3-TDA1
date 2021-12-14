from grafo import Grafo
from bfs import camino_mas_corto
from edmonds_karp import edmonds_karp

def obtener_aristas(grafo):
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.append((v,w))
    return aristas

def definir_trayectos(aeropuertos, grupoFuente, grupoSumidero):
	trayectos = []
	for i in grupoFuente:
		for j in aeropuertos.adyacentes(i):
			if j in grupoSumidero:
				trayectos.append((i,j))
	return trayectos

def pretty_print(trayectos, flujo, fuente, sumidero):
	print(f'La cantidad máxima de pasajeros que pueden ir desde {fuente} a {sumidero} es: {flujo}')
	print('Los trayectos donde poner la publicidad son:')
	for i in trayectos:
		print(f'{i[0]} ---> {i[1]}')

aeropuertos = Grafo(True)
nombre_arch = input("Ingrese el nombre del archivo de vuelos que desea procesar (sin extension): ")
nombre_arch_extension = nombre_arch + ".txt"

with open(nombre_arch_extension, "r") as archivo:
	fuente = archivo.readline().replace("\n", "")
	sumidero = archivo.readline().replace("\n", "")
	for linea in archivo:
		info = linea.replace("\r\n","").split(',')
		aeropuertos.agregar_vertice(info[0])
		aeropuertos.agregar_vertice(info[1])
		aeropuertos.agregar_arista(info[0],info[1],int(info[2]))

aristas = obtener_aristas(aeropuertos)
for arista in aristas:
	peso_nuevo = (aeropuertos.peso_arista(arista[0], arista[1]) * (aeropuertos.total_aristas() + 1) + 1)
	aeropuertos.cambiar_peso(arista[0], arista[1], peso_nuevo)


flujo, grupoFuente, grupoSumidero = edmonds_karp(aeropuertos, fuente, sumidero)
trayectos = definir_trayectos(aeropuertos, grupoFuente, grupoSumidero)
nuevo_flujo = flujo / (aeropuertos.total_aristas() + 1)
pretty_print(trayectos, int(nuevo_flujo), fuente, sumidero)

