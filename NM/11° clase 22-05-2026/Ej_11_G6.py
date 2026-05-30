
# La base de un pórtico es de 10m. Se mide la altura en cinco puntos equidistantes, incluyendo los extremos,
# obteniendo los datos 5m, 6m, 9m, 6m y 5m. Estimar el área del pórtico.
# 
# estimar con:
# polifit polival con trapecios
# osea hacer una funcion con las x medidas de la altura (una parabola) y calcular la integral de esta de 0 a 10

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev
import integracion as int

base=10
alturas=[5,6,9,6,5]
distancias= [0,2.5,5,7.5,10]
h=0.1
rf=np.arange(0,10.1,0.1)

cof= np.polyfit(distancias,alturas,4) # coef del poli
f_polyval= lambda x: np.polyval(cof,x)

cof_spline= splrep(distancias,alturas,k=2)
f_spline= lambda x: splev(x,cof_spline)

Area=int.trapecios_compuestos(f_polyval,0,10,h)
print("El area del portico en polyval es:",Area)

Area1=int.trapecios_compuestos(f_spline,0,10,h)
print("El area del portico en spline es:",Area1)

plt.figure(1) # Crear una ventana donde graficar
plt.plot(distancias,alturas,label = "Medidas", marker="*", linestyle="", color="red")
plt.plot(rf,f_polyval(rf),label = "Funcion Polyval", marker="", linestyle="-", color="blue")
plt.plot(rf,f_spline(rf),label = "Funcion Spline", marker="", linestyle="-", color="green")

plt.xlabel("metros") # Nombre del eje X
plt.ylabel("metros") # Nombre del eje Y
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
plt.axis([-0.5,10.5,0,9.5]) # A axis le paso un vector adentro de la funcion --> axis([Xinf, Xsup, Yinf, Ysup])
plt.show()

