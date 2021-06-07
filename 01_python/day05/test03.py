num = input('Input Number ..?');
if not(num.isspace()) and num.isnumeric():
    result = int(num) * 100;
    print(result);
else:
    print('Invalid Number .. Try Again');