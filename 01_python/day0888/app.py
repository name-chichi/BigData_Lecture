# View 역할을 하는  Application
from itemdb import ItemDB
from itemvo import ItemVO

print('start ...');

idb = ItemDB('shop');
idb.makeTable();

while True:
    cmd = input('Input Command(i,d,u,s,sa,q)');
    if cmd == 'q':
        print('bye');
        break;
    elif cmd == 'i':
        print('Insert Name & Price');
        name = input('input name..');
        price = float(input('input price..'));
        item = ItemVO(0,name,price,'');
        idb.insert(item);
    elif cmd == 'd':
        print('Delete');
        id = int(input('input id..'));
        idb.delete(id);
    elif cmd == 'u':
        print('Update');
        id = int(input('input id..'));
        name = input('input name..');
        price = int(input('input price..'));
        item = ItemVO(id,name,price,'');
        idb.update(item);
    elif cmd == 's':
        print('Select');
        id = int(input('input id..'));
        ir = idb.select(id);
        print(ir);
    elif cmd == 'sa':
        print('Select All');
        irs = idb.selectall();
        for i in irs:
            print(i);

print('end ...');


