#range konusu matlabde oluyordu library olmadan ama pythonda numpy şart

#burada bir contour map'i hazırladım, Coursera Machine Learning'de gördüklerimi bu dosya altında deneyeceğim

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def f(x,y):
    return np.sin(x*y)
x = np.arange(0,1,.05)
print(x)

y = np.arange(0,10,.5)
print(y)

x,y = np.meshgrid(x,y)
z = f(x,y)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.contour3D(x,y,z,50,cmap='binary')
plt.show()
