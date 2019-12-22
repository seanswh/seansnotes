import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import sys

#Let's download and import our primary Canadian Immigration dataset using pandas read_excel() method. Normally, before we can do that, we would need to download a module which pandas requires to read in excel files. This module is xlrd.
df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print ('Data read into a pandas dataframe!')
#basic functions

#Let's view the top 5 rows of the dataset using the head() function.
print(df_can.head())
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10) 
#We can also veiw the bottom 5 rows of the dataset using the tail() function.
print(df_can.tail())
#When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe. We can do this by using the info() method.
df_can.info()
#To get the index and columns as lists, we can use the tolist() method.

print(df_can.columns.tolist())
print(df_can.index.tolist())
print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))
#To get the list of column headers we can call upon the dataframe's .columns parameter.
print(df_can.columns.values)

#Let's clean the data set to remove a few unnecessary columns. We can use pandas drop() method as follows:
# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))
#Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

#We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:
df_can['Total'] = df_can.sum(axis=1)
#We can check to see how many null objects we have in the dataset as follows:
print(df_can.isnull().sum())
#Finally, let's view a quick summary of each column in our dataframe using the describe() method.
print(df_can.head(2))
print(df_can.describe())

#higher usage

print(df_can.Continent)

#Let's try filtering on the list of countries ('OdName') and the data for years: 1980 - 1985.
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.