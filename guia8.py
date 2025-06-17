"""
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

"""
#guia 8 comienzo
from queue import LifoQueue as Pila
from queue import Queue as Cola
import unittest

import random
"""
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

#print("maximo de la pila",buscar_el_maximo(pila))
#print("pila :",pila.queue)

#print("mayor pro usando solo pilas:", buscarElMaximoPro(pila))
#print("pila luego de buscar mayor (queue):", pila.queue)


def buscar_nota_maxima (p:Pila[(str,int)]):
    pila_aux = p
    #print(pila_aux.queue)
    elemNotaMayor = pila_aux.get()
    while not pila_aux.empty() :
        elem = pila_aux.get()
        if(elem[1]>elemNotaMayor[1]):
            elemNotaMayor = elem
    return elemNotaMayor

p = Pila()
p.put(("tomas",1))
p.put(("robert",1))
p.put(("indones",2))
print(buscar_nota_maxima(p))

#1.6
def evaluar_expresion(s:str) ->float:
    pila = Pila()
    i = 0
    while i < len(s):
        if (s[i] == ' '):
            i+=1
        elif(s[i] in ['+','-','*','/']):
            b = pila.get() #desapilo el segundo numero
            a = pila.get() #desapilo el 1er numero
            if s[i] == '+':
                pila.put(a + b)
            elif s[i] == '-':
                pila.put(a - b)
            elif s[i] == '*':
                pila.put(a * b)
            elif s[i] == '/':
                pila.put(a / b)
            i += 1
        else:
            num_str = '' 
            while i<len(s) and s[i] != ' ':
                num_str += s[i]
                i+=1
            pila.put(float(num_str))
    return pila.get()

print(evaluar_expresion("3 4 + 5 * 2 -"))
            

def mostrar_pila(p: Pila) -> any : #Este Any es porque la pila puede tener cualquier input (str,int,float,etc)
    pila_aux: Pila = Pila() #Creo mi pila auxiliar

    #Quito y muestro los elementos de mi pila
    while not p.empty(): 
        elemento = p.get()
        pila_aux.put(elemento)
        print("La pila tiene:", elemento)

    #Reconstruyo mi pila original
    while not pila_aux.empty():
        p.put(pila_aux.get())


def darvueltaPila(p:Pila[any]):
    pilaInversa : Pila[int] = Pila()
    inverso = []
    while not p.empty():
        inverso.append(p.get())

    for i in range(len(inverso)-1,-1,-1): #vuelve a poner la pila
        pila.put(inverso[i])

    for x in range(len(inverso)):
        pilaInversa.put(inverso[x])
    return pilaInversa

def intercalar(p1:Pila, p2:Pila) -> Pila:
    pila1Inversa = darvueltaPila(p1)
    pila2Inversa = darvueltaPila(p2)
    pila_intercalada : Pila[any] = Pila()
    while not pila1Inversa.empty():
        elem1 = pila1Inversa.get()
        elem2 = pila2Inversa.get()
        pila_intercalada.put(elem1)
        pila_intercalada.put(elem2)
    return pila_intercalada


pila1 = Pila()
pila1.put(1) 
pila1.put(2) 
pila1.put(3)
pila2 = Pila()
pila2.put('a') 
pila2.put('b')
pila2.put('c')
#mostrar_pila(pila2)
#pila1Inversa = darvueltaPila(pila1)
#mostrar_pila(pila1Inversa)
#intercalada = intercalar(pila2,pila1)
#mostrar_pila(intercalada)
#print(intercalada.queue)




#print(numerosbingo.queue)

#def jugar_carton_de_bingo()

#colas

def mostrar_cola(c: Cola) -> any : #Este Any es porque la cola puede tener cualquier input (str,int,float,etc)
    cola_aux: Cola = Cola() #Creo mi cola auxiliar
    #Quito y muestro los elementos de mi cola
    while not c.empty(): 
        elemento = c.get()
        cola_aux.put(elemento)
        print("La cola tiene:", elemento)

    #Reconstruyo mi cola original
    while not cola_aux.empty():
        c.put(cola_aux.get())

def generar_nros_al_azar_cola(cantidad:int,desde:int,hasta:int):
    colaNumerosAlAzar = Cola()
    for i in range(cantidad):
        colaNumerosAlAzar.put(random.randint(desde,hasta))
    return colaNumerosAlAzar


#numerosAlazarCola = generar_nros_al_azar_cola(3,1,10)
#print(numerosAlazarCola.queue)


def cantidad_elementos_cola (c:Cola[any]) -> int:
    cola_aux = Cola()
    cantElem = 0
    while not c.empty() :
        cola_aux.put(c.get())
        cantElem += 1
    while not cola_aux.empty() :
        c.put(cola_aux.get())
    return cantElem 

def buscar_el_maximo(c:Cola[int]) -> int:
    cola_aux = Cola()
    max = c.get()
    cola_aux.put(max)
    while not c.empty():
        elem = c.get()
        cola_aux.put(elem)
        if (elem > max) :
            max = elem
    while not cola_aux.empty() :
        c.put(cola_aux.get())
    return max

cola = Cola()
cola.put(1)
cola.put(2)
cola.put(10)
print(cola.queue)
mostrar_cola(cola)
print(cantidad_elementos_cola(cola))
print(cola.queue)

print(buscar_el_maximo(cola))
mostrar_cola(cola)
print(cola.queue)


#bingo solucion profe
c = Cola()

def armaLaSecuenciaDeBingo () -> Cola[int]:
   lista :list[int] = list(range(0,100))
   random.shuffle(lista)
   #print(lista)
   bolillero : Cola[int] = Cola()
   for numero in lista :
      bolillero.put(numero)

   return bolillero

def armaCarton() -> Cola[int]:
    lista :list[int] = list(range(0,100))
    random.shuffle(lista)
    carton : list[int] = []
    for i in range(12) :
        carton.append(lista[i])
    return carton

def jugar_carton(carton,numerosbingo) -> int:
    intentos = 0
    #cartonaux = carton.copy()
    numerosBingoAux = Cola()
    salidos =0
    while salidos != len(carton) :
        numerobingo = numerosbingo.get()
        numerosBingoAux.put(numerobingo)
        #print("numeros carton:",carton," numero bolillero:",numerobingo)
        for i in range(len(carton)):
            if (numerobingo == carton[i]):
                salidos+=1
        intentos+=1
        #print("intentos:",intentos)
    while not numerosbingo.empty():
        numerobingo = numerosbingo.get()
        numerosBingoAux.put(numerobingo)

    while not numerosBingoAux.empty() : #vuelvo a poner la lista y los numeros en su lugar
        numerosbingo.put(numerosBingoAux.get())

    return intentos

numerosbingo :Cola[int] = armaLaSecuenciaDeBingo()
numerosCarton :list[int] = armaCarton()
print(numerosCarton)
print(numerosbingo.queue)
print("intentos: ",jugar_carton(numerosCarton,numerosbingo))
print(numerosbingo.queue)
print(numerosCarton)
#print(numerosbingo.queue)


#cola hospital
#problema pacientes urgentes (in c:Cola[Z× seq⟨Char⟩ × seq⟨Char⟩]) : Z {
pacientes = Cola()
pacientes.put((9,"tomas","pediatria"))
pacientes.put((8,"jose","odontologia"))

def pacientes_urgentes(c:Cola[tuple[(int,str,str)]]) -> int:
    cola_aux = Cola()
    pacientesUrgencias = 0
    while not c.empty():
        paciente = c.get()
        if (paciente[0] < 4):
            pacientesUrgencias +=1
        cola_aux.put(paciente)
    while not cola_aux.empty():
        c.put(cola_aux.get())
    return pacientesUrgencias

print(pacientes.queue)
#print(pacientes_urgentes(pacientes))
#print(pacientes.queue)


#diccionarios
# calcular promedio por estudiante 

def calcular_promedio_por_estudiante (notas:list[tuple[(str,float)]]) -> dict[str,float] :
    promediosxEstudiante :dict[str,float] = {}
    estudiantesSacados = []
    for i in range(len(notas)):
        if(not notas[i][0] in estudiantesSacados):
            estudiante = notas[i][0]
            estudiantesSacados.append(notas[i][0]) #agrego al estudiante el cual ya se le evaluo sus notas
            print(estudiante)
            suma = 0.0
            cantidad = 0
            for x in range(len(notas)) : 
                if (estudiante == notas[x][0]):
                    suma += notas[x][1]
                    cantidad +=1
            promediosxEstudiante[estudiante] = suma/cantidad
            #print("notas del estudiante ", estudiante," ",suma,"promedio:",suma/cantidad)
    return(promediosxEstudiante)

#estudiantes = [("tomas",10),("roberto",9),("tomas",5),("jose ignacio",10),("manuel galanti",4),("manuel galanti",10),("manuel galanti",6),("tomas",5)]
#print(calcular_promedio_por_estudiante(estudiantes))

#problema visitar sitio (inout historiales: Diccionario⟨seq⟨Char⟩, P ila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩)

def visitar_sitio (historial:dict[str,Pila[str] ], usuario:str, sitio:str) :
    if (sitio and usuario in historial) :
        historial[usuario].put(sitio)

def navegar_atras (historial:dict[str,Pila[str]], usuario:str) -> str:
    if (usuario in historial):
        sitioAnterior:str = historial[usuario].get()
        return sitioAnterior
    else:
        return("usuario no encontrado")

print("Historiales:")
paginasAbiertas :Pila[str] = Pila()
historialTomas = Pila()
historialTomas.put("porno")
historialTomas.put("hentai")
historial :dict[str,paginasAbiertas] = {}
historial["tomas"] = historialTomas
historial["javier"] = Pila()
print(historial)
print(historial["javier"].queue)
visitar_sitio(historial,"javier","droga")
print(historial)
print(historial["javier"].queue)

print(navegar_atras(historial,"tomas"))
"""

