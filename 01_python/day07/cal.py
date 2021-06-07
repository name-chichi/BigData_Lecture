def calc(n):
    if n == 0:
        raise ZeroDivisionError;
    if n < 0:
        raise ValueError;
    result = 100 / n;
    return result;