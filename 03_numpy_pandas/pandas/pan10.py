import pandas as pd
import numpy as np

data = {'subject': ['math', 'comp', 'phys', 'chem'], 'score': [100, 95, 80, 90], 'students': [87, 39, 50, 72]}
df = pd.DataFrame(data, columns = ['subject', 'score', 'students', 'class'])
print('#1', df, '\n')
#df['class'] = [1,2,3,4]
df2 = df.copy()
df2.index = ['a', 'b', 'c', 'd']
data = [5, 6, 7, 8]
ser1 = pd.Series(data)
ser1.index = df2.index
print('#2', ser1, '\n')

df2['class'] = ser1
print('#3', df2, '\n')

print('----------------------')
df2['pass'] = (df2['score'] >= 90)
df2['average'] = [96.4, np.NaN, 77.6, 98.0]
print('#4', df2, '\n')

df3 = df2.dropna()
print('#5', df3, '\n')

df4 = df2.fillna(value=0)
print('#6', df4)