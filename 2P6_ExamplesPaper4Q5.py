import matplotlib.pyplot as plt
import control as ctr
import numpy as np

T_d = 2
G = ctr.tf([0.5096*T_d,0.5096],[1,1,0,0])
fig1 = plt.figure()
plt.xlim(-2, 2)
plt.ylim(-2, 2)
mag, phase, omega = ctr.nyquist(G,[0.01,1000])
plt.grid()
fig2 = plt.figure()
mag, phase, omega = ctr.bode(G, np.geomspace(0.01,100,50))
plt.show()

# sys = ctr.nyquist(G,[0.01,1000])
# gm, pm, wg, wp = ctr.margin(sys)
# print(gm, pm)