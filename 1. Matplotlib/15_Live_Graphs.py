import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import os
from matplotlib import style

style.use("ggplot")

fig = plt.figure(0,constrained_layout=True)
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graphData = open(os.path.join(os.path.dirname(__file__),"Files","Example_Animate.txt"),"r").read()
    lines = graphData.split('\n')
    
    xs =[]
    ys = []
    for line in lines:
        if(len(line)>1):
            x, y = line.split(':')
            xs.append(float(x))
            ys.append(float(y))

    ax1.clear()
    ax1.plot(xs,ys,label="Animation")


ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()

