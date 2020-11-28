import matplotlib.pyplot as plt
import control as ctr
import numpy as np
import math

counter = 0
Kmin = 0.09
K_p = 0.0910
kdrange = np.linspace(1,5,100)*Kmin
Tcrit = np.zeros(kdrange.size)
a,b = ctr.pade(0.4)
print(a,b)
sys1 = ctr.tf(a,b)
for kd in kdrange:
    s = ctr.tf('s')
    # G = ctr.tf([1121*math.exp(-s*0.4)*(K_p+s*kd)],[200*s**2*(1+s)])
    G = (1121*(K_p+s*kd))/(200*s**2*(1+s))*sys1
    gm, pm, Wcg, Wcp = ctr.margin(G)
    Tcrit[counter] = pm*(2*math.pi)/(360*0.88)+0.4
    counter += 1
fig1 = plt.figure()
plt.plot(kdrange,Tcrit)
plt.grid()
plt.show()
# help(ctr.tf)