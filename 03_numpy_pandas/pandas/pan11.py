import pandas as pd
import numpy as np

data = [1, 2, 3, 4]
print('#1', data * 2, '\n')

n1 = np.array(data)
print('#2', n1 + 2, '\n')

p1 = pd.Series(data)
print('#3', p1, '\n')

p2 = p1.copy()
p2[4] = 10
print('#4', p1 / p2, '\n')

print('----------------------------------------')

x = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list('abcd'))
print('#5', x, '\n')
xx = x.loc[1]   # 4,5,6,7
print('#6', x.add(xx), '\n') # x + xx
print('#7', x + [9, 9, 9, 9], '\n')