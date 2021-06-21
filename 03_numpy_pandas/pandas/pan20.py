import pandas as pd

t = pd.read_csv('titanic.csv')
print(t.shape)
print(t.columns)

# 등급별 인원
t1 = t.groupby(by=['pclass', 'sex'], as_index=False).count()
print(t1)

# 등급별 연령의 평균
t1 = t.groupby(by=['pclass', 'sex'], as_index=True).mean()['age']
print(t1)