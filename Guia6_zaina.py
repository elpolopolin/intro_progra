import math
#Guia 6
#Ejercicio 1
#1.1
def imprimir_hola():
    print ("Hola")    
#1.2
def imprimir_guns():
    print ("She got a smile")
    print ("That it seems to me")
imprimir_guns()
#1.3
def raiz_de3():
    print(math.sqrt(3))
raiz_de3()
#1.5
def perimetro()-> float:
    res: float = 1*2*math.pi
    print (res)
    return (res)
perimetro()

#Ejercicio 2
#2.1
def imprimir_saludo (nombre:str):
    print ("Hola papu "+ nombre)
imprimir_saludo("Franco")
#2.2    
def raiz (n:int):
    print(math.sqrt(n))
raiz (16)    
#2.3
def farenheit_a_celcius(n:int):
    res = (n-32)*5/9
    print (res)
    print(round(res, 4))
#2.4
def versox2(verso:str):
    print (verso*2)
versox2 ("ndeah")
#2.5
def es_multiplo(n:int, m:int)-> bool :
    return n % m == 0 
print (es_multiplo(10,5))
#2.6
def es_par(n: int) -> bool:
    if es_multiplo(n, 2):
        print(f"{n} es par")
        return True
    else:
        print(f"{n} es impar")
        return False
es_par (5)
#2.7
def cant_pizzas(n: int, m: int) -> int:
    print("Tienen que haber estas pizzas:")
    return math.ceil((n * m) / 8) 
print(cant_pizzas(5, 2))

#Ejercicio 3
#3.1
def alguno_es0 (n:int, m:int) -> bool:
    print ("Algun numero ingresado es 0?")
    res:bool = n == 0 or m == 0
    print (res)
    return res  
alguno_es0 (0,1)
#3.2
def ambos_son0 (n:int, m:int)-> bool:
    print ("Los dos numeros ingresados son 0?")
    res:bool = n== 0 and m == 0
    print (res)
    return res
ambos_son0 (0,1)  
#3.3
def es_nombre_largo (nombre:str)-> bool:
    res:bool = len (nombre) >= 3 and len (nombre) <= 8 
    return res
print (es_nombre_largo("papu"))
#3.4
def es_bisiesto(ano:int)-> bool:
    print("El año ingresado es bisiesto?")
    res:bool = ano%400 == 0 or ano%4 == 0 and ano%100 != 0
    print (res)
    return (res)
es_bisiesto (2020)

#Ejercicio 4

#Ejercicio 5
#5.1
def devolver_el_doble_si_es_par (n:int) -> bool:
    if (n%2==0):
        print (n*2)
    else:
        return (n)
devolver_el_doble_si_es_par(2)
#5.2
def devolver_valor_si_es_par_si_no_el_que_sigue (n:int) -> int:
    if (n%2==0):
        print (n)
    else:
        print (n+1)
devolver_valor_si_es_par_si_no_el_que_sigue (5)
#5.4
def lindo_nombre (nombre:str) -> str:
    if len(nombre) > 5:
        print ("Tu nombre tiene muchas letras! " + nombre)
    else:
        print ("Tu nombre tiene menos de 5 caracteres! " + nombre)
lindo_nombre ("franco")
#5.5
def el_rango (n:int) -> str:
    if (n<5):
        print ("Menor a 5!")
    if(n>9 and n<21):
        print ("Entre 10 y 20!")
    if(n>20):
        print ("Mayor a 20!")
el_rango(10)
#5.6       
def que_te_toca (sexo:str, edad:int):
    if (sexo =="M"):
        if (edad > 64):
            print ("Anda de vacaciones!")
        else :
            print("Te toca trabajar!")
    else:
        if (edad > 59):
            print ("Anda de vacaciones!")
        else:
            print ("Te toca trabajar!")            
que_te_toca("M",65)

#Ejercicio 6
#6.1
def uno_al_diez ():
    i=1
    while (i<11):
        print (i)
        i= i+1
uno_al_diez()
#6.2
def pares ():
    i = 10
    while (i < 41):
        if (i%2 == 0):
            print (i)
            i= i + 1
        else: 
            i= i+1
pares()
#6.3
def eco ():
    for i in range (1, 11):
        print ("eco")
eco()        
#6.4
def cuenta_atras (n:int):
    while (n >=1):
        print (n)
        n = n-1
    print ("despegue")
cuenta_atras(5)
#6.5
def viaje_en_el_tiempo (anopartida:int, anollegada:int):
    for i in range(1,anopartida-anollegada+1):
        anopartida = anopartida - 1
        print ("Estamos en el año:" )
        print (anopartida)
viaje_en_el_tiempo(2025,2020)
#6.6
def viaje_en_el_tiempo_dos(anopartida: int):
    while anopartida > 384:
        anopartida -= 20 
        print(f"Estamos en el año: {anopartida}")
viaje_en_el_tiempo_dos(1000)

#EsPrimo
def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print (es_primo(4))


    
