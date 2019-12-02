import matplotlib.pyplot as plt
import numpy as np
import csv


x3=np.genfromtxt("Messung3.csv", delimiter=",",unpack=True,usecols=0)
y3=np.genfromtxt("Messung3.csv", delimiter=",",unpack=True,usecols=1)


plt.plot(x3,y3,'r.')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')
plt.xlim(0,26)
plt.ylim(0,4)

plt.savefig('build/plot2-3.pdf')