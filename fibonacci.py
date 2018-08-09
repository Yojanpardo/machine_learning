# -*- coding: utf-8 -*-

def fibonacci(n):
    anterior = 0
    actual = 1
    serie = [0,1]
    for i in range(n):
        suma = anterior+actual
        anterior = actual
        actual = suma
        serie.append(actual)
    return serie

if __name__=='__main__':
    n=int(input('cuántos números de la serie de fibonacci quieres contar?'))
    print(fibonacci(n))
