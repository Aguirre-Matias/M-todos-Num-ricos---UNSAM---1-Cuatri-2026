import os
os.system('cls' if os.name == 'nt' else 'clear')
import numpy as np
import matplotlib.pyplot as plt

def euler(f,t0,tf,y0,h):
    m = int((tf - t0) / h)
    t=np.arange(t0,tf+h,h)
    y=np.zeros(len(t))
    y[0]=y0
    for k in range(m):
       y[k+1]=y[k]+h*f(t[k],y[k])
    return t,y

def Huen(f,t0,tf,y0,h):
    m = int((tf - t0) / h)
    t=np.arange(t0,tf+h,h)
    y=np.zeros(len(t))
    y[0]=y0
    for k in range(m):
      F1=f(t[k], y[k])
      F2=f(t[k]+h, y[k]+h*f(t[k], y[k]))  
      y[k+1]=y[k]+h/2*(F1+F2)
    return t,y

def RungeKutta(f,t0,tf,y0,h):
    m = int((tf - t0) / h)
    t=np.arange(t0,tf+h,h)
    y=np.zeros(len(t))
    y[0]=y0
    for k in range(m):
      F1=f(t[k], y[k])
      F2=f(t[k]+(h/2),F1*(h/2) + y[k])  
      F3=f(t[k]+(h/2),F2*(h/2) + y[k])
      F4=f(t[k]+h,y[k]+h*F3)
      y[k+1]=y[k]+(h/6)*(F1+2*F2+2*F3+F4)
    return t,y

