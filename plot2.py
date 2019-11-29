import matplotlib.pyplot as plt
import numpy as np
import csv

x1=np.genfromtxt("Messung1.csv", delimiter=",",unpack=True,usecols=0)
y1=np.genfromtxt("Messung1.csv", delimiter=",",unpack=True,usecols=1)

x2=np.genfromtxt("Messung2.csv", delimiter=",",unpack=True,usecols=0)
y2=np.genfromtxt("Messung2.csv", delimiter=",",unpack=True,usecols=1)

x3=np.genfromtxt("Messung3.csv", delimiter=",",unpack=True,usecols=0)
y3=np.genfromtxt("Messung3.csv", delimiter=",",unpack=True,usecols=1)

plt.subplot(3,1,1)
plt.plot(x1,y1,'r.')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')

plt.xlim(0,26)
plt.ylim(0,4)

plt.subplot(3,1,2)
plt.plot(x2,y2,'r.')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')
plt.xlim(0,26)
plt.ylim(0,4)

plt.subplot(3,1,3)
plt.plot(x3,y3,'r.')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')
plt.xlim(0,26)
plt.ylim(0,4)
plt.tight_layout()



plt.savefig('build/plot2.pdf')

