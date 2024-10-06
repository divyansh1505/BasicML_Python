import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

labels = ['a', 'b', 'c']
values = [1,4,2]

bars = plt.bar(labels, values)

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))


plt.show()