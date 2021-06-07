import time


def gettime():
    now = time.localtime();
    return now.tm_hour, now.tm_min, now.tm_sec;

while True:
    data = gettime();
    print('%d시 %d분 %d초' % (data[0],data[1],data[2]) );
    time.sleep(1);