import numpy as np
import matplotlib.pyplot as plt
import Metodos as met

fd= lambda t,y: -0.2*y
y0=10
h = 0.25
t,y = met.euler(fd,0,1,y0,h)
print(t)
print(y)
