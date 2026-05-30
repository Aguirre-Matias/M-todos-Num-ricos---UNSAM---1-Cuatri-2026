# Para limpiar la terminal antes de continuar
# Desde acá

#import os

#os.system('cls' if os.name == 'nt' else 'clear')

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,10,0.1)
# print("t = ",t)

f= lambda x: np.sin(x)
g= np.cos(t)

# PLOT
plt.figure(1) # Crear una ventana donde graficar
plt.subplot(1,2,2) # Esto genera una ventana (figure) dividida en 4 y grafica en posicion 1
plt.plot(t,f(t), label = "Funcion Seno", marker=".", linestyle=":", color="red") # Grafico t y f(t) y le pongo atributos
# Identificar los puntos, la forma de lina, el color
plt.plot(t,g, label = "Funcion Coseno", marker="x", linestyle="-", color="blue")
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones Trigonometricas") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
plt.axis([0,6.5,-1,1]) # A axis le paso un vector adentro de la funcion --> axis([Xinf, Xsup, Yinf, Ysup])

plt.subplot(1,2,1)
plt.plot(t,f(t), label = "Funcion Seno", marker=".", linestyle=":", color="red") # Grafico t y f(t) y le pongo atributos
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones Trigonometricas") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
plt.axis([0,6.5,-1,1]) # A axis le paso un vector adentro de la funcion --> axis([Xinf, Xsup, Yinf, Ysup])

plt.show() # Muestra todo lo que se pide para graficar
