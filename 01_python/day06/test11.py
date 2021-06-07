text = ''' Force Therapeutics received venture-capital funding to enhance its technology, but its small internal team needed expert assistance to move forward quickly without accruing technical debt. The application is coded in Python and Django, and the management team needed experts to review it, ensure proper coding, and identify areas of potential concern ''';

dic = dict();

for c in text:
    if c.isalpha() == False:
        continue;
    c = c.lower();
    if c not in dic:
        dic[c] = 1;
    else:
        dic[c] += 1;

print(dic);

# 가장 많이 나온 순서대로 정렬 하여 출력 하시오
sort_data = sorted(dic.values(),reverse=True);
print(sort_data);

key_data = list(dic.keys());
print(key_data);
key_data.sort();
print(key_data);

for c in key_data:
    print('%s %d'  % (c,dic[c]));

