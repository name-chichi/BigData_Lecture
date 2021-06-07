st1 = 'ABcd';
st2 = st1.upper();
print(st1, st2);
if 'b' in st1.lower():
    print(st1);

st3 = '   a bc    ';
print('['+st3.strip()+']');
print('['+st3.lstrip()+']');
print('['+st3.rstrip()+']');


st4 = '1-2-3-4';
sum = 0;
for c in st4.split('-'):
    sum += int(c);
print(sum);

st5 = '''안녕하세요 파이썬 교육 입니다.\n안녕하세요 파이썬 파이썬 교육 입니다.\n안녕하세요 파이썬 파이썬 파이썬 교육 입니다.''';

print(st5);

for c in st5.split():
    print(c);

print('-----------------');

sum = 0;
for line in st5.splitlines():
    sum += line.count('파이썬');
print(sum);








