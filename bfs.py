from grafo import Grafo
from collections import deque

def camino_mas_corto(grafo, origen, final):
    """Recibe un grafo, un vertice de origen y un vertice final, halla el camino mas corto entre el origen y el final y 
    devuelve una lista con el camino. En caso de no haber un camino devuelve None"""

    padres = bfs_camino_corto(grafo, origen, final)
    recorrido = []

    if padres != None:
        while final is not None:
            recorrido.append(final)
            aux = final
            final = padres[final]
            # peso = grafo.peso_arista(aux, final)
            # if peso:
            #     recorrido.append(peso)
            #     print("recorrido2 {}".format(recorrido))
        print("recorrido {}".format(recorrido))
        print("padres: {}".format(padres))
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
