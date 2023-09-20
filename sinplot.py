import matplotlib.pyplot as plt
import numpy as np

valor_pi = np.pi
x = np.linspace(0, 2*valor_pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
