
st = input('Input number');
try:
    num = int(st);
    result = num *100;
    print('%d , %d' % (num, result));
except:
    print('Invalid Number .. Try Again');

print('end.......');
