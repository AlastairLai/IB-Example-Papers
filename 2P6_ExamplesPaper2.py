import control as ctr
import numpy as np
import matplotlib.pyplot as plt

G1 = ctr.tf([22000],[1,22000])

fig1 = plt.figure()
mag, phase, omega = ctr.bode(G1)
fig1.set_size_inches(10,10)

G2 = ctr.tf([22000,0],np.convolve([1,300],[1,22000]).astype(float))
fig2 = plt.figure()
mag, phase, omega = ctr.bode(G2)

t1,y1 = ctr.step_response(G1)
fig3 = plt.figure()
plt.plot(t1,y1)
plt.grid()

t2,y2 = ctr.step_response(G2)
fig4 = plt.figure()
plt.plot(t2,y2)
plt.grid()

plt.show()