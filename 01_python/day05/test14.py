data = [10,20,30,30,30,40,50];

print(data.index(40));
print(data.count(30));

# 30을 모두 지우시오
for i in range(0,data.count(30)): # 0,1,2
    data.remove(30);

print(data);

print(sum(data));
print(sum(data)/len(data));
print(min(data));
print(max(data));

ss = '2020-04-03';
print(int(ss[ss.find('-')+1:ss.rfind('-')]));