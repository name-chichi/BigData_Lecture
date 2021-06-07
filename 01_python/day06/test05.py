# 숫자를 1개 입력 받는다.
# 1 ~ 9 까지의 숫자만 입력 받고 이외의 문자가 입력 되면 다시 시도 하게 한다.
# 1 ~ 9 까지의 숫자를 20개 Random 하게 생성(중복 허용)하여
# 입력 받은 수와 같은 수가 몇개 인지 개수를 출력 하시오
import random

while True:
    num = input('Input Number');
    if not(len(num) < 2) and not(num.isnumeric()):
        print('Try Again');
        continue;
    temp = [];
    while True:
        temp_num = random.randint(1,9);
        temp.append(temp_num);
        if len(temp) == 20:
            break;
    print(temp);
    print(temp.count(int(num)));









