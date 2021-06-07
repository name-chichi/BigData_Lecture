num1 = input('input num1..?');
num2 = input('input num2..?');
op = input('input op(+ - / *)..?');

result = 0;
if op == '+':
    result = int(num1) + int(num2);
if op == '-':
    result = int(num1) - int(num2);
if op == '/':
    result = int(num1) / int(num2);
if op == '*':
    result = int(num1) * int(num2);

print(result);