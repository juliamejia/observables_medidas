
#Libreria computacion cuantica
#Julia Mejia
#CNYT


import math

#1. suma de numeros complejos 
def sumaComp (a,b):
    real = a[0] + b[0]
    real = round(real,2)
    img = a[1] + b[1]
    img = round(img,2)
    return (real,img)

#2. multiplicacion de numeros complejos
def multiComp(a,b):
    real = (a[0]*b[0]) - (a[1]*b[1])
    real = round(real,2)
    img = (a[0]*b[1]) + (a[1]*b[0])
    img = round(img,2)
    return (real,img)

#3. resta de numeros complejos 
def restaComp (a,b):
    real = a[0]-b[0]
    real  =round(real,2)
    img = a[1]-b[1]
    img = round(img,2)
    return (real,img)


#4. division de numeros complejos 
def divisionComp(a,b):
    numerador1 = a[0] * b[0] + a[1] * b[1]
    denominador1 = b[0]**2 + b[1]**2
    numerador2 = a[1] * b[0] - a[0] * b[1]
    divisor1 = numerador1 / denominador1
    divisor1 = round(divisor1, 2)
    divisor2 = numerador2 / denominador1
    divisor2 = round(divisor2, 2)
    return(divisor1,divisor2)

#5. modulo de numeros complejos
def moduloComp (complejo):
    raiz = math.sqrt(complejo[0]**2 + complejo[1]**2)
    raiz = round(raiz, 2)
    return (raiz,0)

#6. conjugado de un numero complejo 
def conjugadoComp(complejo):
    return complejo[0] , complejo[1]*-1


#7. conversion de complejo a polar 
def polarComp(complejo):
    r = math.sqrt(complejo[0]**2 + complejo[1]**2)
    r = round(r, 2)
    angulo = math.atan2(complejo[1],complejo[0])
    angulo = round(angulo, 2)
    return (r,angulo)

#8. fase de un numero complejo 
def faseComp(complejo):
    angulo = math.atan2(complejo[1],complejo[0])
    angulo = round(angulo, 2)
    return (angulo)

#------------------------------ SEGUNDA PARTE-----------------------------------
#9. suma de vectores
def sumVectores(a,b):
    matriz =[]
    m = len(a)
    for i in range (m):
        sum1 = sumaComp(a[i],b[i])
        matriz = matriz + [sum1]
    return matriz


#10. inverso aditivo de un numero complejo
def inversoVector(complejo):
    inversa = []
    a = (-1,0)
    for i in range (len(complejo)):
        mult1 = multiComp(complejo[i],a)
    inversa = inversa + [mult1]
    return inversa

#11. multiplicacion de un escalar por un vector complejo
def multiEscalar (c,d):
    matriz = []
    i =0
    for i in range (len(c)):
        matriz = matriz + [multiComp(c[i],d)]
    return matriz

#12. adicion de matrices complejas
def sumaMatriz(a,b):
    n,m = len(a),len(b)
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = sumaComp(a[i][j],b[i][j])
    return c

# resta de matrices complejas
def restaMatriz(a,b):
    n,m = len(a),len(b)
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = restaComp(a[i][j],b[i][j])
    return c

