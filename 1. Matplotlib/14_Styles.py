import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import pandas as pd
import os
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc

'''
    Make Graphs better; more user-friendly
'''

def graphData(someData):
        fig = plt.figure(0, constrained_layout=True)
        grids = gridspec.GridSpec(2,1, fig)
        ax1 = fig.add_subplot(grids[0,0])
        ax2 = fig.add_subplot(grids[1,0])

        sourceCode = pd.read_csv(os.path.join(os.path.dirname(__file__), "Files", "Example_CSV_ADP_DATA.csv"))
        startIndex = list(pd.DatetimeIndex(sourceCode["Date"]).year).index(2021)
        endIndex = list(pd.DatetimeIndex(sourceCode["Date"]).year).index(2022)
        
        sourceCode["Date"] = pd.to_datetime(sourceCode["Date"],format="%Y-%m-%d")   #    Convert to datetime format

        ax1.plot(sourceCode["Date"],sourceCode["Close"],label="Close Price")        # Fine
        
        ohcl = []
        while startIndex < endIndex:
            #   Candlestick_ohlc needs float as date; hence, using date2num to convert to epoch floating format
            append_me = mdates.date2num(sourceCode["Date"][startIndex]), sourceCode["High"][startIndex], sourceCode["Low"][startIndex], sourceCode["Open"][startIndex], sourceCode["Close"][startIndex], sourceCode["Volume"][startIndex]
            ohcl.append(append_me)
            startIndex = startIndex + 1
        candlestick_ohlc(ax2,ohcl, width=0.4,colorup="g",colordown="r")
        ax2.xaxis_date()
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))   # Don't want epoch format as dates; hence, converting back.

        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.title(someData)
        plt.legend()
        plt.show()

print(plt.style.available)
#   style.use("fast")
#   style.use("ggplot")
#   style.use("seaborn-v0_8-white")
#   style.use("seaborn-v0_8-poster")
#   style.use("_mpl-gallery")
#   style.use("bmh")
style.use("dark_background")
graphData("ADP Close Stock Price Data")