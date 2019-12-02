import matplotlib.pyplot as plt
import numpy as np
import csv

x=np.genfromtxt("LSpule.csv", delimiter=",",unpack=True,usecols=0)
y=np.genfromtxt("LSpule.csv", delimiter=",",unpack=True,usecols=1)



x1=np.linspace(0,15.8)
y1=[(1000*300*0.8*4*np.pi*10**(-7))/0.158]*50

plt.plot(x,y,'r.')
plt.plot(x1,y1)
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')


plt.savefig('build/plot1-1.pdf')

