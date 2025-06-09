#guia integradora
"""
Ejercicio 1. Veterinaria - Stock
En la veterinaria ”Exactas’s pets”, al finalizar cada d´ıa, el personal registra en papeles los nombres y la cantidad actual de
los productos cuyo stock ha cambiado. Para mejorar la gesti´on, desde la direcci´on de la veterinaria han pedido desarrollar una
soluci´on en Python que les permita analizar las fluctuaciones del stock. Se pide implementar una funci´on, que reciba una lista
de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento. La funci´on debe procesar esta lista
y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su m´ınimo y m´aximo stock
hist´orico registrado.
problema stock productos (in stock cambios : seq⟨str × Z⟩) : seq⟨Z⟩ {
requiere: {Todos los elementos de stock cambios est´an formados por un str no vac´ıo y un entero ≥ 0.}
asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock cambios (o sea, un producto).}
asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock cambios.}
asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese
producto en stock cambios y como segundo valor el mayor.}
}
"""

stockRegistrado : dict = {}

def stockProductos(stockCambios:list[tuple[str,int]]) -> dict[int] :
    res : dict = {}
    for i in range (len(stockCambios)):
        #s, cantidad = stockCambios[i]
        if not ( stockCambios[i][0] in stockRegistrado) :
            stockRegistrado[stockCambios[i][0]] = (stockCambios[i][1],stockCambios[i][1]) #le asigno max y min al dict q por ahora son mismo valor unico
            res[stockCambios[i][0]] = (stockCambios[i][1],stockCambios[i][1])
        else :
            if stockRegistrado[stockCambios[i][0]][1] < stockCambios[i][1] :
                stockRegistrado[stockCambios[i][0]] = (stockRegistrado[stockCambios[i][0]][0], stockCambios[i][1]) #ASIGNO NUEVO MAYOR
                res[stockCambios[i][0]] = (stockRegistrado[stockCambios[i][0]][0], stockCambios[i][1])
            if stockRegistrado[stockCambios[i][0]][0] > stockCambios[i][1]:
                stockRegistrado[stockCambios[i][0]] = (stockCambios[i][1], stockRegistrado[stockCambios[i][0]][1]) #asigno nuevo menor
                res[stockCambios[i][0]] = (stockCambios[i][1], stockRegistrado[stockCambios[i][0]][1])


    return res

#dia 1
print((stockProductos([("agua",1),("coca",4),("agua",2),("agua",1),("agua",5)])))
