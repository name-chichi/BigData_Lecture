from value import Account

acc = None;
while True:
    cmd = input('input cmd(c,s,d,w,q)');
    if cmd == 'q':
        break;
    elif cmd == 'c':
        print('Create');
        balance = int(input('Input Balance..'));
        interest = float(input('Input Interest..'));
        acc = Account(balance,interest);
        print('Account Created ....');
    elif cmd == 's':
        print('Select');
        if acc != None:
            print(acc);
        else:
            print('Not Exist');
    elif cmd == 'd':
        print('Deposit');
        money = int(input('Input Money..'));
        acc.deposit(money);
        print('Completed...');
    elif cmd == 'w':
        print('Withdraw');
        money = int(input('Input Money..'));
        try:
            acc.withdraw(money);
        except ValueError as v:
            print(v.args[0]);
        print('Completed...');
print('Bye .. !!');
