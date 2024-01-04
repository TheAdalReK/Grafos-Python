import json

class Grafo:
    def __init__(self,vertice_x=0,vertice_y=0,arista_x=0,arista_y=0,distancia=0) -> None:
        self.vertice_x = vertice_x
        self.vertice_y = vertice_y
        self.arista_x = arista_x
        self.arista_y = arista_y
        self.distancia = distancia
d = dict()


def agregar(x1,y1,x2,y2,dis):
    key = (x1,y1)
    value = [(x2,y2),dis]
    if key in d:
         d[key].append(value)
    else:
        d[key] = [value]
    key = (x2,y2)
    value = [(x1,y1),dis]
    if key in d:
         d[key].append(value)
    else:
        d[key] = [value]

def get_dicc():
    return d


