import numpy as np

def euler(f,t0,tf,y0,h):
    m = int((tf - t0) / h)
    t=np.arange(t0,tf+h,h)
    y=np.zeros(len(t))
    y[0]=y0
    for k in range(m):
       y[k+1]=y[k]+h*f(t[k],y[k])
    return t,y

