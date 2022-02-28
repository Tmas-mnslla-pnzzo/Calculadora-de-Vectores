
import math

def modulo_del_vector(T):
    d=[((n**2))for n in T]
    print(f"el modulo del vector {T} es {math.sqrt((sum(d)))}")

def suma_de_vectores(*args):
    c=[]
    for i in zip(*args):
        c.append((sum(i)))
    print(c)
    
def producto_escalar(k, H):
    f=[]
    for i in H:
        w=i*k
        f.append(w)

    print(f)

def producto_punto(Y,O):
    k = [i*j for i,j in zip(Y,O)]
    print(sum(k))

def producto_cruz(G,V):
    K=[]
    K.append(G[1]*V[2]-G[2]*V[1])
    K.append(G[0]*V[2]-G[2]*V[0])
    K.append(G[0]*V[1]-G[1]*V[0])
    print(K)

def convertir_vectores(b):
    i=0
    while i < b:
        i=i+1
        Vi=[int(n) for n in list(input(f"Vector N{i} : "))]
        print(Vi)
        return Vi

def operacion():
    inputs=input("operacion: ")
    if "sumar"==inputs:
        cantidad_vecstores=int(input("Cantidad de vectores: "))
        convertir_vectores(cantidad_vectores)
    elif "escalar"==inputs:
        vector=[int(n) for n in list(input("Vector a escalar: "))]
        k = int(input("magnitud escalar a utilizar: "))
        producto_escalar(k, vector)
    elif "punto"==inputs: 
        cantidad_vectores=int(input("Cantidad de vectores: "))
        producto_punto()

    elif "cruz"==inputs:
        cantidad_vectores=int(input("Cantidad de vectores: "))
        producto_cruz()

    elif "modulo"==inputs:
        modulo_del_vector()

    elif "salir"==inputs:
        print("Saliste")
    elif "ayuda"==inputs:
        print("1) sumar: es una suma entre dos o mas vectores.")
        print("2) escalar: es una multiplicacion entre un vector y un escalar.")
        print("3) punto: es un producto entre dos vectores, como resultado un escalar.")
        print("4) cruz: es un producto entre dos vectores en 3 dimensiones, como resultado otro vector.")
        print("5) modulo: es la magnitud de un determinado vector.")
        print("6) salir: para salir del ejecutable.")
        operacion()  
    else:
        print("selecione una operacion definida")
        operacion()

operacion()