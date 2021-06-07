data = [];
data.append(10);
data.append(20);
data.append(30);
data.insert(0,999);
data.append(30);
data.append(30);
data.append(40);
data.append(50);
data.remove(30);
del(data[2]);
data[1:3] = [];

print(data);