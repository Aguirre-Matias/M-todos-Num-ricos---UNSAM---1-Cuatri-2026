import numpy as np

def trapecios_compuestos(f,a,b,h):
    suma=0
    for x in np.arange(a+h,b,h):
        suma=suma+f(x)
    integ=h*(((f(a)+f(b))/2)+suma)
    return integ