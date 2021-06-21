import pandas as pd

data = {
    'name': ['james1', 'james2', 'james3', 'james4', 'james5'],
    'ko': [100, 90, 89, 99, 89],
    'en': [99, 91, 87, 89, 81],
    'ma': [80, 92, 88, 99, 87],
    'si': [99, 100, 87, 93, 86],
}

df = pd.DataFrame(data)
print(df, '\n')

# 1. 인덱스 값을 이름으로 변경 하시오
df.index = data['name']
print('#1', df, '\n')
del df['name']
print(df, '\n')

# 2. james3의 점수를 출력 하시오
print('#2', df.loc['james3'], '\n')
print(df.iloc[2], '\n')

# 3. ko 점수가 90점 이상인 학생의 정보를 출력 하시오
print('#3', df[df['ko'] > 90], '\n')
print(df.loc[df['ko'] > 90], '\n')

# 4. ko 점수가 90점 이상인 학생의 이름과 en 점수를 출력 하시오
print('#4', df.loc[df['ko'] > 90, 'en'], '\n')
print(df.loc[df['ko'] > 90, ['en', 'si']], '\n')

# 5. james4의 ma, si  점수만 출력 하시오
print('#5', df.loc['james4', ['ma', 'si']], '\n')
print(df.iloc[3, 2:4], '\n')

# 6.df를 df2 로 복사하여 en 점수가 90점 미만인 학생의 점수는 모두 90점으로 변경 하시오
df2 = df.copy()
df2.loc[df['en'] < 90, 'en'] = 90
print('#6', df2)