# 두개의 숫자를 입력 받는다.
# 두수 중 최대 값을 출력 하시오
num1 = int(input('Input num1..'));

num2 = int(input('Input num2..'));

# 두개의 숫자는 모두 한자리로 입력이 되어야 한다.
# 한자리가 아니면 프로그램 종료 시킨다.
# 음수로 입력해도 프로그램 종료 시킨다.



if not((num1 // 10) < 1 and (num2 // 10) < 1)  or (num1 < 0 or num2 < 0):
    print('bye');
    exit(0);

max = 0;
# 두개의 숫자의 큰값을 max 값에 넣는다.
# 두개의 숫자를 비교 한다.
# 큰수를 max 값에 넣는다.
if num1 == num2:
    max = num1;
elif num1 > num2:
    max = num1;
else:
    max = num2;
print(max);





sal = int(input('Input salary'));

asal = sal - (sal * 0.92);
print(asal)














