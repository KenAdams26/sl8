#8) Write a python program to find all null value in a given data set and remove them .
import pandas as pd
import numpy as np
d1 = {'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'], 
      'ID': [1, 2, 3, 4], 'Salary': [100, 200, np.nan, pd.NaT],
      'Role': ['CEO', None, pd.NaT, pd.NaT]}
df = pd.DataFrame(d1)
print(df)
# drop all rows with any NaN and NaT values
df1 = df.dropna()
print(df1)
