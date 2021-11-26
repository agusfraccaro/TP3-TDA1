from grafo import Grafo 
from copy import deepcopy
from bfs import camino_mas_corto
from collections import deque

def edmonds_karp(grafo, fuente, sumidero):
	flujo = 0
	grafo_residual = deepcopy(grafo)
	camino = camino_mas_corto(grafo_residual, fuente, sumidero)
	while camino is not None:
		capacidad_residual = cuello_botella(grafo_residual, camino)
		for i in range(1, len(camino)):
			actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual)
		camino = camino_mas_corto(grafo_residual, fuente, sumidero)
		flujo += capacidad_residual

	grupoFuente, grupoSumidero = corte_minimo(grafo_residual, fuente, sumidero)
	return flujo, grupoFuente, grupoSumidero

def cuello_botella(grafo, camino):
	peso_min = float("inf")
	for i in range(len(camino)-1):
		peso_actual = grafo.peso_arista(camino[i], camino[i+1])
		if peso_actual < peso_min:
			peso_min = peso_actual

	return peso_min

def actualizar_grafo_residual(grafo, u, v, capacidad_residual):
	peso = grafo.peso_arista(u, v)
	if peso == capacidad_residual:
		grafo.borrar_arista(u, v)
	else:
		grafo.cambiar_peso(u, v, peso - capacidad_residual)

	if grafo.estan_unidos(v, u):
		peso_nuevo = grafo.peso_arista(v, u) + capacidad_residual
		grafo.cambiar_peso(v, u, peso_nuevo)
	else:
		grafo.agregar_arista(v, u, capacidad_residual)

def corte_minimo(grafo_residual, fuente, sumidero):
	grupoFuente = set()
	grupoSumidero = set()
	grupoFuente.add(fuente)
	cola = deque()
	cola.append(fuente)

	while cola:
		v = cola.popleft()
		for w in grafo_residual.adyacentes(v):
			if w not in grupoFuente:
				grupoFuente.add(w)
				cola.append(w)

	grupoSumidero = set(grafo_residual.obtener_vertices()) - grupoFuente

	return grupoFuente, grupoSumidero
