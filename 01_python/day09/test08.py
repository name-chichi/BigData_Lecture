st = '1 + 2';
result = eval(st);
print(result);

st2 = '[1,2,3,4,5,6,7]';
print(type(st2));
st2 = eval(st2);
print(type(st2));

st3 = '''for i in range(5):print(i);''';
exec(st3);



