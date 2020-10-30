# Load relevant modules
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import numpy as np

from matplotlib import rcParams
rcParams["font.size"] = "12"
rcParams['figure.figsize'] = 8, 8

x = 0
y = 0

rcParams['figure.figsize'] = 5, 5

plt.plot(x,y,'r.-')
plt.axis('equal')
plt.show()

def ensemble_stat(j,n,move):
    xa=np.zeros(int(j))
    ya=np.zeros(int(j))
    ra=np.zeros(int(j))
    for i in range(int(j)):
        thetas = (2*np.pi) * np.random.rand(n)
        dx = move * np.cos(thetas)
        dy = move * np.sin(thetas)
        print(dx)
        print(dy)
        end_x = np.sum(dx)
        end_y = np.sum(dy)
        (xa[i],ya[i])= end_x,end_y
        ra[i]=np.sqrt(xa[i]**2+ya[i]**2)
    return(xa,ya,ra)

# number of movements
n = 100

# time
t = 100
timestep = 0.1

# number of iterations
j = int(t/timestep)

# length of move
move = 5

(xa,ya,ra) = ensemble_stat(j,n,move)

rcParams["font.size"] = "10.5"
rcParams['figure.figsize'] = 8, 8

plt.subplot(2,2,1)
plt.plot(xa,ya,'.')
plt.axis('equal')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("End positions $(x,y)$")

plt.subplot(2,2,2)
plt.hist(xa, int(np.sqrt(n)))
plt.xlabel("$x$")
plt.title("Histogram of $x$")

plt.subplot(2,2,4)
plt.hist(ya, int(np.sqrt(n)))
plt.xlabel("$y$")
plt.title("Histogram of $y$")

plt.subplot(2,2,3)
plt.hist(ra, int(np.sqrt(n)))
plt.xlabel("$r = \sqrt{x^2+y^2}$")
plt.title("Histogram of mean squared displacement $r$")

plt.tight_layout()
plt.show()

#plt.savefig("polymer_stats.pdf")

rcParams["font.size"] = "12"
rcParams['figure.figsize'] = 5, 5

iterations = 100
t_list = [1,5,10,20,50,100,200,500,1000]
j_list = np.divide(t_list, timestep) 
nval = len(j_list)

r = []
x_axis = []

for i in range(5):
    for j in j_list:
        (xa,ya,ra) = ensemble_stat(j, n, move)
        r.append(np.mean(ra))
        x_axis.append(j)
        
plt.plot(x_axis, r, 'bo')
plt.xlabel("$ t/timestep$")
plt.ylabel("$ r_g = \sqrt{< r^2 >}$")
plt.show()