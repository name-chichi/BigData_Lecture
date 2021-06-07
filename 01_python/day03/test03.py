for i in range(1,13):
    if i % 2 == 1:
        print(i);

print('-----------------------');
# while loop 로 짝수달만 출력 하시오
s = 1;
while s < 13:
    if s % 2 == 0:
        print(s);
    s += 1;
print('---------------------------');
# 1~100까지의 숫자 중 홀수 이면서 3의 배수들의 합과 평균을 구하시오
sum = 0;
cnt = 0;
for j in range(1,101):
    if j%2 == 1 and j%3 == 0:
        sum += j;
        cnt += 1;
print(cnt);
print(sum);
print(sum/cnt);
print('---------------------------');
# while

s = 1;
sum2 = 0;
cnt2 = 0;
while s < 101:
    if s%2 == 1 and s%3 ==0:
        sum2 += s;
        cnt2 += 1;
    s += 1;

print(s-1);
print(cnt2);
print(sum2);
print(sum2/cnt2);



















