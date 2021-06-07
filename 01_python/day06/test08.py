dic = {'IE':28.5,'Fire':10.3,'Chrome':38.9};
print(type(dic));
print(len(dic));

print(dic['Fire']);
print(dic.get('Chrome'));
print('IE' in dic);

dic['IE'] = 29.5;
dic['EG'] = 10.3;
del dic['Fire'];
print(dic);
