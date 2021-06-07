import math as m
import statistics as s
import time

print(m.sqrt(2));

data = [10,20,30,88,99,22,44];
print(s.median(data));

now = time.localtime()
print(now.tm_year,now.tm_mon);

start = time.time();
for i in range(1,10):
    time.sleep(1);
end = time.time();

print(end - start);





