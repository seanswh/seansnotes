import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

##Line Pots (Series/Dataframe)
#A line chart or line plot is a type of plot which displays information as a series of data points called 'markers' connected by straight line segments. It is a basic type of chart common in many fields. Use line plot when you have a continuous data set. These are best suited for trend-based visualizations of data over a period of time.
#Let's start with a case study:
#In 2010, Haiti suffered a catastrophic magnitude 7.0 earthquake. The quake caused widespread devastation and loss of life and aout three million people were affected by this natural disaster. As part of Canada's humanitarian effort, the Government of Canada stepped up its effort in accepting refugees from Haiti. We can quickly visualize this effort using a Line plot:
df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print ('Data read into a pandas dataframe!')
# useful for plotting later on
years = list(map(str, range(1980, 2014)))
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)

#Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
#print(df_can.describe())

#Before we proceed, notice that the defaul index of the dataset is a numeric range from 0 to 194. This makes it very difficult to do a query by a specific country. For example to search for data on Japan, we need to know the corressponding index value.
#This can be fixed very easily by setting the 'Country' column as the index using `set_index()` method.
#df_can.set_index('Country', inplace=True)
#print(df_can.head(3))
#First, we will extract the data series for Haiti.
#haiti = df_can.loc['Haiti'] # passing in years 1980 - 2013 to exclude the 'total' column
#print(haiti.head())
