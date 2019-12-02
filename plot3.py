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

a=[-728.43,0]
b=[-75,131]

plt.plot(H[0:8],y[0:8],'r.',label='Neukurve')
plt.plot(H[9:29],y[9:29],'b.',label='Verringern des Magnetfeldes')
plt.plot(H[29:49],y[29:49],'c.', label='Erhöhen des Magnetfeldes')
plt.plot(a,b,'k-',label='Lineare Ausgleichsgerade')
plt.legend(loc='best',prop={'size':8})



plt.grid(axis='both')
plt.xlabel(r'$H \,/\, \mathrm{A\cdot m^{-1}}$')
plt.ylabel(r'$B \,/\, \mathrm{mT}$')


plt.savefig('build/plot3.pdf')

