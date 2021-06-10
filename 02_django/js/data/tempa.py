# https://data.kma.go.kr/ -> 기후통계분석 -> 기온분석 -> 20100101~20201231
import csv
import os


class Tempa:
    # 서울의 연평균을 구하시오
    def seoula(self):
        f = open('../ta.csv')
        data = csv.reader(f)
        tempa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for row in data:
            print(row)
            for i in range(2010, 2021):
                if i == int(row[0].split('-')[0]):
                    tempa[i - 2010] += float(row[2])
        for i in range(0, len(tempa)):
            tempa[i] = tempa[i] / 365
        print(tempa)
        return

    # 서울의 월평균 기온을 구하시오
    def seoulam(self, year, month):
        f = open('./ta.csv')
        data = csv.reader(f)
        htemp = []
        ltemp = []
        for row in data:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]):
                ltemp.append(float(row[3]))
                htemp.append(float(row[4]))
        datas = [
            {'name': '최고기온', 'data': htemp},
            {'name': '최저기온', 'data': ltemp}
        ]
        return datas


if __name__ == '__main__':
    Tempa().seoulam(2011, 1)