import matplotlib.pyplot as plt

'''
    This program will illustrate Pie Chart Usages.
    The example that will be used will be that of
    the calculation of percentages of how many slices
    three people eat in one sitting.
'''
PIZZASIZE = 8

slices = [2, 3, 1, 2]
names = ["Bob", "Sarah", "Mario", "Leftovers"]
colors = ["red", "cyan", "green", "m"]

plt.pie(slices,labels=names, colors=colors,startangle=90,shadow=True,explode=(0,0,1,0), autopct="%1.1f%%")

plt.title("The Amount of Pizza Slices Eaten Between Bob, Sarah and Mario")
plt.show()