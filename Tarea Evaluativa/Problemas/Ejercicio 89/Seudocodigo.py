def Minimun(size, lista):
    a = 0
    i = 1
    while i < size:
        if lista[i] < lista[a]:
            a = i
        i = i + 1
    
    return a 

def Area (r):
    return 3*r*r
