import matplotlib.pyplot as plt

'''
    Scatter Plots: Graphs used to show some relationship
    between two (2) or more variables; these being, for
    example: x, y, t (time) and z.

    An example of the application for this type of graphs
    is the following:
        a. Age vs Desease Mortality Rate
        b. Type of vehicle vs Fuel Efficiency Rate
'''

colonlyTechAge = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
numberAndroids = [0, 0, 1, 1000, 700, 29, 0, 0, 10, 100, 100]

plt.scatter(colonlyTechAge, numberAndroids, label="Number of Adroids per a Colony Tech Age", marker="p")    # To make marker a pentagon

plt.xlabel("A Colony Technological Age")
plt.ylabel("Number of Androids Constructed")
plt.title("Number of Androids Constructed per a Colony's Technological Age")
plt.legend()
plt.show()