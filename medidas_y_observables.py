#observables y medidas
#Julia Mejia
#CNYT 
import math
import numpy as np
import LIBRERIA


#reto de programacion 
#1) probabilidad de una posición en particular
def posicionDeProbab(numPosiciones,v):
    tamaño =  len(v)
    s = 0
    for j in range(tamaño):
        s = s + (LIBRERIA.moduloComp(v[j]))**2
    s = s**(1/2) 
    proba = (LIBRERIA.moduloComp(v[numPosiciones])**2)/s**2
    return  proba

#2) probabilidad de transitar de un vector (v) a (w) 
def probaTransitar(v,w):
    tamaño = len(v) 
    bra = [(0,0)] * tamaño
    for j in range (tamaño):
        bra[j] = LIBRERIA.conjugadoComp(w[j])
    amplitudT = (0,0)
    for i in range(tamaño):
        amplitudT = LIBRERIA.sumaComp(amplitudT , LIBRERIA.multiComp(v[i],bra[i]))
    return amplitudT

#segundo reto de programación
def mediaVarianza(matriz,y):
    tamaño = len(y)

    matrizMedia = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    varianza = (0,0)
    q = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    w = [(0,0)]*tamaño
    bra = [(0,0)] * tamaño
    x = [(0,0)] * tamaño
    for i in range (tamaño):
        x[i] = y[i]
    media = (0,0)
    if LIBRERIA.revisionHermitiana(matriz) == False:
        return "no es hermitanea"
    else:
        w = LIBRERIA.accionMatVector(matriz,y)
        for j in range (tamaño):
            bra[j] = LIBRERIA.conjugadoComp(w[j])
        for i in range(tamaño):
            media = LIBRERIA.sumaComp(media , LIBRERIA.multiComp(bra[i],y[i]))
        matrizMedia = LIBRERIA.escalarMatriz(lE.diagonal(tamaño),media)
        q = LIBRERIA.restamatriz(matriz,matrizMedia)
        q = LIBRERIA.productoMatriz(q,q)
        for i in range (tamaño):
            y[i] = LIBRERIA.conjugadoComp(y[i])
        y = LIBRERIA.accionMatVector(LIBRERIA.transpuestaMatriz(q),y)
        for i in range(tamaño):
            varianza = LIBRERIA.sumaComp(varianza , LIBRERIA.multiComp(y[i],x[i]))
    return varianza


#cuarto reto, estado final 
def estados(m,v,clk):
    for i in range (clk):
        v = LIBRERIA.accionMatVec(m,v)
    return v


#ejercicio 4.3.1
# Encuentre todos los estados posibles del sistema descrito en el Ejercicio 4.2.2

def probabilidad(vector, numero):
    matriz = [[(0,1),(1,0)],
              [(0,-1),(1,0)],
              [(1,0),(1,0)],
              [(-1,0),(1,0)],
              [(0,0),(1,0)],
              [(1,0),(0,0)]]
    resultado = []
    for i in range((num*2)-2,num*2):
        if LIBRERIA.probabilidad(vector, conjunto[i])!=0.0:
            resultado += conjunto[i]
    return resultado

#Realice los mismos cálculos que en el último ejemplo, usando el Ejercicio 4.3.1
#ejercicio 4.3.2
def probabilidad2(a, valor):
    matrices = [[[(1,0),(0,0)],
                 [(0,0),(-1,0)]],
                [[(0,0),(0,-1)],
                 [(0,1),(0,0)]],
                [[(0,0),(1,0)],
                 [(1,0),(0,0)]]]
    arreglo = []
    posible = posibilidad(a,valor)
    arreglo2 = []
    respuesta = 0
    for i in range(3):
        valores = np.linalg.eig(matrices[i])
        arreglo = arreglo + [valores]
    for i in range(len(posible)):
        arreglo2 = arreglo2 + [posible(a, posible[i])]
    for i in range(2):
        respuesta = respuesta + (posible[i]*arreglo[valor][i])
    return respuesta


#verificar si ambas son unitarias y si su producto da una matriz unitaria
# Ejercicio 4.4.1
def comprueba():
    matriz1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    matriz2 = [[(math.sqrt(2)/2,0),(math.sqrt(2)/2,0)],
          [(math.sqrt(2)/2,0),(-math.sqrt(2)/2,0)]]
    a = LIBRERIA.revisionUnitaria(matriz1)
    b = LIBRERIA.revisionUnitaria(matriz2)
    if a == True and b == True:
        r1 = LIBRERIA.productoMatriz(matriz1,matriz2)
        resultante = LIBRERIA.revisionUnitaria(r1)
        return resultante
    else:
        return False

#determine el estado del sistema de billar despues de 3 puntos
#Ejercicio 4.4.2
def billar():
    shot = 3
    matriz =[[(0,0),( 1/ (math.sqrt(2)),0),( 1/ (math.sqrt(2)),0),(0,0)],
             [(0, 1/ (math.sqrt(2))),(0,0),(0,0),( 1/ (math.sqrt(2)),0)],
             [( 1/ (math.sqrt(2)),0),(0,0),(0,0),(0, 1/ (math.sqrt(2)))],
             [(0,0),( 1/ (math.sqrt(2)),0),(-1/ (math.sqrt(2)),0),(0,0)]]
    vector = [(1,0),(0,0),(0,0),(0,0)]
    for i in range(shot):
        resultado1 = LIBRERIA.accionMatVector(matriz,vector)
    probabilidad = (modulo(resultado[3]))**2
    return probabilidad

#4.5.2 determinar si es separable o no

def separable(v,w):
    tamañox = len(v)
    tamañoy = len(w)
    k = 0
    tamañoComp = tamañox * tamañoy
    psi = [(0,0)] * tamañoComp
    for i in range (tamañox):
        for j in range (tamañoy):
            psi[k] = LIBRERIA.productoMatriz(v[i],w[j])
            k =+ 1
    print(psi) #cada casilla representara el valor complejo que compaña a |xi> x|yi>


#4.5.3 determinar si el sistema es separable 
#el vector a entregar es el vector de las constantes C 
def separable(vector):
    c0 = 1
    cx0 = 1
    c1 = 1
    cx1 = 1
    if vector[0] == 0:
        c0 = 0
        cx0 = 0
    if vector[1] == 0:
        c0 = 0
        cx1 = 0
    if vector[2] == 0:
        c1 = 0
        cx0 = 0
    if vector[3] == 0:
        c1 = 0
        cx1 = 0
    if c0 == 1 or cx0 == 1 or c1 == 1 or cx1 == 1:
        print("es separable")
    else:
        print("no es separable")



def main():
    #punto 4.5.3
    v = (0,1,0,1)
    separable(v))
    

