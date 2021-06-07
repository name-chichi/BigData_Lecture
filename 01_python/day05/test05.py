s = '-';
st1 = 'abcdefg';
result = s.join(st1);
print(result);

st2 = 'abc efg';
result2 = st2.replace(' ','');
print(result2);

print(st2.ljust(10));
print(st2.rjust(10));
print(st2.center(10)); #앞뒤 5개씩 공배 배치
