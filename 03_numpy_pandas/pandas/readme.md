# pandas



## 실습1. Series

- pandas 라이브러리에는 기본적으로 2개의 주요 자료구조가 존재 : Series와 DataFrame
- Series는 1차원 배열, DataFrame은 2차원 배열

```python
import numpy as np
import pandas as pd

# python list
data = [1, 2, 3, 4, 5]

# numpy
ndata = np.array(data)

# series
pdata = pd.Series(data)
print(pdata[0])
print(pdata.values)
print(pdata.index)

pdata2 = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])
print(pdata2)
print(pdata2['C'])

# dic
data2 = {'name': 'kim', 'ko': 100, 'en': 90, 'ma': 80, 'si': 100}
pdata3 = pd.Series(data2)

pdata3.name = 'Score Name'
pdata3.index.name = 'Score Index name'
print(pdata3)
print(pdata3['name'])
print(pdata3.ko)
```

![pan1_01](md-images/pan1_01.JPG)



## 실습2. index

```python
import numpy as np
import pandas as pd

data = np.arange(0, 5)
print(data)

idx = ['b', 'a', 'c', 'e', 'd']
pdata = pd.Series(data, index=idx)
#print(pdata[pdata > 0])
print(pdata)

pdata2 = pdata.reindex(np.sort(np.array(idx)))
print(pdata2)

idx.append('x')
idx.append('y')
pdata3 = pdata.reindex(idx, fill_value=0)
print(pdata3)
print(np.average(pdata3))
```

![pan2_01](md-images/pan2_01.JPG)



## 실습3. DataFrame

```python
import pandas as pd

data1 = ['A', 2]
data2 = ['B', 4]

df1 = pd.DataFrame([data1, data2])
print(df1)

data = {
        'subject' : ['math', 'comp', 'phys', 'chem'],
        'score': [100, 90, 85, 95],
        'students': [94, 32, 83, 17]
}
df2 = pd.DataFrame(data)
print(df2)
print(len(df2))
print(df2.shape)
print(df2.shape[0])  # 행 정보
print(df2.shape[1])  # 열 정보

df3 = pd.DataFrame(df2, columns=['students', 'score', 'subject'])
print(df3)
print(df3['students'][2])
print(df3[df3['score'] > 90])

dic1 = {'math': {1: 80, 2: 90, 3: 100}, 'comp': {1: 90, 2: 100}}
df4 = pd.DataFrame(dic1)
print(df4)
```

![pan3_01](md-images/pan3_01.JPG)



## 실습4. numpy를 활용한 DataFrame

```python
import pandas as pd
import numpy as np

datas = np.random.randint(10, 100, (6, 4))
print(datas)
df = pd.DataFrame(datas)
df.columns = ['score1', 'score2', 'score3', 'score4']
df.columns = ['s1', 's2', 's3', 's4']
#df.index = pd.date_range('20210114', periods=6)
print(df)
```

![pan4_01](md-images/pan4_01.JPG)



## 실습5. DataFrame 인덱싱

- 행을 참조할 때는 `loc`함수를 이용
- `loc[행 이름]` 을 하면 해당 행에 있는 칼럼에 따른 값을 출력
- `loc[행 이름, 열 범위]` 를 하게 되면 해당 행에 있는 열 범위의 칼럼 값이 출력

```python
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
```

![pan5_01](md-images/pan5_01.JPG)



## 실습6. DataFrame 인덱싱2

- `iloc` 을 이용하면 인덱스 값을 이용하여 위치를 참조할 수 있다.
- `iloc[1]` : 1행의 값들 (두번째 행)
- `iloc[1:]` : 1행~의 값들 (두번째 행부터 마지막행 까지)

```python
import pandas as pd

data = {'subject': ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]}

df = pd.DataFrame(data)
df['score2'] = [90, 89, 98, 97]
print(df)
print(df.iloc[0:2, 1:3])

print('---------------------------')
print(df[['score', 'score2']])
print(df.loc[1, ['score', 'score2']])
print(df.loc[0:2, 'subject':'students'])
```

![pan6_01](md-images/pan6_01.JPG)



## 실습7. DataFrame 인덱싱3

- 논리형 인덱싱이 가능하다

```python
import pandas as pd

data = {'subject': ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]}

df = pd.DataFrame(data)

print(df)

df2 = df[df['score'] > 90]
print(df2[['score', 'students']])

print(df.loc[df['score'] > 90, ['score', 'students']])

print('--------------------------------------------')
df3 = df.copy()
print(df3)
df3.loc[df3['score'] > 90, 'score'] = 200
print(df3)
```





## 실습 19. `groupby`

```python
import pandas as pd

df1 = pd.DataFrame(
    {
        '상품번호': ['p1', 'P1', 'p2', 'P2'],
        '수량': ['3,000', '2,000', '5,000', '6,000']
    }
)
print(df1, '\n')

df1['상품번호'] = df1['상품번호'].str.upper()   # 대문자 일괄처리
df1['수량'] = df1['수량'].str.replace(',', '')  # 천단위 일괄처리
df1 = df1.astype({'수량': float})
print(df1, '\n')

gdf1= df1.groupby(by=['상품번호'], as_index=False).sum()    # 상품번호로 그룹화 후 sum
print(gdf1, '\n')

gdf1= df1.groupby(by=['상품번호'], as_index=False).mean()   # 상품번호로 그룹화 후 mean
print(gdf1, '\n')

df1['고객번호'] = ['C1', 'C2', 'C2', 'C2']
print(df1, '\n')

new_df1 = df1.groupby(by=['고객번호', '상품번호'], as_index=False).count()  # 고객번호와 상품번호로 그룹화 후 count
print(new_df1)
```

![pan19_01](md-images/pan19_01-1624240116816.JPG)



## 실습 20. 타이타닉.csv

- 제공되는 타이타닉 정보를 csv파일로 읽어와 그룹화 및 분석 계산

![pan20_01](md-images/pan20_01.JPG)

```python
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
```

![pan20_02](md-images/pan20_02.JPG)