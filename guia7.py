#Trabajamos sobre listas

#pertenece pro
def problema_pertenece (lista: list[int], p:int) -> bool :
    pertenece:bool = False
    i: int = 0
    while(not pertenece and i < len(lista)):
        pertenece = lista[i] == p #true o false
        i += 1
    return pertenece
#1.1
def pertenece (s:list[int],e:int) -> bool :
    for i in range(0,len(s),+1) :
        if ( e == s[i]) :
            return True
    return False
print(pertenece([1,"polo",9,4,5], "polo"))
#pertenece recursivo
def pertenece_recursivo(lista:list[int], e: int) -> bool: 
    if len(lista) == 0: 
        return False
    cabeza_lista : int = lista.pop(0)
    return cabeza_lista == e or pertenece_recursivo(lista, e)
print("pertenece recursivo", pertenece_recursivo([1,2,3,4,10,2], 0)) #pop devuelve el primer elemento de la lista y a su vez lo quita de la lista
#1.2
def divideAtodos(s:list, e:int) -> bool : 
    for i in range (len(s)) :
        if (s[i] % e != 0) :
            return False
    return True

def divideAtodos2(s:list[int], e:int):
    res = False
    i = 0
    while i != len(s) : 
        if (s[i] % e == 0):
            i = i +1
        else :
            return res
    if (i == len(s)) :
        return True 

print(divideAtodos([9,3,3,12], 3))
print("divide a todos 2:",divideAtodos2([1,3,3,12],3))
#1.3
def sumatotal (s:list[int]) -> int :
    suma = 0
    for i in range(len(s)) :
        suma += s[i]
    return suma
print(sumatotal([1,4,10]))
#1.4
def maximo(s:list[int]) :
    maximo = 0
    for i in range(len(s)) :
        if (maximo <= s[i]):
            maximo = s[i]
    return maximo

def maximo2(s:list[int]): 
    i = 0   
    maximo2 = 0 
    while i != len(s) :
        if (maximo2 <= s[i]) :
            maximo2 = s[i]
            i +=1
    return maximo2
print("el maximo valor de la list", maximo([1,20,3,4,5,6,1,1]))
#1 + a/100 = inflacion
#1.5 minimo
def minimo(s:list[int]) -> int :
    min = 0
    for i in range (len(s)) :
        if (min >= s[i]) :
            min = s[i]
    return min
print(min([12,2,3,4,1,10]))
#1.6
def ordenados(s:list[int]) -> bool :
    i = 0
    while i < (len(s)-1) :
        if (s[i] <= s[(i+1)]):
            i += 1
        else : 
         return False
    return ((i+1) == len(s))

print("estan ordenados 3,4,5,1", ordenados([3,4,5,1]))

#1.7
def pos_maximo(s:list[int]) -> int :
    posmax = 0
    for i in range(len(s)):
        if (s[posmax] < s[i]) :
            posmax = i
    return (posmax + 1)
print("pos max [1,2,3,4,1,1]", pos_maximo([1,2,3,4,1,1]))
#1.8 
def pos_minima (s:list[int]) -> int :
    posmin = 0
    for i in range(len(s)) :
        if (s[posmin] > s[i]) :
            posmin = i
    return (posmin +1)
print(pos_minima([1,0,3,4,5]))
#1.9
def longmayor_asiete (s:list[str]) -> bool :
    res = False
    for i in range(len(s)) :
        if (len(s[i]) >= 7 ) : 
            res = True
    return res
print(longmayor_asiete(["polon","nachoidee","golo"]))
#1.10 
def esPalindromo (s:str) -> bool :
    palabraReves = ""
    for i in range (len(s)):
        palabraReves = s[i] + palabraReves
        #print(palabraReves)
    return (palabraReves == s)

print("esee es palindromo", esPalindromo("esee"))

#1.11
def igualesconsecutivos (s:list[int]) -> bool :
    actual = s[0]
    contador = 1
    for i in range(1, len(s)):
        if s[i] == actual:
            contador += 1
            if contador == 3:
                return True
        else:
            actual = s[i]
            contador = 1
    return False

print(igualesconsecutivos([1,2,1,1,2,1,0,1,2,10,10,10]))

#1.12
def quitarRepetidos (x: str, s:list[str]) -> list[str] :
    listaSinXrepetidos = []
    for i in range(len(s)):
        if (x != s[i]):
            listaSinXrepetidos.append(s[i])
    return listaSinXrepetidos

def tres_vocales_distintas (s:list[str]):
    vocalesUsadas = []
    i = 0
    while (i < len(s)) :
        if s[i].lower() in ['a', 'e', 'i', 'o', 'u'] :
            vocalesUsadas.append(s[i].lower())
            s = quitarRepetidos(s[i], s)
        i += 1
    return (len(vocalesUsadas) >= 3)

palabra = input("escriba una palabra para ver si tiene 3 vocales:")
print(tres_vocales_distintas(palabra))
#print(quitarRepetidos('a',"holaa"))

#1.13
def contarSecuenciaOrdenada (s:list[int]) -> int :
    secuenciaOrdenada = 1
    x = 0
    for i in range(1, len(s)):
        if (s[x] < s[i]) :
            secuenciaOrdenada += 1
        else :
            return secuenciaOrdenada
    return secuenciaOrdenada
def quitarPrimerosX (x:int, s:list[int]) -> list :
    nuevalista = []
    for i in range(x,len(s)):
        nuevalista.append(s[i])
    return nuevalista
#print(quitarPrimerosX(3,[1,2,3,4,5,6]))

def secuencia_ordenada_mas_larga (s:list[int]) -> int :
    secuenciaOrdenadaMayor = 0
    i = 0
    while i < (len(s)) :
        secuenciaOrdenadaAcomparar = contarSecuenciaOrdenada(s)
        #print(secuenciaOrdenadaAcomparar)
        if (secuenciaOrdenadaMayor < secuenciaOrdenadaAcomparar):
            secuenciaOrdenadaMayor = secuenciaOrdenadaAcomparar
            s = quitarPrimerosX(secuenciaOrdenadaAcomparar, s)
        i+=1
    return secuenciaOrdenadaMayor

print(secuencia_ordenada_mas_larga([1,2,3,1,2,3,4,5]))
     
#1.13 pos secuencia mas larga

def pos_secuencia_mas_larga(s: list[int]) -> int:
    if not s:
        return -1  # lista vacía
    max_long = 1
    max_pos = 0
    i = 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and s[j] < s[j + 1]:
            j += 1
        long_actual = j - i + 1
        if long_actual > max_long:
            max_long = long_actual
            max_pos = i

        i = j + 1  # saltamos al próximo inicio de secuencia

    return max_pos
    

        