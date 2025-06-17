import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

def pertenece(lista: list[int], e: int) -> bool: 
    for elemento in lista: 
        if elemento == e: 
            return True
    return False

def armar_secuencia_de_bingo() -> Cola[int]: 
    res: Cola[int] = Cola()
    lista: list[int] = []
    for i in range(100):
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

print(jugar_carton_de_bingo([1,2,3,4,5,6,7,8,9,10,11,12],armar_secuencia_de_bingo()))