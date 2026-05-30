import numpy as np
import Integracion as int

# f= lambda x: np.sin(x)
# f= lambda x: np.exp(-x**2)
f= lambda x: np.exp(x)*np.cos(x)

a=float(input("Ingrese el intervalo de integracion inferior: "))
b=float(input("Ingrese el intervalo de integracion superior: "))
h=float(input("Ingrese la resolucion de la integracion: "))
print("El resultado de la integracion (trapecio) es: ", int.trapCompuestos(f,a,b,h))
print("El resultado de la integracion (simpson) es: ", int.simpCompuestos(f,a,b,h))