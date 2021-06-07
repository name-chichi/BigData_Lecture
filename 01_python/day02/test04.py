# 두개의 숫자를 입력 받아 두수의 합을 구하고
# 홀수 인지 짝인 인지를 출력 하시오

num1 = input('input num1..?');
num2 = input('input num2..?');
sum = int(num1) + int(num2);
if  sum % 2 == 0:
     print('짝수');
else:
    print('홀수');