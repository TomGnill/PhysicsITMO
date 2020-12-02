import numpy as np
import matplotlib.pyplot as plt

a = [1, 1, 2, 2]
b = [2, 3, 1, 3]
delta = [np.pi / 4, np.pi / 2, 3 * np.pi /4, np.pi]
t = np.linspace(-np.pi, np.pi, 300)
fig, axs = plt.subplots(4, 4)
fig.suptitle('Lissajous curves')

for i in range (0,4):
 for j in range (0,4):
  x = np.sin(a[i]*t + delta[j])
  y = np.sin(b[i]*t)
  axs[i, j].plot(x, y)


plt.show()