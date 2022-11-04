import pandas
import quandl

dataFrame = quandl.get("WIKI/GOOGL")

print(dataFrame.head())         # To see the data frame which is being worked on.

'''
    It is important to find relationships in the data frame (set)!
    
    In the following example, an albeit overall relationship between
    all the stock values is that they are adjusted. With that being said,
    a more specific relationship would be that of the High and Lows which 
    represent the volatility of the the stock prices for the day. The Open
    and Close values represent the starting and ending prices for the day of
    each stock.

    Since Linear Regression will process the data without taking note
    of the aformentioned relationships, the latter must be created.
'''
dataFrame = dataFrame[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
dataFrame["Adj. High-Low Percentage"] = (dataFrame["Adj. High"] - dataFrame["Adj. Low"]) / dataFrame["Adj. Low"] * 100
dataFrame["Adj. Close-Open Percentage (Percentage Change Per Day)"] = (dataFrame["Adj. Close"] - dataFrame["Adj. Open"]) / dataFrame["Adj. Open"] * 100

# Create a new data frame with the really wanted data
'''
    Of all the column names' Adj. Close is a feature given that it is required for computing the percentages at the end of the time frame.
    They only way for it to be a label, as it is understood, is in the case that it is used to predict future values, which is not.
'''
dataFrame = dataFrame[["Adj. Close", "Adj. High-Low Percentage", "Adj. Close-Open Percentage (Percentage Change Per Day)"]]
print(dataFrame.head())