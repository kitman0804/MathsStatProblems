"""
Question 25 in 
http://cemc.uwaterloo.ca/contests/past_contests/2016/2016PascalContest.pdf
"""
import numpy as np

# Brutal 2**9 = 512
n = 0
for g1 in [0, 1]:
    for g2 in [0, 1]:
        for g3 in [0, 1]:
            for g4 in [0, 1]:
                for g5 in [0, 1]:
                    for g6 in [0, 1]:
                        for g7 in [0, 1]:
                            for g8 in [0, 1]:
                                for g9 in [0, 1]:
                                    grid = np.array([[g1, g2, g3], [g4, g5, g6], [g7, g8, g9]])
                                    colSum = np.sum(grid, axis = 0)
                                    rowSum = np.sum(grid, axis = 1)
                                    n += not ((0 in colSum) | (3 in colSum) | (0 in rowSum) | (3 in rowSum))

print(n)




# Smarter brutal 6**3 = 216
psbl_row = [np.array([1, 0, 0]), 
            np.array([0, 1, 0]), 
            np.array([0, 0, 1]), 
            np.array([0, 1, 1]), 
            np.array([1, 0, 1]), 
            np.array([1, 1, 0])]
psbl_row = np.array(psbl_row)

n = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            colSum = np.sum(psbl_row[[i, j, k]], axis = 0)
            n += not ((0 in colSum) | (3 in colSum))

print(n)