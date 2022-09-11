import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def wave(val):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt((val/100)*X**2 + (val/100)*Y**2)
    Z = np.sin(R)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    
    ax.zaxis.set_major_formatter('{x:.02f}')
    
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.savefig('imgs/'+str(val)+'.jpg',dpi=1000)

for i in range(0,1000):
    wave(i)

