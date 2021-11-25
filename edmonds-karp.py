from grafo import Grafo 
from copy import deepcopy
from bfs import camino_mas_corto

grafo = Grafo(True)
grafo.agregar_vertice(0)
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)
grafo.agregar_vertice(5)
grafo.agregar_arista(0,1,11)
grafo.agregar_arista(0,2,12)
grafo.agregar_arista(2,1,2)
grafo.agregar_arista(2,4,11)
grafo.agregar_arista(4,5,4)
grafo.agregar_arista(4,3,10)
grafo.agregar_arista(1,3,12)
grafo.agregar_arista(3,5,19)

def edmonds_karp(grafo, fuente, sumidero):
	flujo = {}
	for v in grafo:
		for w in grafo.adyacentes(v):
			flujo[(v,w)] = 0
	grafo_residual = deepcopy(grafo)
	print(grafo_residual)
	camino = camino_mas_corto(grafo_residual, fuente, sumidero)
	while camino is not None:
		print(camino)
		#print(distancia)
		capacidad_residual = cuello_botella(grafo_residual, camino)
		print("capacidad:{} ".format(capacidad_residual))
		print("\n")
		for i in range(1, len(camino)):
			if camino[i] in grafo_residual.adyacentes(camino[i-1]):
				flujo[(camino[i-1], camino[i])] += capacidad_residual
				actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual)
			else:
				flujo[(camino[i], camino[i-1])] -= capacidad_residual
				actualizar_grafo_residual(grafo_residual, camino[i], camino[i-1], capacidad_residual)
			print(grafo_residual)
			print("\n")
		camino = camino_mas_corto(grafo_residual, fuente, sumidero)
	return flujo

def cuello_botella(grafo, camino):
	peso_min = float("inf")
	for i in range(len(camino)-1):
		peso_actual = grafo.peso_arista(camino[i], camino[i+1])
		if peso_actual < peso_min:
			peso_min = peso_actual

	return peso_min

def actualizar_grafo_residual(grafo, u, v, capacidad_residual):
	peso = grafo.peso_arista(u, v)
	print(u,v)
	if peso == capacidad_residual:
		grafo.borrar_arista(u, v)
	else:
		grafo.cambiar_peso(u, v, peso - capacidad_residual)

	if grafo.estan_unidos(v, u):
		peso_nuevo = grafo.peso_arista(v, u) + capacidad_residual
		grafo.cambiar_peso(v, u, peso_nuevo)
	else:
		grafo.agregar_arista(v, u, capacidad_residual)

print(edmonds_karp(grafo, 0,5))