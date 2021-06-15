import csv

import numpy as np
import matplotlib.pyplot as plt

class p230:
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

# 1. 전국의 영유아(5세이하)들이 가장 많이 사는 지역 구하시오
def p231(self):
    return


# 2. 서울에서 5년간 인구가 가장 많이 늘어난 구를 구하시오
def p232(self):
    return


if __name__ == '__main__':
    p230().p248('신도림')