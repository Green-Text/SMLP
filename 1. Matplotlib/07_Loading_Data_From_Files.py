import matplotlib.pyplot as plt
import csv
import numpy as np
import os

'''
    Part 1: CVS Test
'''
id = []
data = []

with open(os.path.join(os.path.dirname(__file__),"Files","Example_CSV_Read_1 - Test.txt"), "r") as csvfile:
    plots = csv.reader(csvfile,delimiter=":")
    for row in plots:
        id.append(str(row[0]))
        data.append(str(row[1]))
    csvfile.close()

for i in range(0,len(data)):
    print(id[i] + "\t" + data[i])

xValues = []
yValues = []

with open(os.path.join(os.path.dirname(__file__),"Files","Example_CSV_Read_2 - Bank Account.txt"), "r") as csvfile:
    plots = csv.reader(csvfile,delimiter=":")
    for row in plots:
        xValues.append(int(row[0]))
        yValues.append(int(row[1]))
    csvfile.close()
print(xValues)
print(yValues)

plt.plot(xValues,yValues, label="Current Monetary Health of Bank Account")
plt.xlabel("Days")
plt.ylabel("Monetary Value in Dollars ($)")
plt.title("Monetary Health of a Bank Account for the Past 10 Days")
plt.legend()
plt.show()

'''
    Part 2: Numpy Test
'''

xValues, yValues - np.loadtxt(os.path.join(os.path.dirname(__file__),"Files","Example_CSV_Read_2 - Bank Account.txt"), delimiter=":", unpack=True)

plt.scatter(xValues,yValues, label="Current Monetary Health of Bank Account")
plt.xlabel("Days")
plt.ylabel("Current Monetary Value in Dollars ($)")
plt.title("Monetary Health of a Bank Account for the Past 10 Days")
plt.legend()
plt.show()
