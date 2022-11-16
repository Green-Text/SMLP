import matplotlib.pyplot as plt
import datetime as dt
import time as t
import numpy as np

'''
    This program will show the usage of the time, datetime and numpy libraries to convert date-stamps into
    the matplotlib format.
'''
currentTime = t.time()
print(currentTime)         # In Unix Time
print(dt.datetime.fromtimestamp(currentTime))       # Better readable format

datesUix = [1568113437, 1668113437, 1668117, 199995450, 100]
datesUix.sort()
eventProbability = [0, 0.50, 0.01, 1, 1]
matplotDatesConv = np.vectorize(dt.datetime.fromtimestamp)

plt.plot(matplotDatesConv(datesUix),eventProbability, label="Probability of Event")
plt.xlabel("Date")
plt.ylabel("Propbability")
plt.title("Event Probability At Given Dates")
plt.legend()
plt.show()

