import bs4
import numpy as np
import pandas as pd
from config.settings import DATA_DIRS
import requests

class Titanic:
    def t1(self, option):
        df = pd.read_csv(DATA_DIRS[0] + '\\train.csv')

        survived = df[df['Survived'] == 1][option].value_counts()
        dead = df[df['Survived'] == 0][option].value_counts()
        df2 = pd.DataFrame([survived, dead])
        df2.index = ['Survived', 'Dead']
        result = []
        for i in range(len(df2.columns)):
            d = {}
            d['name'] = np.str(df2.columns[i])
            d['data'] = df2.iloc[:, i].tolist()
            result.append(d)
        print(result)
        return result

    '''
        df2 = df.groupby(['Survived', option]).count()['Name']
        print(df2)
        data = [
            {'name': df2.index[0][1], 'data': df2[0].values.tolist()},
            {'name': df2.index[1][1], 'data': df2[1].values.tolist()}
        ]
        return data
        '''

class Galaxy:
    def g1(self):
        df = pd.read_csv(DATA_DIRS[0] + '\\spstat1.csv', encoding='euc-kr')
        print(df)

class Naver:
    def n1(self):
        df = pd.read_html('https://finance.naver.com/marketindex/?tabSel=materials#tab_section', encoding='euc-kr')
        print(df)
        print(type(df[2]))
        df2 = df[2].copy()
        df2['등락율'] = df2['등락율'].str.strip('%')
        df2_new = df2.astype({'등락율': float})
        print(df2_new['상품명'].values.tolist())
        print(df2_new['등락율'].values.tolist())


class Open:
    def o1(self, startDt, endDt):
        url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=mcKEnmW0EQ24rM1HQJ4JooYXupjA2kHSVKN9DNTY9ZLybkjNC4Mv8JofDeBXlEUoE578%2Fe8QT7K1LvM5Xp1JwQ%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startDt+'&endCreateDt='+endDt
        result = requests.get(url)
        response = result.text.encode('utf-8')
        xml_obj = bs4.BeautifulSoup(response, 'lxml-xml')
        rows = xml_obj.find_all('item')
        print(rows)
        print(np.float(rows[0].find('accDefRate').text))

        result = [] # 최종리스트
        nameList = [] # 컬럼명
        rowsLen = len(rows) # item의 개수

        for i in range(0, rowsLen):
            item = rows[i].find_all()
            itemData = []
            for j in range(0, len(item)):
                if i==0:
                    nameList.append(item[j].name)
                text = item[j].text
                itemData.append(text)
            result.append(itemData)

        data = pd.DataFrame(result, columns=nameList)
        print(data)
        return data


if __name__ == '__main__':
    # Open().o1('20210101','20210601')
    Naver().n1()