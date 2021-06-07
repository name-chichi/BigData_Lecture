def score(name, *s, **option  ):
    """ 이함수는 이름, 점수, 평균여부를 입력 하세요 """
    print(name);
    sum = 0;
    for i in s:
        sum += i;
    print(sum);
    if option['avg'] == True:
        print(sum/len(s));

score('LEE',88,99,100,68,avg=True);
print('--------------------------');
score('KIM',88,99,100,avg=False);