data = [1,2,3,4,5,6,7,8,9];

print(data[3]);
print(len(data));
print(data[2:5]);
print(data[2:]);
print(data[:5]);
print(data[0::2]);
print(data[1:]);

data[1:3] = [20,30,40];
print(data);

data[10:11] = [70,80]
print(data);

del data[1:3];
print(data);

data2 = [1,2,3,4,5];
data3 = [10,20,30];
data4 = data2 + data3;
print(data4);

print(data2 * 4);



d1 = [1,2,3,4,5];
temp = d1.copy();
del temp[2];

print(d1);
print(temp);






