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
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)

#Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
#print(df_can.describe())

df_can.set_index('Country', inplace=True)
#print(df_can.head(3))
#print(df_can.loc['Japan',list(range(1980,1985))])

#Column names that are integers (such as the years) might introduce some confusion. For example, when we are referencing the year 2013, one might confuse that when the 2013th positional index.
#To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.
df_can.columns = list(map(str, df_can.columns))

#First, we will extract the data series for Haiti.
#years = list(map(str, range(1980, 2014)))
#haiti = df_can.loc['Haiti',years] # passing in years 1980 - 2013 to exclude the 'total' column
#print(haiti)

#Also, let's label the x and y axis using plt.title(), plt.ylabel(), and plt.xlabel() as follows:
#haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
#haiti.plot(kind='line')
#plt.title('Immigration from Haiti')
#plt.ylabel('Number of Immigrants')
#plt.xlabel('Years')
# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
#plt.text(2000, 6000, '2010 Earthquake') # see note below
#plt.show() 

#get China and India Immigration
df_ci = df_can.loc[['China','India'],years]
print(df_ci.head())