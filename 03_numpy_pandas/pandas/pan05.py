import pandas as pd

data = {'subject': ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]}

print(data, '\n')

df = pd.DataFrame(data, columns=['subject', 'score', 'students', 'class'])

df['class2'] = [1, 2, 3, 4]
df.index = ['one', 'two', 'three', 'four']
print(df, '\n')
print(df.columns)
print(df.index, '\n')

print(df['subject'], '\n')
print(df.subject, '\n')

# df2 = df[['score','class2']]
# print(df2)

print(df[['subject', 'score']], '\n')

print(df.loc['two', 'score': 'class'], '\n')
print(df.loc['two', ['score', 'students', 'class2']], '\n')