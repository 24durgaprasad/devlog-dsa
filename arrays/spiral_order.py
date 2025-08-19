
# Given an M * N matrix, print the elements in a clockwise spiral manner. Return an array with the elements in the order of their appearance when printed in a spiral manner.

matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

def spiralOrder(matrix):
    result = []
    
    if not matrix:
        return result
    
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
