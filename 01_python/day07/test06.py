def half(s):
    return s/2;

score = [40,80,50,70,90];

for s in map(half,score):
    print(s);

print('----------------');

#lambda 형식

for s in map(lambda x:x/2,score):
    print(s);