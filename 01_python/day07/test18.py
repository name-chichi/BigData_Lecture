import csv;
f = None;
try:
    f = open('num1.csv');
    data = csv.reader(f);
    print(type(data));
    print(data);
    for row in data:
        print(row);
except:
    print('File Not Found...');
finally:
    if f != None:
        f.close();
