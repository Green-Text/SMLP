import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
'''
    This program will continue from the 8th python program in regards to the various customizations that can
    be undertaken in matplotlib.
'''
def graphData(someStock):

    fig = plt.figure(0,constrained_layout=True)
    grids = gridspec.GridSpec(1,1,fig)
    ax1 = fig.add_subplot(grids[0,0])
    ax_YTicks = []

    stockPriceURL = 'https://pythonprogramming.net/yahoo_finance_replacement'
    sourceCode = pd.read_csv(stockPriceURL)
    sourceCode["Date"] = pd.to_datetime(sourceCode["Date"],format="%Y-%m-%d")

    ax1.plot_date(sourceCode["Date"],sourceCode["Close"],"-",label="Prices")
    ax1.fill_between(sourceCode["Date"],sourceCode["Close"], sourceCode["Close"][0], label="Gains", where=sourceCode["Close"][0]<=sourceCode["Close"],facecolor="green", alpha=0.25)
    ax1.fill_between(sourceCode["Date"],sourceCode["Close"], sourceCode["Close"][0], label="Losses", where=sourceCode["Close"][0]>sourceCode["Close"],facecolor="red", alpha=0.25)

    for labels in ax1.xaxis.get_ticklabels():
        labels.set_rotation(45)
    for i in range(0,int(ax1.get_yticks()[-1]),40):
        ax_YTicks.append(i)
    ax1.set_yticks(ax_YTicks)
    ax1.grid(True)
    ax1.xaxis.label.set_color("cyan")
    ax1.yaxis.label.set_color("red")
    
    plt.xlabel("Date")
    plt.ylabel("Stock Market Prices")
    plt.title(someStock + " Stock Market Prices per Date")
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.18,top=1.0,right=0.94,wspace=0.2,hspace=0)
    plt.show()

graphData("Order 66")