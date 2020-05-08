## Module import and boilerplate
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

## Class and function definitions
def distance(pt, center=(0,0)):
    """Measures distance from point 'pt' to (x_c,y_c)
    pt: tuple of (x,y)
    return: float - distance
    """
    dx, dy = np.subtract(pt, center)
    return np.sqrt(dx**2 + dy**2)

def random_tuple(r, size=2):
    """Generates a random tuple of floats with of size 'size'
    with elements in the interval [-r,r)
    r: half-range of interval
    size: number of elements
    return: res - tuple of floats
    """
    while True:
        res = np.random.random(size) * -2*r + r
        yield res

def derive_pi(r=1):
    """Derives pi through random point counting.

    r: radius of circle
    n: number of iterations of random point generation
    return: tuple of
        i - number of iterations
        pi - approxiamtion of value of pi
        x - random x val
        y - random y val
    """
    within_r = 0
    tup = random_tuple(r)
    for i in itertools.count(1):
        x,y = next(tup)

        if distance((x,y)) < r:
            within_r += 1

        pi = (4 * within_r) / i
        yield i, pi, x, y

def init():
    """Initialize axes properties for animation."""
    ax.set_ylim(1,5)
    ax.set_xlim(0, 100)
    ax2.set_xlim(-r,r)
    ax2.set_ylim(-r,r)
    ax2.set_aspect('equal','box')
    del xdata[:]
    del ydata[:]
    del xdata2[:]
    del ydata2[:]
    line.set_data(xdata, ydata)
    points.set_data(xdata2, ydata2)
    return line, points

def run(data):
    # update the data
    i, pi, x_pt, y_pt = data
    xdata.append(i)
    ydata.append(pi)
    xdata2.append(x_pt)
    ydata2.append(y_pt)
    xmin, xmax = ax.get_xlim()

    # resize x axis when data exceeds existing axis
    if i >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()

    line.set_data(xdata, ydata)
    points.set_data(xdata2, ydata2)

    return line,points

r = 2
theta = np.linspace(0,2 * np.pi)

fig, [ax, ax2] = plt.subplots(2)
line, = ax.plot([],[],linewidth=2, label='Pi approximation')
line2, = ax.plot([0,10000],[3.14,3.14],'k--')
points, = ax2.plot([],[],'r.', label='Points')
circle, = ax2.plot(r * np.cos(theta), r * np.sin(theta))

xdata, ydata = [], []
xdata2, ydata2 = [], []
ani = FuncAnimation(fig, run, derive_pi(r), blit=False, interval=10,
                               repeat=False, init_func=init)
plt.show(block=True)
