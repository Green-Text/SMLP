import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import os

def graphData(someData):

    fig = plt.figure(0,constrained_layout=True)
    grids = gridspec.GridSpec(1,1,fig)
    ax1 = fig.add_subplot(grids[0,0])

    sourceCode = pd.read_csv(os.path.join(os.path.dirname(__file__),"Files","Example_CSV_Layoffs.csv"))

    ax1.bar(sourceCode["country"],sourceCode["total_laid_off"])

    for labels in ax1.xaxis.get_ticklabels():
        labels.set_rotation(90)
   
    #   ax1.xaxis.label.set_color("cyan")
    #   ax1.yaxis.label.set_color("red")
   
    #   ax1.spines["left"].set_color("cyan")
    ax1.spines["right"].set_visible(False)
    ax1.spines["top"].set_visible(False)
    #   ax1.spines["left"].set_linewidth(5)

    ax1.tick_params(axis="x", colors="#444444")
    #   ax1.axhline(sourceCode["total_laid_off"][1])
    plt.xlabel("Country")
    plt.ylabel("Total Layoffs")
    plt.title(someData)
    plt.legend()
    plt.show()

graphData("Layoffs 2022 per Country")