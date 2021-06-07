def calc(*n):
    sum = 0;
    # [1,2,3,4,5]
    for i in n:
        sum += i;
    return sum/len(n);

r1 = calc(1,2,3,4,5);
r2 = calc(1,2,3,4,5,6,7,8);
print(r1);
print(r2);