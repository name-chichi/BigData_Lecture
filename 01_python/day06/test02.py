datas = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
];
print(datas);
print(datas[0]);
print(datas[0][0:2]);

print('--------------------');

for d1 in datas:
    for d in d1:
        print(d);

print('--------------------');

for i in range(0,len(datas)):
    for j in range(0,len(datas[i])):
        print(datas[i][j]);