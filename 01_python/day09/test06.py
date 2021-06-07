from urllib import *;
from urllib import request

import bs4;

target = request.urlopen('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108');
soup = bs4.BeautifulSoup(target,'html.parser');

for st in soup.select('location'):
    province = st.select_one('province').string;
    city = st.select_one('city').string;
    for data in st.select('data'):
        tmEf = data.select_one('tmEf').string;
        wf = data.select_one('wf').string;
        tmn = data.select_one('tmn').string;
        tmx = data.select_one('tmx').string;
        print('%s,%s,%s,%s,%s,%s' % (province,city,tmEf,wf,tmn,tmx));