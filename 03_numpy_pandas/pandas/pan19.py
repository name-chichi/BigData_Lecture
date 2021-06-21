import pandas as pd

df1 = pd.DataFrame(
    {
        '상품번호': ['p1', 'P1', 'p2', 'P2'],
        '수량': ['3,000', '2,000', '5,000', '6,000']
    }
)
print(df1, '\n')

df1['상품번호'] = df1['상품번호'].str.upper()   # 대문자 일괄처리
df1['수량'] = df1['수량'].str.replace(',', '')  # 천단위 일괄처리
df1 = df1.astype({'수량': float})
print(df1, '\n')

gdf1= df1.groupby(by=['상품번호'], as_index=False).sum()    # 상품번호로 그룹화 후 sum
print(gdf1, '\n')

gdf1= df1.groupby(by=['상품번호'], as_index=False).mean()   # 상품번호로 그룹화 후 mean
print(gdf1, '\n')

df1['고객번호'] = ['C1', 'C2', 'C2', 'C2']
print(df1, '\n')

new_df1 = df1.groupby(by=['고객번호', '상품번호'], as_index=False).count()  # 고객번호와 상품번호로 그룹화 후 count
print(new_df1)