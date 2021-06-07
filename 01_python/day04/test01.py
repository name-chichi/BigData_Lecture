import random

def calc():
    a = 10;
    b = 20;
    result = a + b;
    return result;

def random_num():
    num = random.randint(1,10);
    return num;

def calcsum(s):
    result = 0;
    for i in range(1,10+1):
        result += i;
    return result;

sum = calc();
print(sum);
num = random_num();
print(num);
sum2 = calcsum(10);
print(sum2);



