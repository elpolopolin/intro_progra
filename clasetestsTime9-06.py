

#operaciones elemntales +,-,*,%... tiempo = 1. operaciones elementales = cada operacion

def producto_1 (n:int) -> int: 
    res: int= 1 #+1
    i:int = 1 #+1 (n)
    while i <= n : #(n veces true + 1 vez false)
        res = res * i #2 oE
        i = i +1 # 2 OE
    return res #+1 oe

#oes = 1 +1 + n*(2 +2) +1 +1= [4 +4n]
producto_1(3)


def producto_1 (n:int) -> int: 
    res: int= 1 #+1
    i:int = 1 #+1 (n veces mas 1)
    while i <= n : #(n veces true + 1 vez false)
        j :int = 1 #+1
        while j <= n: #(n veces + 1 false)
            res = res * i * j #3
            j = j +1 #2

        i = i +1 #+2
    return res #+1 oe

#oes = 1 + 1 +1 + n(1+1(false)+n(3 +2)+2) + 1 = 5n(cuadrado) +4n + 3 


