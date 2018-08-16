# -*- coding: utf-8 -*-
def pendiente(metro2,precio,suma1,suma2,suma3,suma4,metro22):

    for i in range(len(metro2)):
        suma1 += (metro2[i] * precio[i])
        suma2 += precio[i]
        suma3 += metro2[i]
        metro_cuadrado_al_cuadrado = metro2[i]**2
        metro22.append(metro_cuadrado_al_cuadrado)
        suma4 += metro22[i]

    suma32=suma3**2
    b = ((len(metro2)*suma1)-(suma2*suma3))/((suma4*len(metro2)-suma32))
    inter = interseccion(suma2,suma3,precio,b)
    print(pronostico(inter,b))
    return b

def interseccion(suma2,suma3,precio,b):
    promedio1 = suma2/len(precio)
    promedio2 = suma3/len(precio)
    return promedio1-(b*promedio2)

def pronostico(inter,b):
    return inter+(b*157)

if __name__ == '__main__':
    metro2 = [5,15,20,25]
    precio = [375,487,450,500]
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    metro22 = []
    b = pendiente(metro2,precio,suma1,suma2,suma3,suma4,metro22)
    print(b)
