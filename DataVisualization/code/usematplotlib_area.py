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

df_can.columns = list(map(str, df_can.columns))
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_top5 = df_can.head()
years = list(map(str, range(1980, 2014)))
# transpose the dataframe !!!important
df_top5 = df_top5[years].transpose() 

df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
print(df_top5.index)
ax = df_top5.plot(kind='area',
             alpha = 0.25,
             stacked=False,
             figsize=(20, 10), # pass a tuple (x, y) size
             )

ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')

plt.show()