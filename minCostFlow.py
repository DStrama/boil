import numpy as np
from scipy.optimize import linprog

class Solver:

    def calculate_min_flow(self, supply, demand, flow_value):
        A = np.array([[-1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0, -1, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, -1, 0, -1, 1],
                      [0, 0, 0, 0, -1, 0, 0, -1, 0, -1],
                      [0, 0, -1, -1, 0, 1, 1, 1, 0, 0]])

        b = np.array([supply[0], supply[1], -demand[0], -demand[1], -demand[2], 0])
        c = np.array([flow_value[0], flow_value[1], flow_value[2], flow_value[3], flow_value[4], flow_value[5], flow_value[6], flow_value[7], flow_value[8], flow_value[9]])
        res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
        print('Optimal value:', round(res.fun), '\nX:', np.ndarray.round(res.x))
        return res


# A = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [-1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#               [0, -1, 0, -1, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 1, 1, 1, -1, 0, 0, 0],
#               [0, 0, -1, 0, -1, 0, 1, 1, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, -1, 1, 0],
#               [0, 0, 0, 0, 0, -1, 0, 0, -1, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, -1]])
#
# b = np.array([10, 0, -3, 2, 0, -1, 0, -8])
# c = np.array([2,2,3,4,2,2,1,5,3,2])

# =======================================================

# A = np.array([[-1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#               [0, -1, 0, 0, 0, -1, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, -1, 0, -1, 1],
#               [0, 0, 0, 0, -1, 0, 0, -1, 0, -1],
#               [0, 0, -1, -1, 0, 1, 1, 1, 0, 0],
#               [0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#               ])

# b = np.array([250, 300, -120, -250, -100, 0, -30, 50, 150])
# c = np.array([2, 3, 5, 6, 2, 5, 4, 1, 8, 4])

