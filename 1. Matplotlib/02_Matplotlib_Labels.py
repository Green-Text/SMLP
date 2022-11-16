import matplotlib.pyplot as plt
import math

x =[]
y1 = []
y2 = []

def rangeWithFloats(start, stop, step):
    while start < stop:
        yield start
        start = start + step

for i in rangeWithFloats(-1,1,0.1):
    if i < 0:
        y2.append(0)
    else:
        y2.append(1)
    y1.append(1 - math.exp(i-1))
    x.append(i)
    
plt.plot(x,y1, label="Line of 1 - e^x")
plt.plot(x,y2, label="Line of Sqaure Signal Generator")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("X vs. Y Graph")
plt.legend()
plt.show()