import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def graphData(someDataName):
    fig = plt.figure(0,constrained_layout=True)
    ax1 = fig.add_subplot(1,1,1)

    sourceCode = pd.read_csv(os.path.join(os.path.dirname(__file__), "Files", "Example_CSV_Accident_Data.csv"))
    
    daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    slightAccidentsN = [0,0,0,0,0,0,0]
    seriousAccidentsN = [0,0,0,0,0,0,0]

    for i in range(0, len(sourceCode)):
        if sourceCode["Accident_Severity"][i] == "Slight":
            if sourceCode["Day_of_Week"][i] == daysOfWeek[0]:
                slightAccidentsN[0] = slightAccidentsN[0] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[1]:
                slightAccidentsN[1] = slightAccidentsN[1] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[2]:
                slightAccidentsN[2] = slightAccidentsN[2] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[3]:
                slightAccidentsN[3] = slightAccidentsN[3] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[4]:
                slightAccidentsN[4] = slightAccidentsN[4] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[5]:
                slightAccidentsN[5] = slightAccidentsN[5] + 1
            else:
                slightAccidentsN[6] = slightAccidentsN[6] + 1 
        else:
            if sourceCode["Day_of_Week"][i] == daysOfWeek[0]:
                seriousAccidentsN[0] = seriousAccidentsN[0] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[1]:
                seriousAccidentsN[1] = seriousAccidentsN[1] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[2]:
                seriousAccidentsN[2] = seriousAccidentsN[2] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[3]:
                seriousAccidentsN[3] = seriousAccidentsN[3] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[4]:
                seriousAccidentsN[4] = seriousAccidentsN[4] + 1
            elif sourceCode["Day_of_Week"][i] == daysOfWeek[5]:
                seriousAccidentsN[5] = seriousAccidentsN[5] + 1
            else:
                seriousAccidentsN[6] = seriousAccidentsN[6] + 1 
    
    x = np.arange(len(daysOfWeek))
    width = 0.35
    rect1 = ax1.bar(x-width/2, slightAccidentsN, width, label="Number of Slight Accidents Per Day")
    rect2 = ax1.bar(x+width/2, seriousAccidentsN, width, label="Number of Serious Accidents Per Day")

    ax1.annotate("Bad News!",(x[4], slightAccidentsN[4]), xytext=(0.8, 0.9),textcoords="axes fraction", arrowprops=dict(facecolor="grey",color="grey"))
    ax1.text(x[4],slightAccidentsN[4]*0.95,"¯\_('.')_/¯")

    ax1.set_xticks(x,daysOfWeek)
    ax1.bar_label(rect1, padding=3)
    ax1.bar_label(rect2, padding=3)
    plt.xlabel("Day of the Week")
    plt.ylabel("Car Accident Severity")
    plt.title(someDataName)
    plt.legend()
    plt.show()

graphData("UK Road Collision Severities Per Given Week Day (With Sample Size of 2M+ Cases)")