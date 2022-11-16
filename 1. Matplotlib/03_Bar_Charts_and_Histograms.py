import matplotlib.pyplot as plt
import random
'''
    Bar Graphs Testing Code
'''
x1 = [2, 4, 6, 8, 10]
y1 = [6, 7, 8, 4, 2]
x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x1,y1,label="Bar Graph Test #1", color="orange")
plt.bar(x2, y2, label="Bar Graph Test #2", color = "cyan")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Interesting Values")
plt.legend()
plt.show()

'''
    Histogram Testing Code
'''
POPSZIE= random.randint(1000,2000)
populationAges = []
bins_AgeRange = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0,POPSZIE):
    populationAges.append(random.randint(0,100))

plt.hist(populationAges,bins_AgeRange,histtype="bar",rwidth=0.80, label="Age Groups of Sample")
plt.xlabel("Popolutation Age Group")
plt.ylabel("Number of People in Age Group")
plt.title("Histogram of Popultation Ages")
plt.legend()
plt.show()
