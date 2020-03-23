Nama = ('ASMIYENI ISLAMIATI')
NIM = ('H061181012')

print(Nama)
print(NIM)

import math
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,0.1)
y = [i**4 - 6.4*i**3 + 6.45*i**2 + 20.538*i - 31.752 for i in x]

plt.plot(x,y,'r')
plt.grid(True)
plt.show()