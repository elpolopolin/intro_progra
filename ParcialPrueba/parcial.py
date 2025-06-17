

def maximas_cantidades_consecutivos(v:list[int]) -> dict[int,int] :
    contador = 0
    numanterior = 'nada'
    res : dict[int,int] = {}
    for i in range(len(v)) :
        if (numanterior != v[i]):
            contador = 1
            numanterior = v[i]
        else :
            contador +=1

        if (v[i] in res) :
            if (res[v[i]] < contador):
                res[v[i]] = contador
        else:
            res[v[i]] = contador
    return res

print(maximas_cantidades_consecutivos([-1, -2, -2, -3, -3, -1, -1]))

def esPrimo(num:int) -> bool :
    divisores = []
    for i in range(num +1):
        if (i != 0):
            if num % i == 0 :
                divisores.append(i)
    
    if (divisores != [1,num]) :
        return False
    else:
        return True
print(esPrimo(1))

def maxima_cantidad_primos(a:list[list[int]]) -> int:
    #columnas = len(a[0])
    max = 0
    for columna in range (len(a[0])) :
        contador = 0
        for fila in range(len(a)) :
            if (esPrimo(a[fila][columna])):
                contador +=1
        if (max < contador) : 
            max = contador
    return max

print(maxima_cantidad_primos(
    [[1,2,3],
    [3,4,5],
    [10,4,4],
    [10,4,5],
    [2,2,5],
    [2,2,2]]
))

"""
[1,2,3],
[1,3,5],
"""
from queue import LifoQueue as Pila
from queue import Queue as Cola

def construir_cola_con_elementos(elementos: list[tuple[int, int]]) -> Cola[tuple[int, int]]:
    res: Cola = Cola()
    for elem in elementos:
        res.put(elem)
    return res

def tuplas_positivas_y_negativas(c:Cola[tuple[int,int]]): 
    cola_aux = Cola()
    elementosMenoresAcero :list[tuple[int,int]] = []
    while not c.empty() :
        elem :(int,int) = c.get()
        if (elem[0] * elem[1] > 0) :
            cola_aux.put(elem)
        elif (elem[0] * elem[1] < 0) :
            elementosMenoresAcero.append(elem)

    for i in range(len(elementosMenoresAcero)) :
        cola_aux.put(elementosMenoresAcero[i])
    while not cola_aux.empty() :
        c.put(cola_aux.get())

colaa = construir_cola_con_elementos([(1, 2), (1, -2), (-1, -2), (1, 0), (0, 2), (0, 0), (3, 2)])
print(colaa.queue)
tuplas_positivas_y_negativas(colaa)
print(colaa.queue)
        
def resolver_cuenta(s:str) -> float :
    numero:str = ""
    numeros = []
    total = 0
    for letra in s :
        if (letra in ['0','1','2','3','4','5','6','7','8','9','.']):
            numero += letra
        elif (letra == '-' and numero == ''):
            numero += '-'
        elif (letra == '-' and numero != ''):
            numeros.append(float(numero))
            numero = '-'
        elif (numero):
            print("numero",numero)
            numeros.append(float(numero))
            numero = ''
    if (numero) :
        print("ultimo numero", numero)
        numeros.append(float(numero))

    for i in range(len(numeros)) :
        total += numeros[i]
            

    return total

def separar_cuenta(s:str) -> list[str]:
    res: list[str] = []
    i: int = 0
    while i < len(s):
        if s[i] == '+' or s[i] == '-':
            res.append(s[i])
            i += 1
        else:
            aux: str = ""
            while i < len(s) and s[i] != '+' and s[i] != '-':
                aux += s[i]
                i += 1
                
            res.append(aux)
    
    return res

# Ejercicio 4 nacho
def resolver_cuenta(s: str) -> float:
    cuenta_separada: list[str] = separar_cuenta(s)
    cuenta: float = 0
    
    if cuenta_separada[0] != '+' and cuenta_separada[0] != '-':
        cuenta = float(cuenta_separada[0])
    
    for i in range(len(cuenta_separada)):
        if cuenta_separada[i] == '+':
            cuenta += float(cuenta_separada[i+1])
        elif cuenta_separada[i] == '-':
            cuenta -= float(cuenta_separada[i+1])
               
    return cuenta
                    
print(resolver_cuenta("50.25+50.255+100.277+1"))





