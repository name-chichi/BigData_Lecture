import csv

import numpy as np
import matplotlib.pyplot as plt

class p230:
    # 1. '신도림'지역과 인구 분포가 비슷한 지역을 찾으시오
    def p248(self, loc):
        f = open('age.csv')
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

        print(result_name)
        print(result)

        plt.plot(home2, label=loc)
        plt.plot(result, label=result_name)
        plt.legend()
        plt.show()
        return


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


    # 3. 서울에서 3년간(18~20) 인구가 가장 많이 늘어난 구를 구하시오
    #    연령구분 10세 0~100세 데이터 다운로드(전체시군구현황)
    #    후 총 인구수로 계산
    def p232(self):
        f = open('age3.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        max = 0
        loc = ''
        for row in data:
            rdata = int(row[27]) - int(row[1])
            if rdata > max:
                max = rdata
                loc = row[0]
        print(loc, max)
        return


if __name__ == '__main__':
    p230().p232()