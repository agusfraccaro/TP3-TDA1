from grafo import Grafo
from collections import deque

def camino_mas_corto(grafo, origen, final):
    padres = bfs_camino_corto(grafo, origen, final)
    recorrido = []

    if padres != None:
        while final is not None:
            recorrido.append(final)
            aux = final
            final = padres[final]
        return recorrido[::-1]
    return padres

def bfs_camino_corto(grafo, origen, final):
    visitados = set()
    padres = {}
    cola = deque()              
    cola.append(origen)
    visitados.add(origen)
    padres[origen] = None

    while cola:
        v = cola.popleft()
        if v == final: return padres
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.append(w)
                padres[w] = v
    return None
