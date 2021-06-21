import pandas as pd

df1 = pd.DataFrame({'a': [10, 11, 12, 13], 'b': [20, 21, 22, 23]}, index=[0, 1, 2, 3])
df2 = pd.DataFrame({'c': [32, 33, 34, 35], 'd': [42, 43, 44, 45]}, index=[2, 3, 4, 5])
print('#1', df1, '\n')
print('#2', df2, '\n')

df3 = df2.join(df1, how='left')
print('#3', df3, '\n')

df4 = pd.concat([df2, df1], axis=1)
print('#4', df4, '\n')