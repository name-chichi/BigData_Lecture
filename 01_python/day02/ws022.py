num1 = 10;
num2 = 21;
num3 = 8;

# 최대값
max = 0;
if num1 > num2:
    if num1 > num3:
        max = num1;
    else:
        max = num3;
else:
    if num2 > num3:
        max = num2;
    else:
        max = num3;

print(max);

# 최소값
min = 0;
if num1 < num2:
    if num1 < num3:
        min = num1;
    else:
        min = num3;
else:
    if num2 < num3:
        min = num2;
    else:
        min = num3;

print(min);












