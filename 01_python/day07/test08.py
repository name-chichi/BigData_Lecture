loc = ['서울','부산','광주','대구','대전'];
data = [28.8,33.7,29.4,35.2,26.3];

# 지역 별 평균 온도 데이터 집계이다.
# Dictionary로 만든다.
# 온도가 높은 순으로 정렬하여 출력 한다.

loc_data = dict(zip(loc,data));
print(loc_data);

sort_data = sorted(loc_data.items(),key=lambda x:x[1],reverse=True);
print(sort_data);