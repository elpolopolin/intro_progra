
def ordenados(s:list[int]) -> bool :
    i = 0
    while i < (len(s)-1) :
        if (s[i] <= s[(i+1)]):
            i += 1
        else : 
         return False
    return ((i+1) == len(s))

#ordenados por profe
def ordenadosClase (lista:list[int]) -> bool:
    elemento = lista[0]
    ordenados = True
    for i in range(len(lista)):
      if(elemento <= lista[i]):
         elemento = lista[i]
      else:
         ordenados = False
    
    return ordenados
    
def columnas_ordenadas (m:list[list[int]]) -> list[bool]:
    listaOrdenados = []
    columna : list[int] = []
    for i in range(len(m[0])):
        for x in range(len(m)):
            columna.append(m[x][i])
        if (ordenados(columna)) :
           listaOrdenados.append(True)
        else:
           listaOrdenados.append(False)
        columna.clear()

    return listaOrdenados


#print(ordenados([0,1,0,3,4]))
#print(ordenadosClase([1,2,2,1,3,4]))

#print(columnas_ordenadas([[1,1,3],
 #                         [2,1,3],
   #                       [3,1,5],[4,4,4]]))
#


#guia 8 comienzo
from queue import LifoQueue as Pila
from queue import Queue as Cola

import random

def generar_numeros_al_azar(incantidad:int,indesde:int,inhasta:int) -> Pila[int] :
   p: Pila[int] = Pila()
   for i in range (incantidad):
    p.put(random.randint(indesde,inhasta))
   return p

def leerPila(p:Pila[int]):
    pilaAlista = []
    listaAlRevesOseaEnOrdenPila = []
    elemento : int = 0
    while not p.empty() :
        elemento = p.get()
        pilaAlista.append(elemento)
    
    for i in range ((len(pilaAlista)-1),-1,-1) :
        listaAlRevesOseaEnOrdenPila.append(pilaAlista[i])
        p.put(pilaAlista[i])
    print("funcion leer pila: ",listaAlRevesOseaEnOrdenPila)
   
   
pila = generar_numeros_al_azar(5,1,5)
print("pila recien generada:", pila.queue)
leerPila(pila)
print("pila luego de leer pila por funcion: ",pila.queue)

def buscar_el_maximo (p:Pila[int]) -> int :
    pilaAlista = []
    elemento : int = 0
    mayor = 0
    while not p.empty() :
        elemento = p.get()
        pilaAlista.append(elemento)

    for i in range ((len(pilaAlista)-1),-1,-1) :
        p.put(pilaAlista[i])
        if (pilaAlista[i]>=mayor) :
           mayor = pilaAlista[i]
    return mayor

def buscarElMaximoPro (p:Pila[int]) -> int:
   elem : int = 0
   mayor = 0
   pilaAux : Pila[int] = Pila()
   while not p.empty() :
      elem = p.get()
      if(mayor < elem):
         mayor = elem
      pilaAux.put(elem)

   while not pilaAux.empty() :
      elem = pilaAux.get()
      p.put(elem)

   return mayor

print("maximo de la pila",buscar_el_maximo(pila))
print("pila :",pila.queue)

print("mayor pro usando solo pilas:", buscarElMaximoPro(pila))
print("pila luego de buscar mayor (queue):", pila.queue)


#bingo solucion profe
c = Cola()

def armaLaSecuenciaDeBingo () -> Cola[int]:
   lista :list[int] = list(range(0,100))
   random.shuffle(lista)
   
   bolillero : Cola[int] = Cola()
   for numero in lista :
      bolillero.put(numero)

   return bolillero

numerosbingo = armaLaSecuenciaDeBingo()
#print(numerosbingo.queue)

#def jugar_carton_de_bingo()