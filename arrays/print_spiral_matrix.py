# #print spiral matrix
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# res = []

# for i in matrix:
#     for j in i:
#         res.append(j)

# print(res)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# res = []

# top, bottom = 0, len(matrix)-1
# left, right = 0, len(matrix[0])-1

# while top <= bottom and left <= right:
#     # Traverse right
#     for j in range(left, right+1):
#         res.append(matrix[top][j])
#     top += 1

#     # Traverse down
#     for i in range(top, bottom+1):
#         res.append(matrix[i][right])
#     right -= 1

#     # Traverse left
#     if top <= bottom:
#         for j in range(right, left-1, -1):
#             res.append(matrix[bottom][j])
#         bottom -= 1

#     # Traverse up
#     if left <= right:
#         for i in range(bottom, top-1, -1):
#             res.append(matrix[i][left])
#         left += 1

# print(res)

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # Traverse downwards
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Traverse from right to left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # Traverse upwards
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
