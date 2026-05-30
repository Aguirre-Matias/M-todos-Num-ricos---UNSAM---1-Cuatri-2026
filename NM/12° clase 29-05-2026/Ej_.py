import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev
import Metodos as met

fd= lambda t,y: -0.2*y
t0=0
tf=1
y0=10
h=0.25

puntos, t1=met.euler(fd, t0, tf, y0, h)
puntosHEUN, t2=met.Huen(fd, t0, tf, y0, h)
puntosRK, t3=met.RungeKutta(fd, t0, tf, y0, h)

plt.figure(1)

plt.plot(t1, puntos, color="red")
plt.plot(t2, puntosHEUN, color="blue")
plt.plot(t3, puntosRK, color="green")
plt.xlabel("t") # Nombre del eje X
plt.ylabel("y") # Nombre del eje Y
plt.title("EDO") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
plt.show() # Muestra el grafico