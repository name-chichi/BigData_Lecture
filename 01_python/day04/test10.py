# 사용자 정보를 입력 받아 데이터 베이스에
# CRUD(Create, Read, Update, Delete) 하는 프로그램 작성

def insert(id,pwd,name):
    print(id,pwd,name);
    print('Inserted Data ....');

def selectone(id):
    print('Selected One Data ....');
    return [id, 'pwdxx','jamesxx'];

def select():
    print('Selected Data ....');
    datas = [
                ['id01','pwd01','james1'],
                ['id02', 'pwd02', 'james2'],
                ['id03', 'pwd03', 'james3'],
                ['id04', 'pwd04', 'james4']
            ];
    return datas;
def update(id,pwd,name):
    print(id, pwd, name);
    print('Updated Data ....');
def delete(id):
    print(id);
    print('Deleted Data ....');

while True:
    cmd = input('Input Command(i,s,so,u,d,q)...');
    if cmd == 'q':
        print('bye');
        break;
    elif cmd == 'i':
        # 입력 하고자 하는 값을 입력 받는다.
        id = input('Input ID ..?');
        pwd = input('Input PWD ..?');
        name = input('Input NAME ..?');
        insert(id,pwd,name);
    elif cmd == 'u':
        id = input('Input ID ..?');
        pwd = input('Input PWD ..?');
        name = input('Input NAME ..?');
        update(id, pwd, name);
    elif cmd == 'd':
        id = input('Input ID ..?');
        delete(id);
    elif cmd == 's':
        users = select();
        for u in users:
            print(u);
    elif cmd == 'so':
        id = input('Input ID ..?');
        user = selectone(id);
        print(user);

print('End Program ...');




