import pandas as pd

data = {'subject': ['math', 'comp', 'phys', 'chem'], 'score': [100, 95, 80, 90], 'students': [87, 39, 50, 72]}
df = pd.DataFrame(data, columns = ['subject', 'score', 'students', 'class'])
df.index = ['one', 'two', 'three', 'four']
print('#1', df, '\n')
print('#2', df.shape, df.shape[0], '\n')

df2 = pd.DataFrame(data)
new_df = df2.copy()
print('#3', df2, '\n')

df2.loc[df2.shape[0]] = ['korea', 80, 78]
print('#4', df2, '\n')

df2.loc['total'] = ['eng', 99, 89]
print('#5', df2, '\n')

df2['score2'] = [99, 88, 99, 77, 66, 44]
print('#6', df2, '\n')

del df2['subject']
print('#7', df2, '\n')

df3 = df2.drop('students', axis=1)
print('#8', df3, '\n')

df4 = df2.drop(['score', 'score2'], axis=1)
print('#9', df4, '\n')

df5 = df2.drop('total', axis=0)
print('#10', df5, '\n')

print('#11', new_df, '\n')
print('#12', new_df['score'].tolist(), '\n')
print('#13', new_df.loc[2].tolist(), '\n')
print('#14', new_df['score'].to_numpy(), '\n')