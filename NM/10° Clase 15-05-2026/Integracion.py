# Para limpiar la terminal antes de continuar
# Desde acá
#import os
#os.system('cls' if os.name == 'nt' else 'clear')

import numpy as np

def trapCompuestos(f,a,b,h):
    t1=(f(a)+f(b))/2
    sum=0
    for i in np.arange(a+h,b,h): # el arange no toma el ultimo valor, por lo que se debe sumar h al final
        sum= sum + f(i)
    Res=(t1+sum)*h
    return Res

# metodo de simpson compuestos h/3(f(a)+2*E(f(Xk-2)....+4E(f(Xk-1))+f(b)))
def simpCompuestos(f,a,b,h):
    spar=0
    simpar=0
    n=(b-a)/h
    for i in np.arange(a+h,b,2*h):
        simpar= simpar + f(i)
    for i in np.arange(a+2*h,b,2*h):
        spar= spar + f(i)
    Res=(h/3)*(f(a)+2*spar+4*simpar+f(b))
    return Res