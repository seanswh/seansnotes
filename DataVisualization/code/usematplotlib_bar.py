import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
##A bar plot is a way of representing data where the length of the bars represents the magnitude/size of the feature/variable. Bar graphs usually represent numerical and categorical variables grouped in intervals.
#To create a bar plot, we can pass one of two arguments via kind parameter in plot():
  #kind=bar creates a vertical bar plot
   #kind=barh creates a horizontal bar plot
   #Vertical bar plot
    #In vertical bar graphs, the x-axis is used for labelling, and the length of bars on the y-axis corresponds to the magnitude of the variable being measured. Vertical bar graphs are particuarly useful in analyzing time series data. One disadvantage is that they lack space for text labelling at the foot of each bar.
df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print ('Data read into a pandas dataframe!')
df_can.columns = list(map(str, df_can.columns))
years = list(map(str, range(1980, 2014)))
#Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.set_index('Country', inplace=True)
df_iceland = df_can.loc['Iceland',years]
# step 2: plot data
df_iceland.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot


#Let's annotate this on the plot using the annotate method of the scripting layer or the pyplot interface. We will pass in the following parameters:
    #s: str, the text of annotation.
    #xy: Tuple specifying the (x,y) point to annotate (in this case, end point of arrow).
    #xytext: Tuple specifying the (x,y) point to place the text (in this case, start point of arrow).
    #xycoords: The coordinate system that xy is given in - 'data' uses the coordinate system of the object being annotated (default).
    #arrowprops: Takes a dictionary of properties to draw the arrow:
    #arrowstyle: Specifies the arrow style, '->' is standard arrow.
    #connectionstyle: Specifies the connection type. arc3 is a straight line.
    #color: Specifes color of arror.
    #lw: Specifies the line width.
plt.annotate('',                      # s: str. Will leave it blank for no text
             xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',         # will use the coordinate system of the object being annotated 
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )

plt.annotate('2008 - 2011 Financial Crisis', # text to display
             xy=(28, 30),                    # start the text at at point (year 2008 , pop 30)
             rotation=72.5,                  # based on trial and error to match the arrow
             va='bottom',                    # want the text to be vertically 'bottom' aligned
             ha='left',                      # want the text to be horizontally 'left' algned.
            )
plt.show()