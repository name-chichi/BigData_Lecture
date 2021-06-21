import pandas as pd

df = pd.read_html('https://finance.naver.com/sise/lastsearch2.nhn',
                  encoding='euc-kr')
stock = df[1].dropna()
stock.index = stock['순위']
del stock['순위']
print(stock)

# print(stock['검색비율'].str.strip('%'))
stock['검색비율'] = stock['검색비율'].str.strip('%')
print(stock)
new_stock = stock.astype({'검색비율': float})
print(sum(new_stock['검색비율']))

df1 = pd.DataFrame(
    {'상품번호': ['p1', 'P2', 'p3', 'P4'],
     '수량': ['3,000', '2,000', '5,000', '6,000']},
)
print(df1)
df1['상품번호'] = df1['상품번호'].str.upper()
print(df1)
df1['수량'] = df1['수량'].str.replace(',', '')
df1_new = df1.astype({'수량': float})
print(df1_new)