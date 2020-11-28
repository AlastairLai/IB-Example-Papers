import matplotlib.pyplot as plt
import control as ctr
import numpy as np

zeta = 0.5
a = 2
G = ctr.tf([1],[1,(2*zeta),1,0])
fig1 = plt.figure()
mag, phase, omega = ctr.nyquist(G,[0.01,1000])
plt.grid()
fig2 = plt.figure()
mag, phase, omega = ctr.bode(G, np.geomspace(0.01,100,50))
plt.show()