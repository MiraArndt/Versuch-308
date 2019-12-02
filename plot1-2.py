import matplotlib.pyplot as plt
import numpy as np
import csv

x2=np.genfromtxt("KSpule.csv", delimiter=",",unpack=True,usecols=0)
y2=np.genfromtxt("KSpule.csv", delimiter=",",unpack=True,usecols=1)


plt.plot(x2,y2,'r.')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')

plt.savefig('build/plot1-2.pdf')