#A box plot is a way of statistically representing the distribution of the data through five main dimensions:

    #Minimun: Smallest number in the dataset.
    #First quartile: Middle number between the minimum and the median.
    #Second quartile (Median): Middle number of the (sorted) dataset.
    #Third quartile: Middle number between median and maximum.
    #Maximum: Highest number in the dataset.
#To make a box plot, we can use kind=box in plot method invoked on a pandas series or dataframe.
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt
df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print ('Data read into a pandas dataframe!')
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

# let's rename the columns so that they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
# for sake of consistency, let's also make all column labels of type string
df_can.columns = list(map(str, df_can.columns))
years = list(map(str, range(1980, 2014)))
# set the country name as index - useful for quickly looking up countries using .loc method
df_can.set_index('Country', inplace=True)
# to get a dataframe, place extra square brackets around 'Japan'.
df_japan = df_can.loc[['Japan'], years].transpose()
