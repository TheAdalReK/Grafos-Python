import math

def distancia_euclidiana(x_1,y_1,x_2,y_2):
    return math.sqrt((x_2-x_1)**2+(y_2-y_1)**2)

def puntos_mas_cercanos(puntos_list)-> list:
    resultado = []
    for punto_i in puntos_list:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 1000
        cercano = (0,0)
        for punto_j in puntos_list:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distancia_euclidiana(x1,y1,x2,y2)
                if d < min:
                    min = d
                    cercano = (x2,y2)

        resultado.append((punto_i,cercano))
    return resultado
