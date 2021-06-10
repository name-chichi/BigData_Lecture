import json


class Adata:
    def aj011(self):
        data = [
            {'id': 'id01', 'pwd': 'pwd01', 'age': '10'},
            {'id': 'id02', 'pwd': 'pwd02', 'age': '20'},
            {'id': 'id03', 'pwd': 'pwd03', 'age': '30'},
            {'id': 'id04', 'pwd': 'pwd04', 'age': '40'},
            {'id': 'id05', 'pwd': 'pwd05', 'age': '50'},
        ]
        return data

    def aj02(self, type):
        data = []
        if type == 'a':
            data = [
                {'location': 'seoul', 'datas': [10, 20, 30, 40, 50]},
                {'location': 'gwangju', 'datas': [10, 20, 30, 40, 50]},
            ]
        else:
            data = [
                {'location': 'busan', 'datas': [11, 21, 31, 41, 51]}
            ]
        return data

    def aj03(self, country):
        data = []
        if country == 'SEOUL':
            data = [
                {'name': 'SEOUL', 'data': [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]},
            ]
        elif country == 'LONDON':
            data = [
                {'name': 'LONDON', 'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]},
            ]
        else:
            data = [
                {'name': 'TOKYO', 'data': [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]},
            ]
        return data



if __name__ == '__main__':
    '''
    result = Adata().aj011()
    json_result = json.dumps(result)
    print(json_result)
    '''
    result = Adata().aj02('a')
    json_result = json.dumps(result)
    print(json_result)