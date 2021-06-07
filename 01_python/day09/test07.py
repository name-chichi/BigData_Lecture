def calc(op,a,b):
    return op(a,b);

def add(a,b):
    return a+b;

def multi(a,b):
    return a*b;

# ----------------------------------------
result = calc(multi,10,20);
print(result);


def calsum(n):
    def add(a,b):
        return a+b;
    sum = 0;
    for i in range(n+1):
        sum = add(sum,i);
    return sum;

print(calsum(10));


def f1(msg):
    def hello(name):
        return msg+' '+name;
    return hello;

myfunc = f1('Hi!!!');

print(myfunc('jeams'));



















