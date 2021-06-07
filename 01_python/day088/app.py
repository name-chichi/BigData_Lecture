# View 역할을 하는  Application
from userdb import UserDB
from uservo import UserVO

print('start ...');

udb = UserDB('shop');
udb.makeTable();

while True:
    cmd = input('Input Command(i,d,u,s,sa,q)');
    if cmd == 'q':
        print('bye');
        break;
    elif cmd == 'i':
        print('Insert');
        id = input('input id..');
        pwd = input('input pwd..');
        name = input('input name..');
        user = UserVO(id,pwd,name);
        udb.insert(user);
    elif cmd == 'd':
        print('Delete');
        id = input('input id..');
        udb.delete(id);
    elif cmd == 'u':
        print('Update');
        id = input('input id..');
        pwd = input('input pwd..');
        name = input('input name..');
        user = UserVO(id,pwd,name);
        udb.update(user);
    elif cmd == 's':
        print('Select');
        id = input('input id..');
        ur = udb.select(id);
        print(ur);
    elif cmd == 'sa':
        print('Select All');
        urs = udb.selectall();
        for u in urs:
            print(u);

print('end ...');


