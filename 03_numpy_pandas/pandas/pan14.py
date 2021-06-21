import pandas as pd
import numpy as np

x1 = pd.DataFrame(np.random.randint(0, 100, (3, 4)), columns=list('ABCD'), index=np.arange(3))
x2 = pd.DataFrame(np.random.randint(100, 200, (3, 4)), columns=list('ABCD'), index=np.arange(3)+3)
x22 = pd.DataFrame(np.random.randint(100, 200, (3, 4)), columns=list('ABCD'), index=np.arange(3))
print('#1', x1, '\n')
print('#2', x2, '\n')

x3 = pd.concat([x1, x2], axis=0)
print('#3', x3, '\n')

x4 = pd.concat([x1, x2], axis=1)
print('#4', x4, '\n')

x5 = pd.concat([x1, x22], axis=1)
print('#5', x5)