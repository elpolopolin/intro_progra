# Clase 21 de mayo labo 1106. No es autocontenido, las explicaciones se dieron en clase. Cualquier consulta los esperamos la clase que viene.
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
import unittest


def pila_a_lista(p: Pila) -> list[int]:
    res: list[int] = []
    while not p.empty():
        res.append(p.get())
    for i in range(len(res)-1,-1,-1):
        p.put(res[i])
    return res

def generar_nros_al_azar_pila(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    while cantidad > 0:
        res.put(random.randint(desde, hasta))
        cantidad = cantidad - 1
    return res  



def cantidad_elementos(p:Pila[int])->int:
    pila_aux = Pila()
    cantidad = 0
    while not p.empty():
        pila_aux.put(p.get())
        cantidad += 1
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return cantidad

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





def problema_buscar_nota_maxima(p:Pila[(str,int)]):
    lista_pila = pila_a_lista(p)
    maximo = lista_pila[0][1]
    pos = 0
    for i in range (1,len(lista_pila)):
        elemento = lista_pila[i][1]
        if elemento > maximo:
            maximo = elemento
            pos = i
    return lista_pila[pos]


def buscar_nota_maxima(p:Pila[tuple[str,int]]) -> tuple[str,int]:
    pila_aux: Pila = Pila()
    tupla_inicio: tuple[str,int] = p.get()#Aca estoy obteniendo el primer elemento de mi pila
    alumno: str = tupla_inicio[0]  #de mi primer elemento obtengo el nombre del alumno
    nota_maxima: int = tupla_inicio[1] #de mi primer elemento obtengo la nota del alumno    
    pila_aux.put((alumno,nota_maxima)) 
    
    while not p.empty():
        tupla = p.get()
        if nota_maxima < tupla[1]:
            alumno = tupla[0]
            nota_maxima = tupla[1]
        pila_aux.put(tupla)

    #Reconstruyo la pila
    while not pila_aux.empty():
        p.put(pila_aux.get())
    
    return (alumno,nota_maxima)    

pila = Pila()

buscar_nota_maxima(pila)

def esta_bien_balanceada(s: str) -> bool:
    pila = Pila()  # Creamos la pila vacía

    for caracter in s:         # Recorremos cada caracter de la cadena
        if caracter == '(':     # Si el caracter es un paréntesis de apertura
            pila.put(caracter)  # Lo agregamos a la pila
        elif caracter == ')':   # Si es un paréntesis de cierre
            if pila.empty():  # Si no hay nada en la pila, no hay '(' que cierre
                return False
            pila.get()  # Sacamos un '(' de la pila, porque este ')' lo cierra

    return pila.empty()  # Si la pila quedó vacía, los paréntesis estaban balanceados

from queue import LifoQueue as Pila

def evaluar_expresion(s: str) -> float:
    pila = Pila()
    i = 0 #contador para no pasarme en la longitud
    while i < len(s):
        if s[i] == ' ':
            i += 1
        elif s[i] in ['+', '-', '*', '/'] and (i+1 == len(s) or s[i+1] == ' '): #me fijo que sea un operador, lo es si pertence a esa lista y si lo que le sigue es un espacio en blanco o el fin de la expr
            # operador
            b = pila.get() #desapilo el 2do elemento
            a = pila.get() # desapilo el 1er elemento
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
            # Leer número (positivo o negativo)
            num_str = ''
            x= i
            if s[i] == '-':
                num_str += '-'
                i += 1
            while x < len(s) and s[x] != ' ':
                num_str += s[x]
                x += 1
            pila.put(float(num_str))

    return pila.get()


def dame_inverso_p(pila:Pila[any])->Pila[int]:
    pila_aux1 = Pila()
    inverso = []
    while not pila.empty():
        inverso.append(pila.get())
    for i in range(len(inverso)-1,-1,-1):
        pila.put(inverso[i])
    pila_inversa = Pila()
    for i in range(len(inverso)):
        pila_inversa.put(inverso[i])
    return pila_inversa





def intercalar_p(p1:Pila[any],p2:Pila[any])->Pila[any]:
    pila_inversa_1 = dame_inverso_p(p1)
    pila_inversa_2 = dame_inverso_p(p2)
    pila_intercalada : Pila[any] = Pila()
    while not pila_inversa_2.empty():
        pila_intercalada.put(pila_inversa_1.get())
        pila_intercalada.put(pila_inversa_2.get())
    return pila_intercalada

p1 = Pila()
p1.put(1)
p1.put(2)
p1.put(3)
#mi pila1 es [3,2,1], 3 es el tope
print(mostrar_pila(p1))
print("su inverso es:")
print(mostrar_pila(dame_inverso(p1)))


p2 = Pila()
p2.put(4)
p2.put(5)
p2.put(6)
#mi pila2 es [6,5,4], 6 es el tope
print(mostrar_pila(p2))
print("su inverso es:")
print(mostrar_pila(dame_inverso(p2)))

pila_interc = intercalar(p1,p2)
#se espera que esta pila sea igual a : [1,4,2,5,3,6]
#respetamos el orden de cada pila, pues si por ejemplo si pintaramos de colores distintos a p1 y p2 dentro de pila_interc, vemos que se respeta su orden de arriba a abajo
#ademas el tope de pila_interc es el tope de p2
print(mostrar_pila(pila_interc))


class TestEjercicio8(unittest.TestCase):
    def test_pila_vacia(self) -> None:
        self.assertTrue(generar_nros_al_azar_pila(0, 0, 10).empty())

    def test_pila_10_elem_0_10(self) -> None:
        pila: Pila[int] = generar_nros_al_azar_pila(10, 0, 10)
        cantidad: int = 0
        while not pila.empty():
            elemento: int = pila.get()
            if not (0 <= elemento <= 10):
                self.fail()
            cantidad += 1
        self.assertEqual(cantidad, 10)

    def test_pila_10_elem_10_20(self) -> None:
        pila: Pila[int] = generar_nros_al_azar_pila(10, 10, 20)
        cantidad: int = 0
        while not pila.empty():
            elemento: int = pila.get()
            if not (10 <= elemento <= 20):
                self.fail()
            cantidad += 1
        self.assertEqual(cantidad, 10)




# COLAS

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




def generar_nros_al_azar_cola(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    res: Cola[int] = Cola()
    while cantidad > 0:
        res.put(random.randint(desde, hasta))
        cantidad = cantidad - 1
    return res  

def cantidad_elementos(c:Cola[int])->int:
    cola_aux = Cola()
    cantidad = 0
    while not c.empty():
        cola_aux.put(c.get())
        cantidad += 1
    while not cola_aux.empty():
        c.put(cola_aux.get())
    return cantidad



def buscar_el_maximo_c(c: Cola[int]) -> int:
    cola_auxiliar: Cola[int] = Cola()
    maximo: int = c.get()
    cola_auxiliar.put(maximo)
    while not c.empty():
        elem: int = c.get()
        if elem > maximo:
            maximo = elem
        cola_auxiliar.put(elem)
    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())
    return maximo


def buscar_nota_minima(c:Cola[tuple[str,int]]) -> tuple[str,int]:
    cola_aux: Cola = Cola()
    tupla_inicio: tuple[str,int] = c.get()#Aca estoy obteniendo el primer elemento de mi cola
    alumno: str = tupla_inicio[0]  #de mi primer elemento obtengo el nombre del alumno
    nota_minima: int = tupla_inicio[1] #de mi primer elemento obtengo la nota del alumno    
    cola_aux.put((alumno,nota_minima)) 
    
    while not c.empty():
        tupla = c.get()
        if nota_minima > tupla[1]:
            alumno = tupla[0]
            nota_minima = tupla[1]
        cola_aux.put(tupla)

    #Reconstruyo la cola
    while not cola_aux.empty():
        c.put(cola_aux.get())
    
    return (alumno,nota_minima)    


def dame_inverso_cola(cola:Cola[any])->Cola[int]:
    inverso = []
    while not cola.empty():
        inverso.append(cola.get())
    for i in range(len(inverso)):
        cola.put(inverso[i])
    cola_inversa = Cola()
    for i in range(len(inverso)-1,-1,-1):
        cola_inversa.put(inverso[i])
    return cola_inversa





def intercalar(c1:Cola[any],c2:Cola[any])->Cola[any]:
    cola_inversa_1 = dame_inverso_cola(c1)
    cola_inversa_2 = dame_inverso_cola(c2)
    cola_orig_1 = dame_inverso_cola(cola_inversa_1)
    cola_orig_2 = dame_inverso_cola(cola_inversa_2)
    cola_intercalada : Cola[any] = Cola()
    while not cola_orig_2.empty():
        cola_intercalada.put(cola_orig_1.get())
        cola_intercalada.put(cola_orig_2.get())
    return cola_intercalada


#cola1 = Cola()
#cola1.put(3)
#cola1.put(2)
#cola1.put(1)
#
#cola2 = Cola()
#cola2.put(4)
#cola2.put(5)
#cola2.put(6)
#
#cola_interc = intercalar(cola1,cola2)
#mostrar_cola(cola_interc)
#print("cola 1")
#mostrar_cola(cola1)
#print("cola 2")
#mostrar_cola(cola2)



def pertenece(lista: list[int], e: int) -> bool: 
    for elemento in lista: 
        if elemento == e: 
            return True
    return False

def armar_secuencia_de_bingo() -> Cola[int]: 
    res: Cola[int] = Cola()
    lista: list[int] = []
    for i in range(50):
        lista.append(i)
    random.shuffle(lista)
    for i in range(len(lista)):
        res.put(lista[i])
    return res

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int: 
    res: int = 0
    cantidad_bolillas_acertadas: int = 0
    cantidad_numeros_en_carton: int = len(carton)
    bolillero_auxiliar: Cola[int] = Cola()
    # Esto vale solamente porque asumimos que nos van a pasar un bolillero que tiene a todos los numeros de nuestro carton. Si no fuera asi este while no termina nunca.
    while not (cantidad_bolillas_acertadas == cantidad_numeros_en_carton): 
        bolilla_actual: int = bolillero.get()
        bolillero_auxiliar.put(bolilla_actual)
        if pertenece(carton, bolilla_actual): 
            cantidad_bolillas_acertadas += 1
        res += 1
    # Ciclo para terminar de vaciar el bolillero
    while not (bolillero.empty()): 
        bolilla_actual: int = bolillero.get()
        bolillero_auxiliar.put(bolilla_actual)
    
    # Ciclo para pasar del bolillero auxiliar al parametro
    while not (bolillero_auxiliar.empty()):
        num: int = bolillero_auxiliar.get()
        bolillero.put(num)

    return res

    jugar_carton_de_bingo()


def pacientes_urgentes(c:Cola[tuple[(int,str,str)]])->int:
    res :int = 0 #contador de numeros < 4 en toda primer componente de c 
    cola_aux = Cola() # la uso para reconstruir la orig

    while not c.empty():
        elem = c.get()
        cola_aux.put(elem)
        if elem[0] < 4: #corroboro si es de tipo urgente o no
            res +=1

    #reconstruyo mi cola orig
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return res

#pacientes = Cola()
#pacientes.put( (3,"Benja","kinesio") )
#pacientes.put( (3,"rodri","traumatologo") )
#pacientes.put( (3,"facu","radiologo") )
#mostrar_cola(pacientes) #se espera visualizar que aparece en este orden (lo doy ppor nombre noma) : [benja,rodri,facu], benja es el primero que entra, rodri el segundo, facu el ult. 
##ahora aplico pacientes_urgentes, espero como resultado: 2
#print(pacientes_urgentes(pacientes)) 
## me dio 2, hasta aca todo bien
## veo si la cola sigue estando bien ordenada
#mostrar_cola(pacientes)
## confirmo que esta todo okey 


#EJ 15
#REQUIERE QUE PARA TODA ELEMENTO EN COLA[i][1] sea de longitud 8, con 0<=i<len(cola)
#Requiere que no existan DNIs repetidos
#requiere que para todo  0<=i<len(cola) se necesita que COLA[i][2] y COLA[i][3] sean solo de tipo bool
#asegura que no se pperdera c 
#asegura devolver len(res) == len(c)
#asegura no devolver elementos repetidos en res




#algoritmo
#Primero deberiamos recorrer toda la cola, y fijarse cuales son los que tienen prioridad, pues la cola cumple que los primeros que entran son los primeros que salen
# en este caso, los que tienen prioridad son los que entran primero y salen primero
# si cola[i][3] == True (osea tiene prioridad), se lo pone en la nueva cola
#Una vez finalizado eso, pasamos a ver quienes tienen bancaria preferencial
# si cola[i][2] == True (osea tiene cuenta bancaria preferencial), se lo pone en la cola anterior, manteniendo el orden
# finalmente, vuelvo a recorrer la cola y sacando elemento a elemento, poniendolo en la nueva cola.

#me hago una nueva cola que sea la cola original pero al reves
#cola_inversa = dame_inverso_cola(cola)

#con esto me puedo hacer como una copia de mi cola original, entonces solo me basta con operar con esta cola, y la original nunca se vera afectada
#cola_orig= dame_inverso_cola(cola_inversa)

def cola_prioridad(cola: Cola[tuple[str, int, bool, bool]])->Cola[tuple[str, int, bool, bool]]:
    cola_prioridad = Cola()
    #me hago una nueva cola que sea la cola original pero al reves
    cola_inversa = dame_inverso_cola(cola)
    #con esto me puedo hacer como una copia de mi cola original, entonces solo me basta con operar con esta cola, y la original nunca se vera afectada
    cola_orig= dame_inverso_cola(cola_inversa)
    while not cola_orig.empty():
        elem = cola_orig.get()
        if elem[3] == True:
            cola_prioridad.put(elem)
    return cola_prioridad



#dada una cola, devuelvo las personas que son cuentas preferenciales
def cola_preferencial(cola: Cola[tuple[str, int, bool, bool]])->Cola[tuple[str, int, bool, bool]]:
    cola_preference = Cola()
    #me hago una nueva cola que sea la cola original pero al reves
    cola_inversa = dame_inverso_cola(cola)
    #con esto me puedo hacer como una copia de mi cola original, entonces solo me basta con operar con esta cola, y la original nunca se vera afectada
    cola_orig= dame_inverso_cola(cola_inversa)
    while not cola_orig.empty():
        elem = cola_orig.get()
        if elem[2] == True:
            cola_preference.put(elem)
    return cola_preference


#cola_banco = Cola()
#cola_banco.put( ("Benjamin Dominguez",46728095,True,True) )
#cola_banco.put( ("facu rodrigue",1111111,False,False) )
#cola_banco.put( ("carlos palacios",7777777,False,True) )
##Esppero obtener en mi nueva cola que benjamin este a la derecha del todo y que carlos palacios este atras suyo
##La cola antes de ser usada
#mostrar_cola(cola_banco)
#cola_prio = cola_prioridad(cola_banco)
#cola_pref = cola_preferencial(cola_banco)
#print("La cola luego de ser usada")
#mostrar_cola(cola_banco)
#print("La cola de prioridad") 
#mostrar_cola(cola_prio)
#print("La cola de preferencial") 
#mostrar_cola(cola_pref)

#Observo que mi cola original se mantiene intacta, y ademas obtengo lo que queria, al usar mostrar cola primero veo a "benjamin", y esta bien porque fue el pprimero 
#en ingresar a la cola del banco
#Luego veo a carlos palacios, chileno mogolico de mierda muerto


#Para chequear que no hayan repetidos, me hice un auxiliar que se fije si se repite el DNI
def repite_DNI(cola: Cola[tuple[str, int, bool, bool]],dni:int) -> bool: 
    cola_aux = Cola()
    res = False
    while not cola.empty():
        elemento = cola.get()
        cola_aux.put(elemento) 
        if elemento[1] == dni: 
            res = True
    while not cola_aux.empty():
        cola.put(cola_aux.get())
    return res


def atencion_a_clientes(cola: Cola[tuple[str, int, bool, bool]])->Cola[tuple[str, int, bool, bool]]:
    #me hago una nueva cola que sea la cola original pero al reves
    cola_inversa = dame_inverso_cola(cola)
    #con esto me puedo hacer como una copia de mi cola original, entonces solo me basta con operar con esta cola, y la original nunca se vera afectada
    cola_orig= dame_inverso_cola(cola_inversa)
    #Hago mi cola de prioridad
    cola_prio = cola_prioridad(cola_orig)
    #Hago mi cola de preferencial
    cola_pref = cola_preferencial(cola_orig)
    #Ahora como mis dos colas pueden tener elementos compartidos y quiero ir poniendo en orden cada elemento, entonces a mi cola de prioridad le voy
    #Encolando los elementos de la cola preferencial, pues es el orden correcto. Ahora como pueden compartir, entonces simplemente agrego el elemento
    #Si no pertenece a mi cola de prioridad
    while not cola_pref.empty():
        elem = cola_pref.get()
        if not (repite_DNI(cola_prio,elem[1])): #Si dentro de mi cola de prioridad, no se repite el elemento de la cola de preferencia, entonces lo agrego
            cola_prio.put(elem)
    #Ahora hago lo mismo, pero para los elementos restantes que no sean ni preferencial ni prioridad

    while not cola_orig.empty():
        elem = cola_orig.get()
        if elem[2] == False and elem[3] == False:
            cola_prio.put(elem)
    #Finalmente me basta con devolver cola_prio
    return cola_prio

#cola_banco = Cola()
#cola_banco.put( ("Benjamin Dominguez",46728095,False,True) )#Este deberia aparecer en el primero del todo al utilizar atencion_a_clientes
#cola_banco.put( ("facu rodrigue",1111111,True,False) )#Este deberia aparecer cuarto al utilizar atencion_a_clientes
#cola_banco.put( ("carlos palacios",7777777,False,False) )#Este deberia aparecer quinto al utilizar atencion_a_clientes
#cola_banco.put( ("ppepe",4532453,True,True) )#Este deberia aparecer en el 2do del todo al utilizar atencion_a_clientes
#cola_banco.put( ("ciro",22323455,False,False) )#Este deberia aparecer sexto al utilizar atencion_a_clientes
#cola_banco.put( ("gordo",22547899,False,True) )#Este deberia aparecer en el 3ero del todo al utilizar atencion_a_clientes
    

#cuando me refiero a 1ero segundo y bla bla, me refiero a cuandoutilizo la funcion mostrar cola, leemos de arriba hacia abajo
#el primero que te aparece, osea el que esta arriba del todo, es el chabon que ingreso primero, y es justamente el que primero sale
#entonces ese seria como el orden ppara q se entienda mejor esto

#print("La cola del banco inicialmente :")
#mostrar_cola(cola_banco)
#print("La cola prioritaria es : ")
#cola_prio = cola_prioridad(cola_banco)
#mostrar_cola(cola_prio)
#print("La cola preferencial es : ")
#cola_pref = cola_preferencial(cola_banco)
#mostrar_cola(cola_pref)
#
#
#print("La cola del banco luego es :")
#mostrar_cola(cola_banco)
#
#
#cola_ordenada = atencion_a_clientes(cola_banco)
##me hago mi cola ordenada 
#print("La cola ordenada del banco es asi : ")
#mostrar_cola(cola_ordenada)
##muestro mi cola orig
#print("La cola del banco original luego de utilizar la funcion :")
#mostrar_cola(cola_banco)


# DICCIONARIOS


        
    
     
def calcular_promedio_por_estudiante(notas:list[(str,float)])->dict[str,float]:   
    res:dict = {}
    for estudiante in notas:
           res[estudiante[0]] = estudiante[1]
    return res

#
#notas = [ ("pepe",4.5),("pepe",5.5)]
#print(notas)
#
#notas_a_dic = calcular_promedio_por_estudiante(notas)
#print(notas_a_dic)
#llaves = notas_a_dic.keys()
#print(llaves)




def visitar_sitio(historiales:dict[str,Pila:[str]],usuario:str,sitio:str)->None:
    if usuario in historiales.keys():#si usuario esta en las llaves de historiales@pre, apilo el sitio 
        historiales[usuario].put(sitio)
    else:
        nuevo_hist= Pila()
        nuevo_hist.put(sitio) 
        historiales[usuario] = nuevo_hist #caso contrario, creo una nueva llave con este usuario y una nueva pila a la cual le apilo el sitio indicado
        

#sitios_ben = Pila()
#sitios_ben.put("campus")#primer visitado
#sitios_ben.put("google")#segundo visitado
#print("Mis sitios anteriores:")
#mostrar_pila(sitios_ben)
#historiales_muestra = {"ben":["google","campus"]} # asi se deberia ver el historial antes de agregar un nuevo sitio
#historiales_orig = {"ben":sitios_ben}
#
#visitar_sitio(historiales_orig,"ben","youtube") #visito un nuevo sitio 
#print("Ahora veo mi pila luego de usar visitar_sitio:")
#mostrar_pila(sitios_ben) #ahora espero ver que mi pila original fue cambiada
#print(historiales_orig) #espero no ver ningun usuario nuevo 

#ahora pruebo usar el mismo historial, pero con un nuevo usuario 

#visitar_sitio(historiales_orig,"juan","firefox") #juan no esta en historiales_orig@pre, ahora espero verlo en llaves 
#print(historiales_orig.keys()) # observo que se agrego juan
#print(historiales_orig.values()) # observo que se creo una pila con este sitio
#mostrar_pila(historiales_orig["juan"]) #observo que justamente, esta pila existe y contiene a firefox
#cumplo todos los asegura

def navegar_atras(historiales:dict[str,Pila:[str]],usuario:str)->str:
    res = historiales[usuario].get()
    return res

# ahora voy a querer para 'ben' que esta en historiales_orig, ir hacia atras, osea ir a youtube que es el tope de historiales_orig['ben']
#res = navegar_atras(historiales_orig,"ben")
#print(res)#observo youtube, esta bien
#print(historiales_orig.keys())#observo que mis claves no cambian
#print(historiales_orig.values()) #observo que mi cant de llaves no cambia
#mostrar_pila(historiales_orig["juan"]) #observo que la otra llave que tenia, no cambia su valor
#mostrar_pila(sitios_ben)#observo que desaparecio youtube, que es lo que buscaba, y me queda google y campus


#historiales = {}
#visitar_sitio(historiales, "Usuario1", "google.com")
#visitar_sitio(historiales, "Usuario1", "facebook.com")
#print("La pila de historiales de Usuario1 es:")
#mostrar_pila(historiales["Usuario1"])#espero ver arriba del todo a facebook, luego ver a google
#
#navegar_atras(historiales, "Usuario1")#si navego hacia atras, entonces esto me deberia sacar el tope, osea facebook.com
#print("La pila de historiales de Usuario1 es:")#espero solo ver a google.com
#mostrar_pila(historiales["Usuario1"])
#
#visitar_sitio(historiales, "Usuario2", "youtube.com") 
#print("La pila de historiales de Usuario2 es:")
#mostrar_pila(historiales["Usuario2"]) #Espero ver a youtube.com
#print(historiales.keys())#espero ver a usuario1 y 2 en sus llaves
#print(historiales.values())#espero ver 2 pilas 
##no observo fallas, el codigo anda a priori





















def contar_lineas(nombre_archivo:str)->int:
    archivo = open(nombre_archivo,"r")
    cant_lineas = len(archivo.readlines())
    archivo.close()
    return cant_lineas

def mostarLineas(nombre_archivo:str)->int:
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas

#lineas = (mostarLineas("aaa"))
#print(lineas[2][10])
