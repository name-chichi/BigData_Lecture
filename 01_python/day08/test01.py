custid = '';
balance = 10000;

def deposit(m):
    global balance;
    balance += m;

def select():
    return balance;

result = select();
print(result);

deposit(500);
result = select();
print(result);