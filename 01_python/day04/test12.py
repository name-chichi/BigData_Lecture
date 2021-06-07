st1 = 'jmlee@tonesol.co.kr';

print(len(st1));
print(st1.find('.'));
print(st1.rfind('.'));
print(st1.count('.'));

# 이메일 주소에서
# ID(jmlee)와 Domain(tonesol)만 추츨 하여 출력 하시오
id = st1[0:st1.find('@')];
domain = st1[st1.find('@')+1:st1.find('.')];
print(id);
print(domain);