#problema agregar producto (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
#in precio: R, in cantidad: Z) {


def agregarProducto(inventario:dict[str,dict[str, float | int ]], nombreNuevo:str, precioNuevo:float, cantidadNueva:int):
    if (not nombreNuevo in inventario):
        print("agregando producto", nombreNuevo)
        inventario[nombreNuevo] = {"precio":precioNuevo,"cantidad":cantidadNueva}
    elif(nombreNuevo in inventario):
        print("actualizando",nombreNuevo,"con anterior precio", inventario[nombreNuevo]["precio"], "y cantidad ",inventario[nombreNuevo]["cantidad"], " a ",precioNuevo,cantidadNueva )
        inventario[nombreNuevo] = {"precio":precioNuevo,"cantidad":cantidadNueva}
    elif(not precioNuevo or not cantidadNueva):
        print("faltan datos")

        
def calcular_valor_inventario (inventario):
    suma = 0
    for producto in inventario:
        suma += (inventario[producto]["precio"] * inventario[producto]["cantidad"] )
    return suma

inventario :dict[str,dict[str, float | int ]] = {}
inventario = {
    "remera": {
        "precio": 999.99,
        "cantidad": 3
    },
    "pantalón": {
        "precio": 1499.00,
        "cantidad": 5
    }
}
print(inventario)
agregarProducto(inventario,"remera",10,10)
agregarProducto(inventario,"camara",100,20)
print(inventario)
print("valor inventario:", calcular_valor_inventario(inventario))


