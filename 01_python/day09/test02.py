import random
import sys

sys.path.append('c:\\mylib');
import mymodule;

a = random.randint(1,10);
print(a);

result = mymodule.calc(100,200);
print(result);