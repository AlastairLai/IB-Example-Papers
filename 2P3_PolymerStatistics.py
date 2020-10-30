# Load relevant modules
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import numpy as np

from matplotlib import rcParams
rcParams["font.size"] = "12"
rcParams['figure.figsize'] = 8, 8

def get_polymer_shape(nm, am):
    thetas = (2*np.pi) * np.random.rand(nm)
    dx = am * np.cos(thetas)
    dy = am * np.sin(thetas)
    x = np.add.accumulate(dx)
    y = np.add.accumulate(dy)
    return((x,y))

number_of_monomers = 100
monomer_length = 1.

(x,y)=get_polymer_shape(number_of_monomers, monomer_length)

rcParams['figure.figsize'] = 5, 5

plt.plot(x,y,'.-')
plt.plot([x[0]],[y[0]],'g*')
plt.plot([x[-1]],[y[-1]],'ro')
plt.axis('equal')
plt.show()

# uncomment this to save the figure
#plt.savefig("polymer_shape.svg")

def ensemble_stat(n, nm, am):
    xa=np.zeros(n)
    ya=np.zeros(n)
    ra=np.zeros(n)
    for i in range(n):
        (x,y)=get_polymer_shape(nm, am)
        (xa[i],ya[i])=(x[-1],y[-1])
        ra[i]=np.sqrt(xa[i]**2+ya[i]**2)
    return(xa,ya,ra)

# number of polymer configurations
n = 50000

(xa,ya,ra) = ensemble_stat(n, number_of_monomers, monomer_length)

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
plt.title("Histogram of end-to-end distance $r$")

plt.tight_layout()
plt.show()

#plt.savefig("polymer_stats.pdf")

rcParams["font.size"] = "12"
rcParams['figure.figsize'] = 5, 5

nm_list = [10,20,50,100,200,500,1000]
am_list = [1,2,5]
nval = len(nm_list)*len(am_list)

r = []
sqrtna = []

for n_m in nm_list:
    for a_m in am_list:
        (xa,ya,ra) = ensemble_stat(n, n_m, a_m)
        r.append(np.mean(ra))
        sqrtna.append(np.sqrt(n_m)*a_m)
        
plt.plot(sqrtna, r, 'bo')
plt.xlabel("$ \sqrt{n} a$")
plt.ylabel("$ r_g = \sqrt{< r^2 >}$")

# Add linear regression to the plot    
    
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(sqrtna,r)

print("<r>/sqrt(n)r = " + str(slope))

plt.plot([0,max(sqrtna)], [0, slope * max(sqrtna)], '--')
plt.show()
#plt.savefig("length_vs_mon_number.svg")