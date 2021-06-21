import numpy as np

ldata = [1, 2, 3, 4, 5]
print(ldata)    # [1, 2, 3, 4, 5]
print(type(ldata)) # <class 'list'>
print(ldata[2:]) # [3, 4, 5]

ndata = np.array(ldata)
print(ndata)    # [1 2 3 4 5]
print(type(ndata))  # <class 'numpy.ndarray'>
print(ndata[2:])    # [3 4 5]

a = np.eye(5)
print(a)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

#print(ldata + 5)
print(ndata / 5)    # [0.2 0.4 0.6 0.8 1. ]
ndatas = np.sqrt(ndata)
print(ndatas)   # [1.         1.41421356 1.73205081 2.         2.23606798]

ndata2 = np.zeros(5)
print(ndata2 + 6)   # [6. 6. 6. 6. 6.]

ndata3 = np.arange(-5, 5)
print(ndata3)   # [-5 -4 -3 -2 -1  0  1  2  3  4]
print(ndata3 > 2)   # [False False False False False False False False  True  True]
print(ndata3[ndata3 > 2])   # [3 4]

data1 = [10,9,33,88,66,55,40]

ndata1 = np.array(data1)
result = ndata1[ndata1 > 50]
print(result)   # [88 66 55]

# 짝수만 result2에 추츨 하시오
result2 = ndata1[ndata1 % 2 == 0]
print(result2)  # [10 88 66 40]
result3 = result2.tolist()
print(result3)  # [10, 88, 66, 40]