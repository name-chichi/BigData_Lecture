import pandas as pd

df = pd.read_csv('titanic2.csv')
print('#1', df, '\n')

def t1(feature):
    survived = df[df['Survived'] == 1][feature].value_counts()  # 생존자
    dead = df[df['Survived'] == 0][feature].value_counts()  # 사망자
    print('#2', survived, '\n')
    print('#3', dead, '\n')

# t1('Sex')

# group 함수
print('#4', df.groupby('Survived').count(), '\n')
df2 = df.groupby(['Survived', 'Sex']).count()['Pclass']
print('#5', df2, '\n')
print('#6', df2[0].values, '\n')
print('#7', df2[0].values.tolist(), '\n')

# 클래스별 성별 생존율
df3 = df.groupby(['Pclass', 'Sex']).mean()
print('#8', df3, '\n')
print('#9', df3['Survived'], '\n')

# 10세 미만 데이터
df4 = df[df['Age'] < 10].groupby('Sex').count()
print('#10', df4, '\n')
df5 = df[(df['Age'] < 10) & (df['Age'] > 5)].groupby('Sex').mean()['Survived']
print('#11', df5)