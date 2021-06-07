st1 = 'python programming';
cnt = len(st1);
print(cnt);
print(st1.find('pro'));
print(st1.rfind('o'));
print(st1.index('t'));
print(st1.count('p'));
print(st1[0:6]);
result = ('pro' in st1);
print(result);


st2 = ' ';
st3 = '123';

print(st2.islower());
if st2.islower():
    print(st2.upper());

print(st2.isalpha(), st3.isalpha());
print(st2.isnumeric(), st3.isnumeric());
print(st2.isspace());

