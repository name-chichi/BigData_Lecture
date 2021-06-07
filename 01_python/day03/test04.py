# 1~100 까지의 숫자 중 홀수의 합과 평균, 짝수의 합과 평균을 구하시오
sum=0
cnt=0
sum2=0
cnt2=0
for i in range(1,101):
    if i % 2 == 1:
        sum += i;
        cnt += 1;
    else:
        sum2 += i;
        cnt2 += 1;
print(cnt);
print(sum);
print(sum/cnt);
print(cnt2);
print(sum2);
print(sum2/cnt2);
print('-------------------------------');
# 1~1000 까지의 숫자 중
# 2의배수의 합과 평균,
# 3의배수의 합과 평균,
# 5의배수의 합과 평균
s = 0;
s2 = 0;
s3 = 0;
c = 0;
c2 = 0;
c3 = 0;
for i in range(1,101):
    if i % 2 == 0:
        s += i;
        c += 1;
    if i % 3 == 0:
        s2 += i;
        c2 += 1;
    if i % 5 == 0:
        s3 += i;
        c3 += 1;

print(s2/c2);
print(s2/c2);
print(s3/c3);
