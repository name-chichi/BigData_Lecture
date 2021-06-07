import csv
import os

datas = ['1','2',''];

sum = 0;
for d in datas:
    if d == None or d == '':
        continue;
    num = int(d);
    sum += num;
print(sum);

# 2020년 가장 추웠던 날과 더웠던 날이 언제 인지 출력 하시오
os.chdir('c:\\mydata');
f = open('ta_2021.csv');
data = csv.reader(f);
header = next(data);
print(header);
print('------------------------------');
max = 0.0;
max_date = '';
min = 999;
min_date = '';
for row in data:
    if max < float(row[-1]):
        max = float(row[-1]);
        max_date = row[0];
    if min > float(row[-2]):
        min = float(row[-2]);
        min_date = row[0];
print('%s, %.2f' % (max_date, max));
print('%s, %.2f' % (min_date, min));
f.close();
