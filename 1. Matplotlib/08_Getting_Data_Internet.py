import matplotlib.pyplot as plt
import pandas as pd

def graphData(someStock):
    stockPriceURL = 'https://pythonprogramming.net/yahoo_finance_replacement'
    sourceCode = pd.read_csv(stockPriceURL)
    sourceCode["Date"] = pd.to_datetime(sourceCode["Date"],format="%Y-%m-%d")

    plt.plot(sourceCode["Date"],sourceCode["Close"],"-",label="Prices")
    plt.xlabel("Date")
    plt.ylabel("Stock Market Prices")
    plt.title(someStock + " Stock Market Prices per Date")
    plt.legend()
    plt.show()

graphData("Order 66")