#archivos:
#: open, close, read, readline, readlines, write, os.path.join(), os.path.exists(). salto= /n

def contar_lineas(nombreArchivo:str) -> int:
    File_object = open(nombreArchivo, 'r')
    lineas = File_object.readlines()
    print("lineas:",lineas)
    File_object.close()
    return len(lineas)

def existe_palabra (nombreArchivo:str, palabra:str) -> bool :
    File_object = open(nombreArchivo, 'r')
    text = File_object.read()
    palabraEntexto = ''
    #print(text)
    for i in range (len(text)) :
        if (text[i] not in [' ', '\n', '\t']):
            palabraEntexto += text[i]
        else:
            #print(palabraEntexto)
            if (palabraEntexto == palabra):
                return True
            palabraEntexto = ''

        if (palabraEntexto == palabra): #verifica ultima palabra sin separador
            return True
    return False

#cantidad de_apariciones
    
print(contar_lineas("archivo.txt"))
print(existe_palabra("archivo.txt","polonsky"))

def cantidadDeVecesPalabra (nombreArchivo:str, palabra:str) -> bool :
    File_object = open(nombreArchivo, 'r')
    text = File_object.read()
    palabraExtraida = ''
    contador = 0
    for i in range(len(text)) :
        if (text[i] not in [' ', '\n', '\t']):
            palabraExtraida += text[i]
        else:
            if(palabraExtraida == palabra):
                contador +=1
            palabraExtraida = ''
    if(palabraExtraida == palabra):
        contador +=1
        
        
    return contador

print(cantidadDeVecesPalabra("archivo.txt", "mini"))

def agrupar_por_long (nombre_archivo:str) -> dict[int,int] :
    File_object = open(nombre_archivo, 'r')
    text = File_object.read()
    File_object.close()
    contador = 0
    res :dict[int,int] = {}

    for i in range(len(text)) :
        if (text[i] not in [' ', '\n', '\t']):
            contador +=1
        else:
            if (contador in res):
                res[contador] += 1
            else:
                res[contador] = 1
            contador = 0
    if (contador > 0):
        if (contador in res):
            res[contador] += 1
        else:
            res[contador] = 1

    return res

def palabraMas (nombre_archivo:str) -> str :
    File_object = open(nombre_archivo, 'r')
    text = File_object.read()
    File_object.close()
    palabras = {}
    textoExtraido = ""
    mayor= 0
    masFrecuente = "nada"
    for i in range(len(text)) :
        if (text[i] not in [' ', '\n', '\t', ',','.']):
            textoExtraido += text[i].lower()
        elif textoExtraido != "": #palabra despues de varios espacios sera ""
            if (not textoExtraido in palabras) :
                palabras[textoExtraido] = 1
            else:
                palabras[textoExtraido] += 1
            if (palabras[textoExtraido] > mayor) :
                mayor = palabras[textoExtraido]
                masFrecuente = textoExtraido 
            textoExtraido = ''
    if (textoExtraido != ""):
        if (not textoExtraido in palabras) : #verificamos ultima palabra q puede haber quedado ya que no hubo salto de linea ni espacio q haga q cambie textoExtraido
            palabras[textoExtraido] = 1
        else:
            palabras[textoExtraido] += 1
        if (palabras[textoExtraido] > mayor) :
            mayor = palabras[textoExtraido]
            masFrecuente = textoExtraido 
    #print(masFrecuente)
    return masFrecuente


print(agrupar_por_long("archivo.txt"))
print(palabraMas("archivo.txt"))