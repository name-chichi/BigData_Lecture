from decimal import Decimal
from fractions import Fraction

f = Decimal('0.1');
print(type(f));

sum = 0;
for i in range(100):
    sum += f;

print(sum);

a = Fraction(1,3);
print(a);