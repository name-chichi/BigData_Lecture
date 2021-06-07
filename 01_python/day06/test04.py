d1 = [4,3,5,2,1];
d2 = ['Korea','japan','China','america'];
d2.sort(key=str.lower);
print(d2);

print(max(d1));
print(min(d1));

d1.sort(reverse=True);
print(d1);

d1.reverse();
print(d1);

d3 = [8,2,4,6,1];
d4 = sorted(d3,reverse=True);
print(d3);
print(d4);
