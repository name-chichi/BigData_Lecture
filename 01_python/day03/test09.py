import random

print('start....');

num = random.randint(1,10);

while True:
    cmd = input('Input Number(q:exit) .. ');
    if cmd == 'q':
        print('bye');
        break;
    else:
        int_num = int(cmd);
        if int_num == num:
            print('OK');
        else:
            print('Fail');

print('end....');