import numpy as np
import matplotlib.pyplot as plt


def myfunc(x):
    if x<=1:
        return 1/(2*np.pi)*np.sin(2*np.pi*x)
    else:
        return x-1

def ofunc(x):
    if x<=1:
        y = 1/(2*np.pi)**2*(1-np.cos(2*np.pi*x))
    else:
        y = 1/2*(x-1)**2

    return y 

x = np.arange(0, 2, 0.01)
print(x)
y = [myfunc(xx)/xx for xx in x]
yy = [ofunc(xx) for xx in x]
# plt.axhline(y=0, linewidth=1.5, linestyle="--", color="grey")
# plt.plot(x, y)
# plt.xlabel("$\\nabla \phi$")
# plt.ylabel("$D$")
# plt.savefig("./dd.png", dpi=500)
# plt.show()
plt.plot(x, yy)
plt.xlabel("$x$")
plt.ylabel("$p$")
plt.savefig("./p.png", dpi=500)
plt.show()