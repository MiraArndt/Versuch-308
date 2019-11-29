import matplotlib.pyplot as plt
import numpy as np
import csv

x=np.genfromtxt("LSpule.csv", delimiter=",",unpack=True,usecols=0)
y=np.genfromtxt("LSpule.csv", delimiter=",",unpack=True,usecols=1)

x2=np.genfromtxt("KSpule.csv", delimiter=",",unpack=True,usecols=0)
y2=np.genfromtxt("KSpule.csv", delimiter=",",unpack=True,usecols=1)


x1=np.linspace(0,15.8)
y1=[(1000*300*0.8*4*np.pi*10**(-7))/0.158]*50
plt.subplot(2,1,1)
plt.plot(x,y,'r.')
plt.plot(x1,y1)
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')
plt.subplot(2,1,2)
plt.plot(x2,y2,'r.')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')

plt.tight_layout()
plt.savefig('build/plot1.pdf')

