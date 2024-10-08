import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

#Resize your graph

# plt.figure(figsize=(2.5,1.5), dpi=300)

x = [0,1,2,3]
y = [0,2,4,6]

# could have written x, 2x instead of x and y too in plt.plot

plt.plot(x,y, label='2x', color='yellow', linewidth = 4, marker='.', markersize=20,
        linestyle='--', markeredgecolor="blue")

plt.title("MATPLOT", fontdict={'fontsize':20})
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6,8])

##Line number 2 

x2 = np.arange(0,4,0.5) #mtlb 0,0.5,1,1.5,2,2.5,3,3.5,4
plt.plot(x2, x2**2, 'red', label='x2')

plt.savefig('mygraph.png', dpi=1200)
plt.show()