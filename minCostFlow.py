import numpy as np
from scipy.optimize import linprog

np.set_printoptions(suppress=True)

A = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [-1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, -1, 0, -1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, -1, 0, 0, 0],
              [0, 0, -1, 0, -1, 0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, -1, 1, 0],
              [0, 0, 0, 0, 0, -1, 0, 0, -1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, -1]])

b = np.array([10, 0, -3, 2, 0, -1, 0, -8])
c = np.array([2,2,3,4,2,2,1,5,3,2])

res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

print('Optimal value:', round(res.fun), '\nX:', np.ndarray.round(res.x))



