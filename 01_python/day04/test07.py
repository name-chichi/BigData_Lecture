def func(**n):
    w = n['w'];
    h = n['h'];
    return (w**2 + h**2) ** 0.5;

result = func(w=90,h=80);
print(result);
