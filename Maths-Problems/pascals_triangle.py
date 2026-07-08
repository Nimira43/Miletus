import numpy as np
import matplotlib.pyplot as plt
import math

def nChooseK(n,k):
  num = math.factorial(n)
  den = math.factorial(k) * math.factorial(n-k)
  return num / den

pascal_size = 5
pascal_triangle = np.zeros((pascal_size, pascal_size), dtype=int)

for n in range(pascal_size):
  for k in range(n + 1):
    pascal_triangle[n, k] = nChooseK(n,k)

# print(pascal_triangle)
plt.imshow(pascal_triangle)
plt.show()

for i in range(pascal_size):
  temp = pascal_triangle[i,:]
  temp = temp[temp != 0]
  print(' ' * (pascal_size - i) + np.array2string(temp)[1:-1])