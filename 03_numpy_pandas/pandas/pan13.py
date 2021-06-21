import pandas as pd
import numpy as np

s1 = pd.date_range('20210114', periods=6)
print('#1', s1, '\n')

s1 = np.random.permutation(s1)
print('#2', s1, '\n')

s2 = list('DBCA') #['','','','']
y = pd.DataFrame(np.random.randint(0, 100, (6, 4)), index=s1, columns=s2)
print('#3', y, '\n')

y1 = y.sort_index(axis=0, ascending=False)
print('#4', y1, '\n')

y2 = y.sort_index(axis=1, ascending=False)
print('#5', y2, '\n')
print('---------------------------------')

y3 = y.sort_values(by='A', ascending=False)
print('#6', y3, '\n')

y['E'] = np.random.randint(0, 5, size=6)
print('#7', y, '\n')
print('#8', y['E'].unique(), '\n')
print('--------------------------------------')

yy = y.transpose()
print('#9', yy, '\n')
print('#10', yy.loc['E'].isin([2, 1]))