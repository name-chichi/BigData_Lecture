# 한개의 숫자를 입력 받아
# 3의 배수 이고 짝수이고 양수
# OK 그렇지 않으면  FAIL 을 출력 하시오

num = int(input('Input Number ..?'));

# 두자리 숫자만 입력을 받는다. 단 두자리 숫자가 아니면 프로그램 종료
# exit(0);

# 99 // 10 = 9
# 11 // 10 = 1
if not((num // 10) >= 1 and (num // 10) < 10):   # 1 ~ 9
    print('bye...........');
    exit(0);


if (num > 0) and (num % 3 == 0) and (num % 2 == 0):
    print('OK');
else:
    print('FAIL');

