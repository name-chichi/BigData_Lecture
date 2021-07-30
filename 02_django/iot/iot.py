import time
import random
from urllib import request

import bs4 as bs4

while True:
    url = 'http://127.0.0.1:8000/iots?'
    speed = str(random.randint(1, 200))
    rpm = str(random.randint(0, 3000))
    temp = str(random.randint(0, 100))
    url += 'speed='+speed+'&'
    url += 'rpm='+rpm+'&'
    url += 'temp='+temp
    target = request.urlopen(url)
    result = bs4.BeautifulSoup(target, 'html.parser')
    if result.select_one('h1').string != 'OK':
        break
    time.sleep(3)
