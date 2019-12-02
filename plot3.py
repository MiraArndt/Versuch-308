import matplotlib.pyplot as plt
import numpy as np
import csv

x=np.genfromtxt("Messwerte.csv", delimiter=",",unpack=True,usecols=0)
y=np.genfromtxt("Messwerte.csv", delimiter=",",unpack=True,usecols=1)
H=595/(2*np.pi*0.13)*x
Hrund=["%.0f" %elem for elem in H]
xrund=["%.0f" %elem for elem in x]
yrund=["%.0f" %elem for elem in y]

with open("tabelle1.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(xrund,yrund,Hrund))

plt.plot(H[9:29],y[9:29],'r.')
plt.plot(H[29:49],y[29:49],'k.')
plt.plot(H[0:8],y[0:8],'.')
plt.grid(axis='both')
plt.xlabel(r'$H \,/\, \mathrm{A\cdot m^{-1}}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')


plt.savefig('build/plot3.pdf')

