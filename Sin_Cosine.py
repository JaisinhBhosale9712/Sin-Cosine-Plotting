import numpy as np
import matplotlib as mp
from matplotlib import pyplot
#import sympy as sp
t=np.arange(0,2*np.pi,0.1)
#t=np.arange(sp.sin(0), sp.sin(sp.pi/2),sp.sin(sp.pi), sp.sin(sp.pi*3/2))
print(t)
fig=pyplot.figure(1)
fig.add_subplot(2,1,1).margins(x=0)
ax=fig.add_subplot(2,1,1).spines['bottom']
ax.set_position('center')
ax1=fig.add_subplot(2,1,1).spines['right']
ax1.set_visible(False)
ax1=fig.add_subplot(2,1,1).spines['top']
ax1.set_visible(False)
pyplot.plot(t,np.sin(t),"y-")
pyplot.xlabel("Degrees(x)")
pyplot.ylabel("sin(x)")
pyplot.title("Sin Graph")
pyplot.xticks((0,np.pi/2,np.pi,np.pi*3/2,np.pi*2),[0,90,180,270,360])
pyplot.yticks((-1,0,1))


fig=pyplot.figure(1)
fig.add_subplot(2,1,2).margins(x=0)
ax=fig.add_subplot(2,1,2).spines['bottom']
ax.set_position('center')
ax1=fig.add_subplot(2,1,2).spines['right']
ax1.set_visible(False)
ax1=fig.add_subplot(2,1,2).spines['top']
ax1.set_visible(False)
pyplot.plot(t,np.cos(t),"y-")
pyplot.xlabel("Degrees(x)")
pyplot.ylabel("cos(x)")
pyplot.title("Cos Graph")
pyplot.xticks((0,np.pi/2,np.pi,np.pi*3/2,np.pi*2),[0,90,180,270,360])
pyplot.yticks((-1,0,1))
pyplot.show()

