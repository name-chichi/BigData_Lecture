Numpy

> 행렬이나 대규모 다차원 배열을 쉽게 처리할 수 있도록 지원하는 파이썬 라이브러리





## 3. 인구조사 실습

- '신도림' 지역의 인구와 가장 유사한 지역을 찾아보자!!

  

1. 데이터 수집

   - [행정안전부 - 연령별 인구현황](https://jumin.mois.go.kr/index.jsp)

   - ![numpy00](md-images/numpy00.JPG)

   - ![numpy01](md-images/numpy01.JPG)

   - csv.reader()한 데이터는 일반적인 리스트가 아니기 때문에 <u>한번 전체 for문으로 순회하면 데이터가 사라진다.</u> 그래서 reader를 하면 **list**형태로 바꿔주도록 하자!!

   - ```python
     import csv
     import numpy as np
     
     class p230:
         def p248(self, loc):
             f = open('age.csv')
             data = csv.reader(f)
             next(data)
             print(type(data))
             data = list(data)
             print(type(data))
     
     if __name__ == '__main__':
         p230().p248('신도림')
         
     ''' 출력 결과
     C:\Python\Python36\python.exe C:/PycharmProjects/03_numpy_pandas/numpan/p230.py
     <class '_csv.reader'>
     <class 'list'>
     '''
     ```

2. 데이터 처리

   - 2-1) '신도림' 지역의 연령별 비율 구하기

   - ```python
     # 신도림의 연령별 비율
     for row in data:
     	if loc in row[0]:
     		home = np.array(row[3:], dtype=int)
     		home2 = home / int(row[2].replace(',',''))
     ```

   - 2-2) 모든 지역의 연령별 비율 구하기

   - 2-3) '신도림' 지역과 '전지역'의 각 연령대 비율을 빼고 그 값이 가장 낮은 지역을 찾는다.

   - ```python
     # 모든 지역의 연령별 비율을 구한다.
     min = 987654321
     result = None
     result_name = None
     	for row in data:
     		away = np.array(row[3:], dtype=int)
             away2 = away / int(row[2].replace(',',''))
             s = np.sum(np.abs(home2 - away2))
             if  loc not in row[0] and s < min:
             	min = s
                 result = away2
                 result_name = row[0]
     ```

   - 2-4) 두 지역의 연령별 인구수를 pyplot 라이브러리를 이용하여 그래프로 시각화한다.

   - ```python
     plt.plot(home2, label=loc)
     plt.plot(result, label=result_name)
     plt.legend()
     plt.show()
     ```

3. 결과(출력 화면)

   - '경기도 하남시'가 '신도림' 지역과 가장 유사한 인구분포를 가지고 있다. 

   - ![numpy02](md-images/numpy02.JPG)
   - [소스코드](./p230.py)











