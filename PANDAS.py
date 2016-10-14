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

#Boolean Indexing basically filtering values of a column based on conditions from another set of columns 
#Example listing all females who are not graduate and got a loan...............................status - uknown
data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]

#Apply returns some value after passing each row/column of a data frame with some function. The function can be both default or user-defined. For instance, here it can be used to find the #missing values in each row and column.
#status......uknown
#Create a new function: that returns if value is null
def num_missing(x):
  return sum(x.isnull())

#Applying per column: Displays it
print "Missing values per column:"
print data.apply(num_missing, axis=0) #axis=0 defines that function is to be applied on each column

#Applying per row:Displays
print "\nMissing values per row:"
print data.apply(num_missing, axis=1).head() #axis=1 defines that function is to be applied on each row

#The display in the above code is not really fancy very simple. 


























