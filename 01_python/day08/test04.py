from value import Account

acc1 = Account(10000,3.2);
print(acc1);
acc1.balance = 99999999;
print(acc1);
print(acc1.getBalance());
print(acc1.getInterest());
acc1.setInterest(2.8);
print(acc1);