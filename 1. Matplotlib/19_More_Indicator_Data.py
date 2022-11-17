import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

MA1, MA2 = 10, 30

def moving_average(values, windows):
    weights = np.repeat(1.0, windows) / windows
    smas = np.convolve(values, weights, "valid")
    return smas

def highMinusLows(highs,lows):
    return highs - lows

def graphData(someStock):

    fig = plt.figure(0,constrained_layout=True)
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    stockPriceURL = 'https://pythonprogramming.net/yahoo_finance_replacement'
    sourceCode = pd.read_csv(stockPriceURL)
    sourceCode["Date"] = pd.to_datetime(sourceCode["Date"],format="%Y-%m-%d")

    ax1.plot_date(sourceCode["Date"],sourceCode["Close"],"-")
    ax1.fill_between(sourceCode["Date"],sourceCode["Close"], sourceCode["Close"][0], label="Gains", where=sourceCode["Close"][0]<=sourceCode["Close"],facecolor="green", alpha=0.25)
    ax1.fill_between(sourceCode["Date"],sourceCode["Close"], sourceCode["Close"][0], label="Losses", where=sourceCode["Close"][0]>sourceCode["Close"],facecolor="red", alpha=0.25)

    ma1 = moving_average(sourceCode["Close"],MA1)
    ma2 = moving_average(sourceCode["Close"],MA2)
    start = len(sourceCode["Date"][MA2-1:])
    ax2.plot(sourceCode["Date"][-start:],ma1[-start:])
    ax2.plot(sourceCode["Date"][-start:],ma2[-start:])

    h_l = []
    for i in range(0,len(sourceCode["High"])):
        h_l.append(highMinusLows(sourceCode["High"][i], sourceCode["Low"][i]))
    ax3.plot(sourceCode["Date"], h_l, "-")

    ax1.grid(True)
    ax2.grid(True)
    ax2.grid(True)

    plt.xlabel("Date")
    plt.ylabel("Stock Market Prices")
    plt.title(someStock + " Stock Market Prices per Date")
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.18,top=1.0,right=0.94,wspace=0.2,hspace=0)
    plt.show()

graphData("Order 66")