import csv

from config.settings import DATA_DIRS


class MyAnalysis:
    def wm(self,year,month):
        f = open('data/ta.csv');
        #f = open('../data/ta.csv');
        data = csv.reader(f);
        next(data);
        htemp = [];
        ltemp = [];
        for row in data:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]):
                ltemp.append(float(row[3]));
                htemp.append(float(row[4]));
        data = [{
            'name':'일별 최저 기온',
            'data':ltemp
        },{
            'name': '일별 최고 기온',
            'data': htemp
        }];
        return data;

    def localage(self, target):
        # f = open('data/age.csv', 'r', encoding='UTF-8')
        # f = open('../data/age.csv', 'r', encoding='UTF-8')
        f = open(DATA_DIRS[0] + '\\age.csv', 'r', encoding='UTF-8')
        data = csv.reader(f)
        next(data)
        cnt = []
        for row in data:
            if target in row[0]:
                for i in row[3:104]:    # 계 3~104, 남 106~207, 여 209~310
                    try:
                        cnt.append(int(i))
                    except:
                        cnt.append(int(i.replace(',','')))
        result = [{
            'name': 'Total',
            'data': cnt
        }]
        return result

    def genderage(self, target):
        # f = open('data/age.csv', 'r', encoding='UTF-8')
        # f = open('../data/age.csv', 'r', encoding='UTF-8')
        f = open(DATA_DIRS[0] + '\\age.csv', 'r', encoding='UTF-8')
        data = csv.reader(f)
        next(data)
        m = []
        f = []
        for row in data:
            if target in row[0]:
                for i in row[106:207]:  # 남
                    m.append(-int(i.replace(',','')))
                for i in row[209:310]:  # 여
                    f.append(int(i.replace(',','')))
        result = [
            {'name': 'male', 'data': m},
            {'name': 'fmale', 'data': f},
        ]
        return result

    def genderage2(self, target):
        f = open(DATA_DIRS[0] + '\\age.csv', 'r', encoding='UTF-8')
        data = csv.reader(f)
        next(data)
        m = 0
        f = 0
        for row in data:
            if target in row[0]:
                m = int(row[105].replace(',',''))
                f = int(row[208].replace(',',''))

        result = [
            {'name': 'Male', 'y': 100*(m/(m+f))},
            {'name': 'Fmale', 'y': 100*(f/(m+f))},
        ]
        return result


if __name__ == '__main__':
    '''
    result = MyAnalysis().wm(2010,8)
    print(result)
    '''

    '''
    result = MyAnalysis().localage('신도림')
    print(result)
    '''

    '''
    result = MyAnalysis().genderage('신도림')
    print(result)
    '''

    result = MyAnalysis().genderage2('신도림')
    print(result)