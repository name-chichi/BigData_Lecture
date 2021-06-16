import csv

import numpy as np
import matplotlib.pyplot as plt

from config.settings import DATA_DIRS


class P230:
    # 1. '신도림'지역과 인구 분포가 비슷한 지역을 찾으시오
    def p248(self, loc):
        f = open(DATA_DIRS[0] + '\\age.csv')
        data = csv.reader(f)
        next(data)
        home2 = []
        data = list(data)

        # 신도림의 연령별 비율
        for row in data:
            if loc in row[0]:
                home = np.array(row[3:], dtype=int)
                home2 = home / int(row[2].replace(',',''))

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
            # print(row[0], s)

        # print(loc)
        # print(home2.tolist())
        # print(result_name.split(' ')[1])
        # print(result.tolist())

        result = [
            {'name': loc, 'data': home2.tolist()},
            {'name': result_name.split(' ')[1], 'data': result.tolist()}
        ]
        # print(result)
        return result


    # 2. 서울시 영유아(5세이하)들이 가장 많이 사는 지역 구하시오
    def p231(self):
        f = open('age2.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        max = 0
        max_loc = ''
        for row in data:
            rdata = np.array(row[3:9], dtype=int)
            sumdata = np.sum(rdata)
            if sumdata > max:
                max = sumdata
                max_loc = row[0]
        print(max_loc, max)
        return

    def p2311(self):
        f = open(DATA_DIRS[0] + '\\age2.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        result = []
        for row in data:
            datas = []
            baby = np.array(row[3:9], dtype=int)
            babys = int(np.sum(baby))
            datas.append(row[0].split(' ')[1])
            datas.append(babys)
            result.append(datas)
        # print(result)
        return result


    # 3. 서울에서 5년간(15~20) 인구가 가장 많이 늘어난 구를 구하시오
    #    연령구분 10세 0~100세 데이터 다운로드(전체시군구현황) 후 총 인구수로 계산
    def p232(self):
        # 2020
        f = open(DATA_DIRS[0] + '\\age3.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)

        # 2015
        f2 = open(DATA_DIRS[0] + '\\age4.csv')
        data2 = csv.reader(f2)
        next(data2)
        data2 = list(data2)

        datas = []
        locs = []

        for i in range(0, len(data)):
            diff = int(data[i][27]) - int(data2[i][1])
            loc = data[i][0].split(' ')[1]
            datas.append(diff)
            locs.append(loc)

        result = {
            'locs': locs,
            'datas': datas
        }
        return result




if __name__ == '__main__':
    P230().p232()