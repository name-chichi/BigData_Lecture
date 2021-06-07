# 4과목(90 80 100 80) 성적을 입력 받는다.
# 4과목 평균이
# 90점 이상이면 "A학점"
# 80점 이상이면 "B학점"
# 70점 이상이면 "C학점"
# 60점 이상이면 "D학점"
# 60점 미만이면 "F학점"

ko = 90;
ma = 80;
en = 70;
si = 70;

avg = (ko+ma+en+si)/4;
print(avg);

if avg >= 90:
    print('A학점');
elif avg >= 80:
    print('B학점');
elif avg >= 70:
    print('C학점');
elif avg >= 60:
    print('D학점');
else:
    print('F학점');


print('---------------------------------------------');

# 91 ~ 95: A  96~100: A+
# 81 ~ 85: B  86~90: B+
# 71 ~ 75: C  76~80: C+
# 61 ~ 65: D  66~70: D+
# 60 이하는 F

if avg >= 96 and avg <= 100:
    print('A+학점');
elif avg >= 91 and avg <= 95:
    print('A학점');
elif avg >= 86 and avg <= 90:
    print('B+학점');
elif avg >= 81 and avg <= 85:
    print('B학점');
elif avg >= 76 and avg <= 80:
    print('C+학점');
elif avg >= 71 and avg <= 75:
    print('C학점');
elif avg >= 66 and avg <= 70:
    print('D+학점');
elif avg >= 61 and avg <= 65:
    print('D학점');
else:
    print('F학점');

print('-------------------------------------------------------');

if avg > 90:
    if avg >= 96:
        print('A+');
    else:
        print('A');
elif avg > 80:
    if avg >= 86:
        print('B+');
    else:
        print('B');
elif avg > 70:
    print('C');
elif avg > 60:
    print('D');
else:
    print('F');












