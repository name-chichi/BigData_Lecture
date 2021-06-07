import random

temp1 = [];
temp2 = [];

for i in range(0,10):
    num = random.randint(1,10);
    if num not in temp1:
        temp1.append(num);

print(temp1);

while True:
    num = random.randint(1, 10);
    if num not in temp1:
        temp1.append(num);
    if len(temp1) == 10:
        break;
print(temp1);
