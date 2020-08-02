import numpy as np
import time
import sys

# showing numpy array takes less space than python list
l = range(1000)
print(sys.getsizeof(5) * len(l)) # size of one python object is 14

array = np.arange(1000)
print(array.size * array.itemsize)


# showing numpy array takes less time than python list

SIZE = 10000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [(x + y) for x, y in zip(l1,l2)]
print("python list takes: ", (time.time() - start) * 1000)

# numpy array
start = time.time()
result = a1 + a2
print(" numpy takes: ", (time.time() - start) * 1000)






