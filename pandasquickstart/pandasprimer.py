import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
A Primer on the Pandas Library

A quickstart guide to operate using the pd library quickly.
This is a primer: Refer to documentation for in-depth & niche testcases
"""

"""DATAFRAMES AND SERIES"""
# All construction methods: https://pandas.pydata.org/docs/user_guide/dsintro.html
# The core of pandas is the Dataframe and Series classes.

"""SERIES"""
# One dimensional array taking in any datatype (including n-dimensional arrays...)
# Conversion to numpy's ndarray is possible with Series.to_numpy()
someSeries = pd.Series(data=np.random.randn(10), index=tenIndex)
# Series is ndarray-like & py dict-like
someSeries[1]
# >>> returns data @ index=1
someSeries[11] = 404
# >>> sets data at index 11
def showSeries():
    print(someSeries.dtype)
    #.dtype is a numpy fn
    print(someSeries)
    someSeries += someSeries
    # Vector operation / series-level operations 
    print(someSeries)

"""DATAFRAME"""
# 2-Dimensional array (Table), like a SQL table or dict of series objects
# OPTIONAL BUT KEY ARGS: index (row label), columns (column label)
_d = {
    "Alpha" : pd.Series([1,2,3], index=['a','b','c']),
    "Bravo" : pd.Series([4,5,6,7,8], index=['b','c','d','e','f']),
    "Charlie" : pd.Series([7,5,2,1], index =['a','b','c','d'], name = 'C')
} # Building a df from a dict of series
someDataFrame = pd.DataFrame(_d)

# SELECTING, DELETING AND ADDING COLUMNS DEMONSTRATION
def dfAddSelectDelete():
    print("\nOriginal DataFrame: \n")
    print(someDataFrame)
    # Selection
    a = someDataFrame['Alpha']
    print("\nSELECT a specific row:")
    print(a)
    # Deletion
    someDataFrame.pop('Charlie') #this
    print("\nDeleting a column:")
    print(someDataFrame)
    # Addition & Slicing
    someDataFrame['B Slice'] = someDataFrame['Bravo'][2:5]
    print('\nAdding a slice of a column:')
    print(someDataFrame)
    # Addition (scalar)
    someDataFrame['foo'] = 'bar' 
    print("\nAdding a scalar value:")
    print(someDataFrame)
    # Insertion
    someDataFrame.insert(1, 'AlphaFlag', True)
    print('\nInserting a column:')
    print(someDataFrame)

"""I/O FUNCTIONALITY"""
# pd comes with an arsenal of filetype readers.
# Pick your poison: https://pandas.pydata.org/docs/user_guide/io.html
osudataframe = pd.read_csv("./OSUDATA.csv", index_col='s/no')
#print(osudataframe)

"""PLOTTING"""
# The focus of the primer. Plotting in pandas is slightly different than matplotlib

# BASIC GRAPHS 
# >>> a .plot() wrapper
def plotLineGraphs():
    # LINE GRAPHS
    osudataframe.plot(y='Rank')
    osudataframe.plot(y='NationalRank')
    plt.show()
def plotBarGraphs():
    osudataframe.plot.bar(y='MostPlays')
    plt.show()
def plotHistogram():
    osudataframe.plot.hist(y='PP', bins=20)
    plt.show()
def plotDensity():
    ppSeries = osudataframe['Rank']
    ppSeries.plot.density()
    plt.show()
def plotBox():
    tempDf = pd.DataFrame(osudataframe[['Level', 'Hitaccuracy']])
    tempDf.plot.box()
    plt.show()
def plotScatter():
    osudataframe.plot.scatter(x='PP', y='Level', color='red')
    plt.show()
