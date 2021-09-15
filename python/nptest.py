#! /usr/local/bin/python3

import numpy as np
#import linalg as lin

a = np.array([1,2,3])
b = np.array([4,5,6])

c = 2 * (a + b)
print(c)

x = np.dot(a,a)
print(x)

y = np.linalg.norm(a)
print(y*y)
