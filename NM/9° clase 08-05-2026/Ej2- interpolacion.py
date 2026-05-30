# Para limpiar la terminal antes de continuar
# Desde acá

#import os

#os.system('cls' if os.name == 'nt' else 'clear')

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep

x = [0.2,0.8,1.0,1.4,2.2,2.7,3.7,4.2,5.7,6.1]
y=[0.2,0.72,0.84,0.99,0.81,0.43,-0.53,-0.87,-0.55,-0.18]

plt.figure(1) # Crear una ventana donde graficar

plt.subplot(2,1,1)
# plt.xlabel("rf") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones interpoladas") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos

plt.plot(x,y,label = "Muestreo de puntos", marker="*", linestyle="", color="red")

rf2= np.arange(0.2,6.11,0.01) # red fina para elvaluar la funcion de interpolacion 
spl= splrep(x,y, k=3)
Pi2= splev(rf2,spl)
plt.plot(rf2,Pi2,label = "Funcion interpolada Splrep", marker="", linestyle="-", color="blue")

cof= np.polyfit(x,y,9) # coef del poli
rf= np.arange(0.2,6.11,0.01) # red fina para elvaluar la funcion de interpolacion 
Pi= np.polyval(cof,rf)
plt.plot(rf,Pi,label = "Funcion interpolada Polyfit", marker="", linestyle="-", color="yellow")
plt.plot(rf,np.sin(rf),label = "Funcion seno",marker="", linestyle="-", color="green") # Grafico t y f(t) y le pongo atributos

# plt.xlabel("rf") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones interpoladas") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos

plt.subplot(2,1,2)
dif=abs(Pi2-np.sin(rf2))
plt.plot(rf2,dif,label = "Funcion error polyfit",marker="", linestyle="-", color="green") # Grafico t y f(t) y le pongo atributos

dif2=abs(Pi-np.sin(rf))
plt.plot(rf,dif2,label = "Funcion error splrep",marker="", linestyle="-", color="blue") # Grafico t y f(t) y le pongo atributos

plt.xlabel("rf") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones del error absoluto") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
plt.show()

print("El maximo error encotrado es:",max(dif))
