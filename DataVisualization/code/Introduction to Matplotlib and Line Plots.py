import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import sys

#Let's download and import our primary Canadian Immigration dataset using pandas read_excel() method. Normally, before we can do that, we would need to download a module which pandas requires to read in excel files. This module is xlrd.
df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print ('Data read into a pandas dataframe!')
#Let's view the top 5 rows of the dataset using the head() function.
print(df_can.head())
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10) 
#We can also veiw the bottom 5 rows of the dataset using the tail() function.
print(df_can.tail())