#13. inversa de una matriz compleja
def inversaMatriz(mCompleja):
    n,m = len(mCompleja),len(mCompleja[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = multiComp(mCompleja[i][j],(-1,0))
    return c

#14. multiplicacion de un escalar por una matriz compleja
def escalarmatriz(matriz,num):
    n,m = len(matriz), len(matriz[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = multiComp(matriz[i][j], num)
    return c


#15. transpuesta de una matriz
def transpuestaMatriz(a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[j][i]
    return c

#16. conjugada de una matriz
def conjugadaMatriz (z):
    n,m = len(z),len(z[0])
    i = 0
    j = 0
    c = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = conjugadoComp(z[i][j])
    return c

#17. adjunta de una matriz
def adjuntaMatriz(matriz):
    adjunta = conjugadaMatriz(transpuestaMatriz(matriz))
    return adjunta

#18. producto de dos matrices (de tamaños compatibles)
def productoMatriz(a,b):
    n,m = len(a),len(a[0])
    d,f = len(b),len(b[0])
    c = transpuestaMatriz(b)
    matriz = []
    acumulador = []
    cont = 0
    c = [[(0,0) for j in range(m)]for i in range(n)]
    if m == d:
        for k in range(f):
            for i in range(n):
                for j in range(m):
                    p = multiComp(a[k][j], b[i][j])
                    matriz = matriz + [p]
            for i in range(n):
                for j in range(m):
                    while cont <= len(matriz)-1:
                        acumulador = acumulador + [sumaComp(matriz[cont],matriz[cont+1])]
                        cont = cont + 2
    return matriz

#19. calcular la accion de una matriz sobre un vector
def accionMatVector(a,b):
    m,n = len(a), len(a[0])
    prob1 = len(b)
    arreglo = []
    if prob1 == n:
        matinicial = (0,0)
        for i in range(m):
            for j in range(len(a[i])):
                resultado = multiComp(a[i][j],b[j])
                matinicial = sumaComp(resultado,matinicial)
            arreglo = arreglo + [matinicial]
            matinicial = (0,0)
    return arreglo

   


#20. producto interno de dos vectores
def interno(a,b):
    vector = (0,0)
    m,n = len(a),len(b)
    for i in range(m):
        resp1 = conjugadoComp(a[i])
        respuesta2 = multiComp(resp1,b[i])
        respuesta = sumaComp(vector,respuesta2)
    return respuesta

#21. norma de un vector
def norma(a):
    e = interno(a,a)
    c = (e[0]) ** (1/2)
    c = round(c,2)
    return c

#22. distancia entre dos vectores
def distancia(d,e):
    b = inversoVector(e)
    c = sumVectores(d,e)
    h = interno(c,c)
    respuesta = (h[0] ** (1/2))
    respuesta = round(respuesta,2)
    return respuesta

#23. revisar si una matriz es unitaria
def revisionUnitaria(a):
    respuesta = False
    b = adjuntaMatriz(a)
    c = productoMatriz(a,b)
    if a == c:
        respuesta = True
        print(respuesta)
        return respuesta
    else:
        respuesta = False
        print(respuesta)
        return respuesta
    
#24. revisar si una matriz es hermitiana
def revisionHermitiana(a):
    respuesta = False
    b = adjuntaMatriz(a)
    if b == a:
        respuesta = True
        print(respuesta)
        return respuesta
    else:
        respuesta = False
        return respuesta
    
#25. producto tensor de dos matrices
def tensor(a,b):
    arreglo = []
    posi = 0
    posj = 0
    while posi < (len(a)-1)*2:
        fila1 = a[posi]
        fila2 = b[posj]
        fila3 = []
        for i in fila1:
            for j in fila2:
                fila3 = fila3 + [multiComp(i,j)]
        posj = posj + 1
        fila2 = b[posj]
        arreglo.append(fila3)
        fila = []
        for i in fila1:
            for j in fila2:
                fila.append(multiComp(i,j))
        posi = posi + 1
        posj = posj - 1
        arreglo.append(fila)
    return arreglo

def probabilidad(vector, posicion):
    numero1 = moduloCom(vector[posicion])
    numero2 = norma(vector)
    respuesta = (numero1**2)/(numero2**2)
    round (respuesta,2)
    return respuesta 
    


    



def main():
    a = (2,13)
    b = (34,56)
    #prueba 1
    print(sumaComp(a,b))
    #prueba 2
    print(restaComp(a,b))
    #prueba 3
    print(multiComp(a,b))
    #prueba 4
    print (divisionComp(a,b))
    #prueba 5
    print(moduloComp(b))
    #prueba 6
    print(conjugadoComp(b))
    #prueba 7
    print (polarComp(b))
    #prueba 8
    print(faseComp(b))
    vector1 = [(5,6),(4,2)]
    vector2 = [(3,7),(4,6)]
    #prueba 9
    print (sumVectores(vector1,vector2))
    #prueba 10
    print (inversoVector(vector2))
    matriz1 =  [(8,0),(3,2)], [(3,5),(6,6)]
    matriz2 = [(13,4),(23,2)], [(3,7),(1,0)]
    num = (3,0)
    #prueba 11
    print (multiEscalar(vector1,num))
    #prueba 12
    print(sumaMatriz(matriz1,matriz2))
    #prueba 13
    print(inversaMatriz(matriz1))
    #prueba 14
    print(escalarmatriz(matriz1,num))
    #prueba 15
    print(transpuestaMatriz(matriz2))
    #prueba 16
    print(conjugadaMatriz(matriz2))
    #prueba 17
    print(adjuntaMatriz(matriz1))
    #prueba 18
    print(productoMatriz(matriz1,matriz2))
    #prueba 19
    print(accionMatVector(matriz1,vector1))
    #prueba 20
    print(interno(vector1,vector2))
    #prueba 21
    print(norma(vector1))
    #prueba 22
    print(distancia(vector1,vector2))
    #prueba 23
    print(revisionUnitaria(matriz1))
    #prueba 24
    print(revisionHermitiana(matriz2))
    #prueba 25
    print(tensor(matriz1,matriz2))
    A = [(1,1),(1,0)]
    B = [(1,0),(0,1)]


