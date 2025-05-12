
import math
from math import sqrt, pi, ceil 

#function decirHola 
def imprimirHolamundo():    
    print("aloha mundo")


#imprimirHolamundo()
#raiz de 3
print("raiz cuadrada de 3:", sqrt(3)) #si importara de math llamaria a sqrt como math.sqrt

#imprimimos el valor de pi
print("numero pi:",pi)

#imprimimos el techo de un flotante
print("techo de 8,23:",ceil(8.323))

def perimetro() -> float : #perimetro de radio 1 = radio * 2 * pi
    res: float = 1*2* math.pi
    return res

print("Perimetro de circunferencia radio 1:", perimetro())

#2
def esmultiploDe (x:int, y:int) ->bool:
    if (x % y == 0) :
        return True
    else :
        return False 
    
def esmultiplodePrint (x,y):
    if esmultiploDe(x,y) :
        print (y, "es multiplo de", x," TRUE")
    else :
        print(y,"no es multiplo de ", x, "FALSE")

esmultiplodePrint (20.2,10.1)

#3.3
def es_nombre_largo (nombre:str) -> bool:
    return 3 <= len(nombre) and len(nombre) <= 8

print(es_nombre_largo("Jhon"))

#5.1
def devolver_el_doble_si_par (n:int) -> int:
    res : int
    if (n % 2 == 0):
        res = n *2
    else :
        res = n
    return res

print("Devolver el doble si es par de 12:",devolver_el_doble_si_par(12))

#6.2 while
def numPares10y40 ():
    i = 10
    while i <= 40 :
        if(i%2 == 0):
            print(i)
        i = i + 1

#numPares10y40()

#6.3
def cuentaRegresiva (x:int):
    while x>=1 :
        print(x)
        x= x-1
    print("Despegue!")

#cuentaRegresiva(10)

#7 implementar las funciones del 6 utilizando: for num in range(i,f,p)

def numpares10y40_2 ():
    for num in range (10,41,1) :
         if(num%2 == 0):
            print(num)

#numpares10y40_2()

def cuentaRegresiva_2 (x:int) : 
    for num in range(x,0,-1) :
        print(num)
    print("Despegue! con inrange")
cuentaRegresiva_2(20)