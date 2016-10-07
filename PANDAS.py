# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:09:02 2016

@author: irayc
"""

import pandas as pd
#df = pd.read_csv("address") Reads the dataset in a dataframe using Pandas
#df.head(10) Printing first 10 rows of dataset\

#df.describe() Gets summary of numerical variables

#For non-numerical values we can look at the frequency distribution to understand if they make 
#sense or not. Produces Frequency Table
#df['non-numerical value'].value_counts()

#using df['column name'] is the normal way to access a column

#df.['column name'].hist(bins=50) bins are the distribution for y-axis
#above line makes a histogram : D 

dataframe = pd.read_csv("SampleDataSet.csv")

#creates histogram ......status-works
dataframe['Favorite Dice Number'].hist(bins=50)

#dataframe.describe() does not work

#displays first 10 rows of dataframe.........status-not working but no errors given
dataframe.head(10)

#creates a boxplot using data from column 'Favorite Dice Number' ..........status-works
dataframe.boxplot(column = 'Favorite Dice Number')

#creates a boxplot grouped by a criteria(League or Overwatch) .........status - works
dataframe.boxplot(column = 'Favorite Dice Number', by = 'League or Overwatch')
