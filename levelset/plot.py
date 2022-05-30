import numpy as np
import matplotlib.pyplot as plt


def myfunc(x):
    if x<=1:
        return 1/(2*np.pi)*np.sin(2*np.pi*x)
    else:
        return x-1

x = np.arange(0, 2, 0.01)
print(x)
y = [myfunc(xx)/xx for xx in x]
plt.axhline(y=0, linewidth=1.5, linestyle="--", color="grey")
plt.plot(x, y)
plt.savefig("./dd.png", dpi=500)
plt.show()