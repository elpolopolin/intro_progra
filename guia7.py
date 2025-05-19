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
def igualesconsecutivos (s:list[int]) ->bool :
    i= 0
    consecutivos =0
    while i< (len(s)-1) and consecutivos <3 :
        if (s[i] == s[(i+1)]):
            consecutivos +=1
        else :
            consecutivos =0
        i+=1
    return (consecutivos == 3)
print(igualesconsecutivos([1,2,1,1,2,1,1,1]))
          
        