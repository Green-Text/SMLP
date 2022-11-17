import matplotlib.pyplot as plt
import random
from matplotlib import style

style.use("dark_background")
fig = plt.figure(0, constrained_layout=True)

def create_plots(n):
    xs = []
    ys = []
    for i in range(n):
        x = i
        y = random.randrange(n)
        xs.append(x)
        ys.append(y)

    return xs, ys

'''
    Basic Subplot Syntax
'''
#   ax1 = fig.add_subplot(221)
#   ax2 = fig.add_subplot(222)
#   ax3 = fig.add_subplot(212)

'''
    Enhanced Subplot Syntax: The first parameter dictates the number of rows and columns that the subplot will have. In this case,
    it has 6 rows and 1 column. The second paramenter is the starting grid-point of the figure. Since rows span for 2 units, all
    row starting grids are additions of 2.
'''
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=2,colspan=1)
ax2 = plt.subplot2grid((6,1),(2,0),rowspan=2,colspan=1)
ax3 = plt.subplot2grid((6,1),(4,0),rowspan=2,colspan=1)

x, y = create_plots(25)
ax1.plot(x,y, label="First Plot Data")

x, y = create_plots(50)
ax2.plot(x,y,label="Second Plot Data")

x, y = create_plots(100)
ax3.plot(x,y,label="Third Plot Data")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Subplots Example")
plt.legend()
plt.show()