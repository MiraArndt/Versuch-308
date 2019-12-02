import matplotlib.pyplot as plt
import numpy as np
import csv

x1=np.genfromtxt("Messung1.csv", delimiter=",",unpack=True,usecols=0)
y1=np.genfromtxt("Messung1.csv", delimiter=",",unpack=True,usecols=1)


plt.plot(x1,y1,'r.')
plt.xlabel(r'$x \,/\, \mathrm{cm}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')

plt.xlim(0,26)
plt.ylim(0,4)





plt.savefig('build/plot2-1.pdf')

