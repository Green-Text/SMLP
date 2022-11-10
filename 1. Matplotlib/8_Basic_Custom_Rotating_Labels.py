import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
'''
    This program will illustrate how to create many subplots graphs inside a given figure
'''
def graphData(someStock):

    fig = plt.figure(0,constrained_layout=True)
    grids = gridspec.GridSpec(2,2,fig)
    ax1 = fig.add_subplot(grids[0,0])
    ax2 = fig.add_subplot(grids[0,1])
    ax3 = fig.add_subplot(grids[1,0:])

    stockPriceURL = 'https://pythonprogramming.net/yahoo_finance_replacement'
    sourceCode = pd.read_csv(stockPriceURL)
    sourceCode["Date"] = pd.to_datetime(sourceCode["Date"],format="%Y-%m-%d")

    ax1.plot_date(sourceCode["Date"],sourceCode["Close"],"-",label="Prices")
    for labels in ax1.xaxis.get_ticklabels():
        labels.set_rotation(45)
    ax3.bar(sourceCode["Date"],sourceCode["Close"],label="Prices")
    for labels in ax3.xaxis.get_ticklabels():
        labels.set_rotation(45)
    plt.xlabel("Date")
    plt.ylabel("Stock Market Prices")
    plt.title(someStock + " Stock Market Prices per Date")
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.18,top=1.0,right=0.94,wspace=0.2,hspace=0)
    plt.show()

graphData("Order 66")