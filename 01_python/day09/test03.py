import sys;
sys.path.append('c:\\mylib');

# import mypackage.p1.report;
from mypackage.p1.report import *;

st1 = 'abcvADGVaaa';

print(reportA(st1));
print(reportB(st1));