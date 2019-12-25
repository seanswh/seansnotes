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
years = list(range(2008,2011))
df_can.set_index("")
df_iceland = df_can.loc['iceland',years]