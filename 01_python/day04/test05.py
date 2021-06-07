# 함수명:  calc
# 숫자 2개와 연산자(+,-,/,*) 3개를 함수로 전달하여
# 결과를 return 하는 함수를 구현 하시오

# '+', 10,20
def calc(op,*n):
    result = 0;
    if op == '+':
        result = n[0] + n[1];
    elif op == '-':
        result = n[0] - n[1];
    elif op == '/':
        result = n[0] / n[1];
    elif op == '*':
        result = n[0] * n[1];
    else:
        result = 0;
    return result;

num1 = input('Input num1 ...');
num2 = input('Input num2 ...');
op = input('Input op ...');

data = calc(op, int(num1),int(num2));
print(data);


