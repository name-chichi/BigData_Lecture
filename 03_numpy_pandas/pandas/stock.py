import pandas as pd

df = pd.read_html('https://finance.naver.com/sise/lastsearch2.nhn',
                  encoding='euc-kr')
stock = df[1].dropna()
stock.index = stock['순위']
del stock['순위']
print(stock)