print('start....');

while True:
    cmd = input('Input Command ..(q,i,d,u,s) ');
    if cmd == 'q':
        print('bye');
        break;
    elif cmd == 'i':
        print('Insert Data ...');
    elif cmd == 'd':
        print('Delete Data ...');
    elif cmd == 'u':
        print('Update Data ...');
    elif cmd == 's':
        y = input('Input year..');
        print(y, '   Select Data ...');
    else:
        print('Invalid Cmd .. Try again..');
print('end....');